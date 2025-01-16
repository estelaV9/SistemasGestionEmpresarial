from odoo import models, fields, api
import datetime


# MODELO TASK
# ESTA CLASE REPRESENTA UNA TAREA INDIVIDUAL DENTRO DEL PROCESO DE DESARROLLO.
# LAS TAREAS ESTÁN RELACIONADAS CON SPRINTS, HISTORIAS DE USUARIO Y TECNOLOGÍAS.
class Task(models.Model):
    _name = 'manageestela.task'
    _description = 'manageestela.task'

    # CÓDIGO GENERADO AUTOMÁTICAMENTE PARA IDENTIFICAR LA TAREA.
    code = fields.Char(string="Código", compute="_get_code")

    # CAMPO PARA EL NOMBRE DE LA TAREA. ES OBLIGATORIO PARA IDENTIFICARLA.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # CAMPO OPCIONAL PARA DESCRIBIR LA TAREA.
    description = fields.Char(string="Descripcion")

    # FECHAS DE INICIO Y FINALIZACIÓN DE LA TAREA.
    start_date = fields.Datetime(string="Fecha Inicio")
    end_date = fields.Datetime(string="Fecha Finalizacion")

    # BOOLEANO PARA INDICAR SI LA TAREA ESTÁ PAUSADA.
    is_paused = fields.Boolean(string="¿Está pausado?")

    # RELACIÓN MANY2ONE ENTRE UNA TAREA Y EL SPRINT AL QUE PERTENECE.
    sprint_id = fields.Many2one("manageestela.sprint", string="Sprint",
                                ondelete="cascade", compute="_get_sprint", store=True)

    # RELACIÓN MANY2ONE ENTRE UNA TAREA Y LA HISTORIA DE USUARIO ASOCIADA.
    history_task_id = fields.Many2one("manageestela.history",
                                      ondelete="cascade",
                                      string="Historia relacionada")

    # RELACIÓN MANY2MANY ENTRE UNA TAREA Y LAS TECNOLOGÍAS QUE UTILIZA.
    technology_id = fields.Many2many(
        comodel_name="manageestela.technology",
        relation="technology_task",
        column1="technology_id",
        column2="task_id"
    )

    # MÉTODO PARA GENERAR AUTOMÁTICAMENTE EL CÓDIGO DE LA TAREA.
    def _get_code(self):
        for task in self:
            task.code = "TSK_" + str(task.id)

    # MÉTODO PARA ASIGNAR AUTOMÁTICAMENTE UNA TAREA A UN SPRINT EN BASE A FECHAS Y PROYECTO.
    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['manageestela.sprint'].search([('project_sprint_id.id', '=', task.history_task_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
                    break

            if not found:
                task.sprint_id = False