from odoo import models, fields, api

# MODELO PARA GESTIONAR NOTIFICACIONES AUTOMATICAS
class Notification(models.Model):
    _name = 'manageestela.notification'
    _description = 'Notificaciones automAticas'

    # USUARIO AL QUE ESTA ASOCIADA LA NOTIFICACION
    user_id = fields.Many2one('res.users', string="Usuario", required=True)

    # TAREA RELACIONADA CON LA NOTIFICACION (OPCIONAL PARA ELIMINACION)
    task_id = fields.Many2one('manageestela.task', string="Tarea", required=False)

    # DESCRIPCION DE LA NOTIFICACION
    description = fields.Text(string="Descripcion", required=True)

    # TIPO DE NOTIFICACION (CREACION, ACTUALIZACION, ETC.)
    notification_type = fields.Selection([
        ('create', 'Creacion'),
        ('update', 'Actualizacion'),
        ('delete', 'Eliminacion'),
        ('deadline', 'Plazo cercano'),
    ], string="Tipo", required=True)

    # ESTADO DE LA NOTIFICACION (LEIDA O NO LEIDA)
    state = fields.Selection([
        ('unread', 'No leida'),
        ('read', 'Leida')
    ], string="Estado", default='unread')

    # FECHA EN QUE SE CREO LA NOTIFICACION
    creation_date = fields.Datetime(string="Fecha de creacion", default=fields.Datetime.now)

