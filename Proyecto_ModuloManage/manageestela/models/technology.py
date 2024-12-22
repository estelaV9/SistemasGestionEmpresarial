# -*- coding: utf-8 -*-

from odoo import models, fields, api


class technology(models.Model):
    _name = 'manageestela.technology'
    _description = 'manageestela.technology'

    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    description = fields.Char(string="Descripcion")
    image = fields.Image(string="Imagen")

    # CADA TAREA SE USA MULTIPLE TECNOLOGIAS Y CADA TECNOLOGIA ESTA ASOCIADA A
    # MULTIPLES TAREAS
    task_id = fields.Many2many(
        comodel_name="manageestela.technology",
        relation="technology_task",
        column1="task_id",
        column2="technology_id"
    )

    developer_id = fields.Many2many('res.partner',
                                    relation='developer_technologies',
                                    column1='technologies_id',
                                    column2='developer_id')