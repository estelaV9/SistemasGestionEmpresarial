from odoo import fields, api, models

"""
Monitor (coach), con su nombre (no se puede dejar en blanco), 
apellidos (no se puede dejar en blanco), correo, teléfono 
"""


class student(models.Model):
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

    """ MEJORAS PARA ESTUDIAR EL CAMPO COMPUTADO """
    # Campo computado que concatena el nombre y apellido de un estudiante:
    completed_name = fields.Text(string="Nombre completo", compute="_get_completed_name")

    @api.depends('name', 'last_name')
    def _get_completed_name(self):
        # SE RECORRE LOS ESTUDIANTES
        for student in self:
            student.completed_name = self.name + " " + self.last_name

    # En el modelo student, muestra una lista con todos los nombres de los monitores que han
    # impartido cursos en los que el estudiante está matriculado.
    list_coach = fields.Text(string="Lista monitores del curso", compute="_get_list_coach")

    @api.depends('course_id')
    def _get_list_coach(self):
        for student in self:
            # Creamos un conjunto para almacenar nombres únicos de monitores
            coach_names = set()

            # Recorremos los cursos en los que el estudiante está matriculado
            for course in student.course_id:
                if course.coach_course_id:  # Comprobamos que el curso tiene monitor
                    coach_names.add(course.coach_course_id.name)

            # Convertimos el conjunto en una cadena separada por comas
            student.list_coach = ', '.join(coach_names)

    # En el modelo student, crea un campo computado que devuelva una lista de
    # los nombres de los cursos en los que está matriculado ese estudiante.
    list_course = fields.Text(string="Lista cursos", compute="_get_list_course")

    @api.depends('course_id')
    def _get_list_course(self):
        for student in self:
            course_names = []  # Creamos una lista vacía
            for course in student.course_id:
                course_names.append(course.name)  # Agregamos el nombre de cada curso a la lista
            student.list_course = ', '.join(course_names)  # Unimos los nombres con una coma
