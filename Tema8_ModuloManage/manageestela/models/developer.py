from odoo import models, fields

# MODELO DEVELOPER
# ESTA CLASE EXTENDIÓ EL MODELO 'res.partner' PARA AGREGAR UNA RELACIÓN MANY2MANY
# ENTRE LOS DESARROLLADORES Y LAS TECNOLOGÍAS QUE UTILIZAN.
class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # RELACIÓN MANY2MANY ENTRE DESARROLLADORES Y TECNOLOGÍAS.
    # ESTA RELACIÓN ALMACENA LAS TECNOLOGÍAS QUE CADA DESARROLLADOR CONOCE.
    technologies_id = fields.Many2many('manageestela.technology',
                                       relation='developer_technologies',
                                       column1='developer_id',
                                       column2='technologies_id')
