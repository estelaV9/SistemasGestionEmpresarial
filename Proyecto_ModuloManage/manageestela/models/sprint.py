# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class sprint(models.Model):
    _name = 'manageestela.sprint'
    _description = 'manageestela.sprint'

    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    description = fields.Char(string="Descripcion")

    duration = fields.Integer()

    start_date = fields.Datetime(string="Fecha Inicio")
    end_date = fields.Datetime(compute="_get_end_date", store=True,
                               string="Fecha Finalizacion")

    # CADA SPRINT TIENE MULTIPLES TAREAS ASIGNADAS; CADA TAREA SE ASIGNA A UN
    # SPRINT ESPECIFICO
    task_id = fields.One2many(string="Tasks", comodel_name="manageestela.task",
                              inverse_name="sprint_id")

    # CADA SPRINT PERTENECE A UN SOLO PROYECTO
    project_sprint_id = fields.Many2one("manageestela.project",
                                        ondelete="cascade",
                                        string="Projects")


    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if (isinstance(sprint.start_date, datetime.datetime) and
                    sprint.duration > 0):
                sprint.end_date = (sprint.start_date +
                                   datetime.timedelta(days=sprint.duration))
            else:
                sprint.end_date = sprint.start_date
