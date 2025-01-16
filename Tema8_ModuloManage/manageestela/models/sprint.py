# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

# MODELO SPRINT
# ESTA CLASE REPRESENTA UNA ITERACIÓN O PERIODO DE TIEMPO DENTRO DE UN PROYECTO.
class sprint(models.Model):
    _name = 'manageestela.sprint'
    _description = 'manageestela.sprint'

    # CAMPO PARA EL NOMBRE DEL SPRINT. ES OBLIGATORIO Y DEBE SER ÚNICO PARA SU IDENTIFICACIÓN.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # CAMPO OPCIONAL PARA DESCRIPCIONES DETALLADAS DEL SPRINT.
    description = fields.Char(string="Descripcion")

    # CAMPO PARA INDICAR LA DURACIÓN DEL SPRINT EN DÍAS.
    duration = fields.Integer()

    # FECHA DE INICIO DEL SPRINT.
    start_date = fields.Datetime(string="Fecha Inicio")

    # FECHA DE FINALIZACIÓN CALCULADA AUTOMÁTICAMENTE BASADA EN LA DURACIÓN Y FECHA DE INICIO.
    end_date = fields.Datetime(compute="_get_end_date", store=True, string="Fecha Finalizacion")

    # RELACIÓN ONE2MANY ENTRE EL SPRINT Y LAS TAREAS ASIGNADAS A ESTE.
    task_id = fields.One2many(string="Tasks", comodel_name="manageestela.task",
                              inverse_name="sprint_id")

    # RELACIÓN MANY2ONE ENTRE EL SPRINT Y EL PROYECTO AL QUE PERTENECE.
    project_sprint_id = fields.Many2one("manageestela.project",
                                        ondelete="cascade",
                                        string="Projects")

    # MÉTODO PARA CALCULAR LA FECHA DE FINALIZACIÓN DEL SPRINT.
    # SI LA DURACIÓN O LA FECHA DE INICIO NO SON VÁLIDAS, SE MANTIENE LA FECHA DE INICIO COMO FECHA FINAL.
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date