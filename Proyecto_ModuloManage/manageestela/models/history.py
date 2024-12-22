# -*- coding: utf-8 -*-

from odoo import models, fields, api


class history(models.Model):
    _name = 'manageestela.history'
    _description = 'manageestela.history'

    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    description = fields.Char(string="Descripcion")

    # CADA HISTORIA DE USUARIO PERTENECE A UN PROYECTO ESPECIFIC
    project_id = fields.Many2one("manageestela.project",
                                 string="Proyecto",
                                 required=True, ondelete="cascade")

    # CADA HISTORIA SE DIVIDE EN VARIAS TAREAS
    task_history_id = fields.One2many(comodel_name="manageestela.task",
                              inverse_name="history_task_id",
                              string="Tarea ID")
