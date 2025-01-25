from odoo import fields, api, models

"""
Curso (course), con su nombre (no se puede dejar en blanco), 
fecha de inicio, fecha de fin, duración en días, precio y breve 
descripción
"""


class course(models.Model):
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

    """
    price = fields.Float(string="Precio del curso",required=True)
    discount = fields.Float(string="Descuento a aplicar",required=True)
     @api.depends("price", "discount")
    def _get_end_price(self):
        for course in self:
            if course.discount > 0:
                course.end_price = course.price - course.discount
            else:
                course.end_price = course.price
    """

    """ REPASO """
    # En el modelo course, crea un campo computado que muestre el número
    # total de estudiantes matriculados en ese curso.
    total_student = fields.Integer(string="Total estudiantes en este curso", compute="_get_total_student")

    @api.depends('student_id')
    def _get_total_student(self):
        for course in self:
            total = len(course.student_id)
            course.total_student = total

    # En el modelo course, crea un campo computado que devuelva la fecha de finalización
    # del curso con la duración más larga de todos los cursos de esa escuela.
    longest_course = fields.Datetime(string="Fecha curso con la duracion mas larga", compute="_get_longest_course")

    @api.depends('school_id')
    def _get_longest_course(self):
        for course in self:
            max_duration = 0
            longest_course_end_date = False  # Inicializamos la fecha
            # Recorrer todos los cursos de la escuela asociada al curso actual
            for school_course in course.school_id.course_id:
                if school_course.duration > max_duration:
                    max_duration = school_course.duration
                    longest_course_end_date = school_course.end_date
            course.longest_course = longest_course_end_date

    # En el modelo course, crea un campo computado que devuelva el nombre completo del monitor
    # (nombre y apellido) que está impartiendo ese curso.
    coach_name = fields.Text(string="Nombre monitor curso", compute="_get_coach_name")

    @api.depends('coach_course_id')
    def _get_coach_name(self):
        for course in self:
            if course.coach_course_id:
                # Concatenar el nombre y el apellido del monitor
                full_name = course.coach_course_id.name + " " + course.coach_course_id.last_name
                course.coach_name = full_name
            else:
                course.coach_name = ""  # En caso de que no haya monitor asignado
