from odoo import models, fields, api

"""
Escuela (school) con su nombre (no se puede dejar en blanco), 
logotipo, datos completos de contacto (dirección, correo, teléfono) 
y una descripción de la escuela
"""
class school(models.Model):
    _name = 'padelschool.school'
    _description = 'padelschool.school'

    # CAMPO OBLIGATORIO PARA EL NOMBRE DE LA ESCUELA
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    logo = fields.Image(string="logotipo")

    # DATOS COMPLETOS DE CONTACTO
    address = fields.Text(string="Direccion")
    mail = fields.Text(string="Correo")
    phone = fields.Text(string="Telefono")

    description = fields.Text(string="Descripcion")

    # UNA ESCUELA PUEDE OFERTAR VARIOS CURSOS
    course_id = fields.One2many(comodel_name="padelschool.course",
                                 inverse_name="school_id",
                                 string="Cursos")