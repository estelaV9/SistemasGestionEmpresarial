from odoo import models, fields, api


# MODELO TECHNOLOGY
# ESTA CLASE REPRESENTA UNA TECNOLOGIA UTILIZADA EN EL DESARROLLO DE PROYECTOS.
# LAS TECNOLOGIAS PUEDEN ESTAR RELACIONADAS CON TAREAS Y DESARROLLADORES.
class Technology(models.Model):
    _name = 'manageestela.technology'
    _description = 'manageestela.technology'

    # NOMBRE DE LA TECNOLOGIA. ES OBLIGATORIO Y DEBE SER UNICO.
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")

    # DESCRIPCION OPCIONAL DE LA TECNOLOGIA.
    description = fields.Char(string="Descripcion")

    # IMAGEN OPCIONAL PARA REPRESENTAR LA TECNOLOGIA.
    image = fields.Image(string="Imagen")

    # RELACION MANY2MANY ENTRE TECNOLOGIAS Y TAREAS.
    # PERMITE ASOCIAR UNA TECNOLOGIA CON LAS TAREAS QUE LA UTILIZAN.
    task_id = fields.Many2many(
        comodel_name="manageestela.task",
        relation="technology_task",
        column1="technology_id",
        column2="task_id"
    )

    # RELACION MANY2MANY ENTRE TECNOLOGIAS Y DESARROLLADORES.
    # CADA TECNOLOGIA PUEDE SER CONOCIDA POR VARIOS DESARROLLADORES.
    developer_id = fields.Many2many('res.partner',
                                    relation='developer_technologies',
                                    column1='technologies_id',
                                    column2='developer_id')