# -*- coding: utf-8 -*-

from odoo import models, fields, api


class project(models.Model):
    _name = 'manageestela.project'
    _description = 'manageestela.project'

    # CAMPO QUE GUARDA EL NOMBRE DEL PROYECTO. ES OBLIGATORIO Y AYUDA A IDENTIFICARLO.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # CAMPO OPCIONAL PARA UNA BREVE DESCRIPCIÓN DEL PROYECTO.
    description = fields.Char(string="Descripcion")

    # RELACIÓN ONE2MANY ENTRE UN PROYECTO Y LAS HISTORIAS DE USUARIO QUE LE PERTENECEN.
    history_id = fields.One2many(comodel_name="manageestela.history",
                                 inverse_name="project_id",
                                 string="Historial")

    # RELACIÓN ONE2MANY ENTRE UN PROYECTO Y LOS SPRINTS QUE CONTIENE.
    sprint_project_id = fields.One2many(comodel_name="manageestela.sprint",
                                        inverse_name="project_sprint_id",
                                        string="Sprint")