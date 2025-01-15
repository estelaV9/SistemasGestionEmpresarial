# -*- coding: utf-8 -*-

from odoo import models, fields, api


# MODELO TECHNOLOGY
# ESTA CLASE REPRESENTA UNA TECNOLOGÍA UTILIZADA EN EL DESARROLLO DE PROYECTOS.
# LAS TECNOLOGÍAS PUEDEN ESTAR RELACIONADAS CON TAREAS Y DESARROLLADORES.
class technology(models.Model):
    _name = 'manageestela.technology'
    _description = 'manageestela.technology'

    # NOMBRE DE LA TECNOLOGÍA. ES OBLIGATORIO Y DEBE SER ÚNICO.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # DESCRIPCIÓN OPCIONAL DE LA TECNOLOGÍA.
    description = fields.Char(string="Descripcion")

    # IMAGEN OPCIONAL PARA REPRESENTAR LA TECNOLOGÍA.
    image = fields.Image(string="Imagen")

    # RELACIÓN MANY2MANY ENTRE TECNOLOGÍAS Y TAREAS.
    # PERMITE ASOCIAR UNA TECNOLOGÍA CON LAS TAREAS QUE LA UTILIZAN.
    task_id = fields.Many2many(
        comodel_name="manageestela.technology",
        relation="technology_task",
        column1="task_id",
        column2="technology_id"
    )

    # RELACIÓN MANY2MANY ENTRE TECNOLOGÍAS Y DESARROLLADORES.
    # CADA TECNOLOGÍA PUEDE SER CONOCIDA POR VARIOS DESARROLLADORES.
    developer_id = fields.Many2many('res.partner',
                                    relation='developer_technologies',
                                    column1='technologies_id',
                                    column2='developer_id')