# -*- coding: utf-8 -*-

from odoo import models, fields, api


class history(models.Model):
    _name = 'manageestela.history'
    _description = 'manageestela.history'

    # CAMPO QUE GUARDA EL NOMBRE DE LA HISTORIA. ESTE CAMPO ES OBLIGATORIO.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # CAMPO PARA UNA BREVE DESCRIPCIÓN DE LA HISTORIA.
    description = fields.Char(string="Descripcion")

    # RELACIÓN MANY2ONE ENTRE UNA HISTORIA Y SU PROYECTO.
    # CADA HISTORIA DE USUARIO ESTÁ ASOCIADA A UN SOLO PROYECTO.
    project_id = fields.Many2one("manageestela.project",
                                 string="Proyecto",
                                 required=True, ondelete="cascade")

    # RELACIÓN ONE2MANY ENTRE UNA HISTORIA Y LAS TAREAS QUE LA COMPONEN.
    # CADA HISTORIA DE USUARIO PUEDE DIVIDIRSE EN VARIAS TAREAS PARA SU IMPLEMENTACIÓN.
    task_history_id = fields.One2many(comodel_name="manageestela.task",
                                      inverse_name="history_task_id",
                                      string="Tarea ID")
