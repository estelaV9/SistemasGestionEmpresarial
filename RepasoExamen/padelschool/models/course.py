from odoo import fields, api, models

"""
Curso (course), con su nombre (no se puede dejar en blanco), 
fecha de inicio, fecha de fin, duración en días, precio y breve 
descripción
"""
class course (models.Model):
    _name = 'padelschool.course'
    _description = 'padelschool.course'

    # CAMPO OBLIGATORIO PARA EL NOMBRE DE LA ESCUELA
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de fin")
    duration = fields.Integer(string="Duracion")

    mail = fields.Text(string="Correo")
    phone = fields.Text(string="Telefono")

    # CADA CURSO SOLO PUEDE PERTENECER A UNA ESCUELA
    school_id = fields.Many2one('padelschool.school', string="Escuela")

    # CADA CURSO SOLO PUEDE ESTAR IMPARTIDO POR UN MONITOR
    coach_course_id = fields.Many2one('padelschool.coach', string="Entrenador")

    # EN UN CURSO PUEDEN ESTAR MATRICULADOS VARIOS ALUMNOS
    student_id = fields.Many2many(comodel_name="padelschool.student",
                                  relation="student_course",
                                  column1="course_id",
                                  column2="student_id")