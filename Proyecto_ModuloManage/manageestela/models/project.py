# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _name = 'manageestela.project'
    _description = 'manageestela.project'

    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    description = fields.Char(string="Descripcion")

    # CADA PROYECTO TIENE VARIAS HISTORIAS DE USUARIO
    history_id = fields.One2many(comodel_name="manageestela.history",
                                 inverse_name="project_id",
                                 string="Historial")

    # CADA PROYECTO TIENE VARIOS SPRINTS
    sprint_project_id = fields.One2many(comodel_name="manageestela.sprint",
                                        inverse_name="project_sprint_id",
                                        string="Sprint")