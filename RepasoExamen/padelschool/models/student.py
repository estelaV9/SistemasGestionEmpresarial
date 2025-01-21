from odoo import fields, api, models

"""
Monitor (coach), con su nombre (no se puede dejar en blanco), 
apellidos (no se puede dejar en blanco), correo, teléfono 
"""
class student (models.Model):
    _name = 'padelschool.student'
    _description = 'padelschool.student'

    # CAMPO OBLIGATORIO PARA EL NOMBRE DEL ESTUDIANTE
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    # CAMPO OBLIGATORIO PARA EL APELLIDO DEL ESTUDIANTE
    last_name = fields.Char(string="Apellido", readonly=False, required=True,
                       help="Introduzca el apellido")

    mail = fields.Text(string="Correo")
    phone = fields.Text(string="Telefono")

    # EN UN CURSO PUEDEN ESTAR MATRICULADOS VARIOS ALUMNOS
    course_id = fields.Many2many(comodel_name="padelschool.course",
                                  relation="student_course",
                                  column1="student_id",
                                  column2="course_id")