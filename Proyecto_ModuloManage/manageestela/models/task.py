from odoo import models, fields, api
import datetime


class Task(models.Model):
    _name = 'manageestela.task'
    _description = 'manageestela.task'

    code = fields.Char(string="Código", compute="_get_code")

    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    description = fields.Char(string="Descripcion")
    start_date = fields.Datetime(string="Fecha Inicio")
    end_date = fields.Datetime(string="Fecha Finalizacion")
    is_paused = fields.Boolean(string="¿Está pausado?")

    # CADA SPRINT TIENE MULTIPLES TAREAS ASIGNADAS; CADA TAREA SE ASIGNA A
    # UN SPRINT ESPECIFICO
    sprint_id = fields.Many2one("manageestela.sprint", string="Sprint",
                                ondelete="cascade", compute="_get_sprint",
                                store=True)

    # CADA TAREA ESTA ASOCIADA A UNA HISTORIA
    history_task_id = fields.Many2one("manageestela.history",
                                      ondelete="cascade",
                                      string="Historia relacionada")

    # CADA TAREA SE USA MULTIPLE TECNOLOGIAS Y CADA TECNOLOGIA ESTA ASOCIADA
    # A MULTIPLES TAREAS
    technology_id = fields.Many2many(
        comodel_name="manageestela.technology",
        relation="technology_task",
        column1="technology_id",
        column2="task_id"
    )

    # @api.one
    def _get_code(self):
        for task in self:
            # try:
            task.code = "TSK_" + str(task.id)
            # _logger.info("Código generado: "+task.code)
        # except:
        # raise ValidationError(_("Generación de código errónea"))

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
