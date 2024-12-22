from odoo import models, fields


class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    technologies_id = fields.Many2many('manageestela.technology',
                                       relation='developer_technologies',
                                       column1='developer_id',
                                       column2='technologies_id')
