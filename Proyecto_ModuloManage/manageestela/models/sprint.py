# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


# MODELO SPRINT
# ESTA CLASE REPRESENTA UNA ITERACION O PERIODO DE TIEMPO DENTRO DE UN PROYECTO.
class sprint(models.Model):
    _name = 'manageestela.sprint'
    _description = 'manageestela.sprint'

    # CAMPO PARA EL NOMBRE DEL SPRINT. ES OBLIGATORIO Y DEBE SER UNICO PARA SU IDENTIFICACION.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # CAMPO OPCIONAL PARA DESCRIPCIONES DETALLADAS DEL SPRINT.
    description = fields.Char(string="Descripcion")

    # CAMPO PARA INDICAR LA DURACION DEL SPRINT EN DIAS.
    duration = fields.Integer()

    # FECHA DE INICIO DEL SPRINT.
    start_date = fields.Datetime(string="Fecha Inicio")

    # FECHA DE FINALIZACION CALCULADA AUTOMATICAMENTE BASADA EN LA DURACION Y FECHA DE INICIO.
    end_date = fields.Datetime(compute="_get_end_date", store=True, string="Fecha Finalizacion")

    # RELACION ONE2MANY ENTRE EL SPRINT Y LAS TAREAS ASIGNADAS A ESTE.
    task_id = fields.One2many(string="Tasks", comodel_name="manageestela.task",
                              inverse_name="sprint_id")

    # RELACION MANY2ONE ENTRE EL SPRINT Y EL PROYECTO AL QUE PERTENECE.
    project_sprint_id = fields.Many2one("manageestela.project",
                                        ondelete="cascade",
                                        string="Projects")

    # METODO PARA CALCULAR LA FECHA DE FINALIZACION DEL SPRINT.
    # SI LA DURACION O LA FECHA DE INICIO NO SON VALIDAS, SE MANTIENE LA FECHA DE INICIO COMO FECHA FINAL.
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date
