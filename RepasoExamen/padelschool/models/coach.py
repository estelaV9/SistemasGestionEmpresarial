from odoo import fields, api, models

"""
Monitor (coach), con su nombre (no se puede dejar en blanco), 
apellidos (no se puede dejar en blanco), correo, teléfono 
"""
class coach (models.Model):
    _name = 'padelschool.coach'
    _description = 'padelschool.coach'

    # CAMPO OBLIGATORIO PARA EL NOMBRE DEL ENTRENADOR
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    # CAMPO OBLIGATORIO PARA EL APELLIDO DEL ENTRENADOR
    lastName = fields.Char(string="Apellido", readonly=False, required=True,
                       help="Introduzca el apellido")

    mail = fields.Text(string="Correo")
    phone = fields.Text(string="Telefono")

    # UN MONITOR PUEDE IMPARTIR VARIOS CURSOS A LA VEZ
    course_coach_id = fields.One2many(string="Cursos",
                                      comodel_name="padelschool.course",
                                      inverse_name="coach_course_id")