from odoo import models, fields, api
import datetime

class Task(models.Model):
    _name = 'manageestela.task'
    _description = 'manageestela.task'

    # CODIGO GENERADO AUTOMATICAMENTE PARA IDENTIFICAR LA TAREA
    code = fields.Char(string="Codigo", compute="_get_code")

    # CAMPO OBLIGATORIO PARA EL NOMBRE DE LA TAREA
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # CAMPO OPCIONAL PARA DESCRIBIR LA TAREA
    description = fields.Char(string="Descripcion")

    # FECHAS DE INICIO Y FINALIZACION DE LA TAREA
    start_date = fields.Datetime(string="Fecha Inicializacion")
    end_date = fields.Datetime(string="Fecha Finalizacion")

    # BOOLEANO PARA INDICAR SI LA TAREA ESTA PAUSADA
    is_paused = fields.Boolean(string="¿Esta pausado?")

    # RELACION MANY2ONE ENTRE UNA TAREA Y EL SPRINT AL QUE PERTENECE
    sprint_id = fields.Many2one(
        "manageestela.sprint", string="Sprint",
        ondelete="cascade", compute="_get_sprint", store=True
    )

    # RELACION MANY2ONE ENTRE UNA TAREA Y LA HISTORIA DE USUARIO ASOCIADA
    history_task_id = fields.Many2one(
        "manageestela.history", string="Historia relacionada",
        ondelete="cascade"
    )

    # RELACION MANY2MANY ENTRE UNA TAREA Y LAS TECNOLOGIAS QUE UTILIZA
    technology_id = fields.Many2many(
        comodel_name="manageestela.technology",
        relation="technology_task",
        column1="task_id",
        column2="technology_id"
    )

    # RELACION MANY2MANY ENTRE LA TAREA Y LOS DESARROLLADORES
    developer_ids = fields.Many2many(
        'res.partner',  # MODELO DE DESARROLLADORES (res.partner)
        string="Desarrolladores",  # NOMBRE DEL CAMPO EN LA INTERFAZ
        domain="[('is_company', '=', False)]"  # FILTRAMOS SOLO LOS USUARIOS (DESARROLLADORES)
    )

    # ESTADO DE LA TAREA
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En progreso'),
        ('done', 'Completada'),
        ('cancelled', 'Cancelada')
    ], default='draft', string="Estado")

    # BARRA DE PROGRESO
    progress = fields.Float(string="Progreso", compute='_compute_progress')

    # ATRIBUTO PARA SABER SI SE ESTA APUNTO DE CUMPLIR LA FEHCA DE FINALIZACION
    time_limit = fields.Boolean(string="Plazo cercano", compute="_compute_time_limit")


    # METODO PARA GENERAR AUTOMATICAMENTE EL CODIGO DE LA TAREA
    def _get_code(self):
        for task in self:
            task.code = "TSK_" + str(task.id)


    # METODO PARA ASIGNAR AUTOMATICAMENTE UNA TAREA A UN SPRINT
    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['manageestela.sprint'].search(
                [('project_sprint_id.id', '=', task.history_task_id.project_id.id)]
            )
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
                    break

            if not found:
                task.sprint_id = False

    @api.depends('state', 'start_date', 'end_date', 'progress')
    def _compute_progress(self):
        for task in self:
            if task.state == 'done':
                # SI EL ESTADO DE LA TAREA ES 'done' SE SETTEA A 100 LA BARRA
                task.progress = 100  # COMPLETADA
            elif task.state == 'cancelled':
                # SI EL ESTADO DE LA TAREA ES 'cancelled' SE SETTEA A 0 LA BARRA
                task.progress = 0  # CANCELADA
            elif task.state == 'in_progress':
                # SI EL ESTADO DE LA TAREA ES 'in_progress' SE COGE EL DIA DE HOY Y CALCULAMOS EL PORCENTAJE
                today = datetime.datetime.today()  # OBTENEMOS LA FECHA Y HORA ACTUAL COMO DATETIME

                """ SE COMBINA LA FECHA CON UNA HORA DE 00:00 (datetime.time.min) PARA ASEGURAR LA COMPARACION
                DE FECHAS CONSIDERANDO LA FECHA Y NO LA HORA """
                start_datetime = datetime.datetime.combine(task.start_date, datetime.time.min)
                end_datetime = datetime.datetime.combine(task.end_date, datetime.time.min)

                if today > end_datetime:
                    # SI LA TAREA ESTA EN PROGRESO Y LA FECHA HA PASADO, PUEDE SEGUIR AUMENTANDO EL PROGRESO
                    """ nota: se calcula la diferencia entre la fecha actual y la finalizacion y extrae los dias
                    completos de esa diferencia (.day). Se multiplica entre 5 para incrementar la barra por cada dia 
                    que pasa """
                    task.progress = 100 + (today - end_datetime).days * 5  # AUMENTA EL PROGRESO MAS ALLÁ DEL 100%
                else:
                    # SI AUN NO SE HA PASADO LA FECHA, CALCULA EL PROGRESO NORMAL
                    """ la diferencia en dias de la fecha actual y la fecha de inicio entre la diferencia de dias
                    entre la fehca finalizacion y la de inicio == nos el tiempo transcurrido entre el inicio de la tarea
                    y el tiempo actual con respecto a la duracion de la tarea """
                    task.progress = (today - start_datetime).days / (end_datetime - start_datetime).days * 100
            else:
                # SI EL ESTADO DE LA TAREA ES 'draft', EL PORTENTAJE SERA 0
                task.progress = 0

            task.progress = min(task.progress, 200)  # SE PONE UN MINIMO DE QUE NO SUPERE EL 200%


    # METODO PARA SABER SI EL PLAZO DE LA TAREA ESTA A PUNTO DE TERMINA
    @api.depends('end_date')
    def _compute_time_limit(self):
        for task in self:
            # SI LA TAREA TIENE FECHA DE FINALIZACION Y ESA FECHA ES MENOR O IGUAL AL DIA DE HOY + 1 DIA
            if task.end_date and task.end_date <= datetime.datetime.now() + datetime.timedelta(days=1):
                task.time_limit = True # PLAZO CERCANO
            else:
                task.time_limit = False


    # METODO PARA CREAR UNA NOTIFICACION RELACIONADA CON LA TAREA Y EL USUARIO ACTUAL
    def _create_notification(self, notification_type, description):
        for task in self:
            # ESCRIBE LOS NOMBRES DE LOS DESARROLLADORES
            developers = ", ".join([dev.name for dev in task.developer_ids])
            # SE INCLUYEN LOS DESARROLLADORES EN LA DESCRIPCION
            description_with_devs = f"{description} (Desarrolladores: {developers})"

            self.env['manageestela.notification'].create({
                'user_id': self.env.user.id,  # ID DEL USUARIO ACTUAL
                # SI LA TAREA NO ES DELETE, ENTONCES ASIGNA EL ID,
                'task_id': task.id if notification_type != 'delete' else False,
                'description': description_with_devs,
                'notification_type': notification_type,  # TIPO DE NOTIFICACION (CREACION, ACTUALIZACION, ETC.)
            })

    # METODO PARA CREAR UNA TAREA
    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)  # CREA LA TAREA
        # CREA UNA NOTIFICACION DESPUES DE CREAR LA TAREA
        task._create_notification(
            # SE DEFINE LA NOTIFICACION DE CREADCION CON LA DESCRIPCION DE LA TAREA
            notification_type='create',  # TIPO: CREACION
            description=f"Se ha creado la tarea: {task.name}"
        )
        return task

    """ nota: en Odoo existen metodos ya predefinidos que se ejecutan automaticamente. 
    El metodo write se ejecuta uatomaticamente cuando se realiza una actualizacion en la tarea y lo mismo
    con el metodo unlink, se ejecuta automaticamente cuando se  elimina un registro """

    # METODO PARA CUANDO SE ACTUALIZA UNA TAREA
    def write(self, vals):
        taskUpdate = super(Task, self).write(vals)  # ACTUALIZA LA TAREA
        # RECORRE LAS TAREAS QUE ESTAN SIENDO ACTUALIZADAS
        for task in self:
            # COMPRUEBA SI SE HAN MODIFICADO EL CAMPO 'is_paused', 'start_date', 'end_date'
            if 'is_paused' in vals or 'start_date' in vals or 'end_date' in vals:
                # SI SE HAN MODIFICADO ESTOS CAMPOS, SE CREA UNA NOTIFICACION
                task._create_notification(
                    notification_type='update',  # TIPO: ACTUALIZACION
                    description=f"La tarea '{task.name}' ha sido actualizada."
                )
        return taskUpdate

    # METODO PARA ELIMINAR UNA TAREA
    def unlink(self):
        # RECORE LAS TAREAS QUE ESTAN SINEDO ELIMINADAS
        for task in self:
            # CREA UNA NOTIFICACION ANTES DE ELIMINAR LA TAREA
            self.env['manageestela.notification'].create({
                'user_id': self.env.user.id,
                'task_id': task.id,  # ASIGNA LA TAREA ANTES DE BORRARLA
                'description': f"La tarea '{task.name}' ha sido eliminada.",
                'notification_type': 'delete',  # TIPO: ELIMINACION
            })
        # LLAMA AL METODO PROPIO DE unlink PARA ELIMINAR LA TAREA
        return super(Task, self).unlink()  # ELIMINA LA TAREA

    # METODO ONCHANGE PARA GENERAR NOTIFICACIONES CUANDO LA FECHA FINAL ESTA CERCA
    @api.onchange('end_date') # DETECTA CAMBIOS EN UN CAMPO ESPECIFICO
    def _onchange_end_date(self):
        # SI HAY FECHA FINAL
        if self.end_date:
            # Y SI LA FECHA FINAL ESTA A MENOS DE 1 DIA DE DIFERENCIA
            if self.end_date - datetime.datetime.now() <= datetime.timedelta(days=1):
                # SE CREA LA NOTIFICACION DEL PLAZO CERCANO
                self._create_notification(
                    notification_type='deadline',  # TIPO: PLAZO CERCANO
                    description=f"La tarea '{self.name}' esta cerca de su plazo."
                )
