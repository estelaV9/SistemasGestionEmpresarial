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
    logo = fields.Binary(string="logotipo")

    # DATOS COMPLETOS DE CONTACTO
    address = fields.Char(string="Direccion")
    mail = fields.Char(string="Correo")
    phone = fields.Integer(string="Telefono")

    description = fields.Text(string="Descripcion")

    # UNA ESCUELA PUEDE OFERTAR VARIOS CURSOS
    course_id = fields.One2many(comodel_name="padelschool.course",
                                inverse_name="school_id",
                                string="Cursos")

    """ Crear un campo computado para ver todos los alumnos que tiene matriculados 
        cada una de las escuelas de paddel. En la vista form de cada escuela, se debe 
        mostrar una tabla con los alumnos que tiene matriculados """

    student_in_school = fields.Text(string="Alumnos matriculados en las escuelas", compute_model="_get_student")

    # CAMPO COMPUTADO: ALUMNOS MATRICULADOS EN LA ESCUELA
    students = fields.Many2many(
        comodel_name="padelschool.student",
        compute="_compute_students",
        string="Alumnos Matriculados"
    )

    """ MEJORAS PARA ESTUDIAR EL CAMPO COMPUTADO """
    # Calcular la duración total de los cursos de una escuela
    duration_course = fields.Integer(string="Duracion", compute="_get_duration_course")

    @api.depends('course_id.start_date', 'course_id.end_date')
    def _get_duration_course(self):
        for school in self:
            total_duration = 0  # INICIALIZAR LA DURACION TOTAL
            for course in school.course_id:  # ITERAR SOBRE LOS CURSOS DE LA ESCULA
                if course.initDate and course.finishDate:  # COMPROBAR QUE LAS FECHAS NO SEAN NULL
                    duration = (course.finishDate - course.initDate).days  # SE CALCULA LA DURACION EN DIAS
                    total_duration += duration  # SE SUMA AL TOTAL
            school.duration_course = total_duration  # SE ASIGNA EL TOTAL AL CAMPO COMPUTADO

    # En el modelo school, busca todos los cursos de una escuela y cuenta cuántos cursos tiene.
    total_course = fields.Integer(string="Total cursos", compute="_get_total_course")

    @api.depends('course_id')
    def _get_total_course(self):
        for school in self:
            # Calcula directamente el número de cursos relacionados
            school.total_course = len(school.course_id)

    # En el modelo school, crea un campo computado para mostrar una lista con todos los
    # nombres de los monitores que están impartiendo cursos en esa escuela.
    list_coach_course = fields.Text(string="Monitores de los cursos", compute="_get_list_coach_course")

    @api.depends('course_id')
    def _get_list_coach_course(self):
        for school in self:
            # Usamos un conjunto para evitar nombres duplicados
            coach_names = set()

            # Iteramos sobre los cursos de la escuela
            for course in school.course_id:
                if course.coach_course_id:  # Verificamos que el curso tenga un monitor
                    coach_names.add(course.coach_course_id.name)

            # Convertimos el conjunto en una cadena separada por comas
            school.list_coach_course = ', '.join(coach_names)

    # En el modelo school, crea un campo computado que calcule el promedio de
    # duración de los cursos que ofrece esa escuela.
    average_duration = fields.Integer(string="Promedio duracion cursos", compute="_get_average_duration")

    @api.depends('course_id')
    def _get_average_duration(self):
        for school in self:
            total = 0
            numberCourse = len(school.course_id)

            # Solo hacer la división si hay cursos
            if numberCourse > 0:
                for course in school.course_id:
                    total += course.duration
                school.average_duration = total / numberCourse
            else:
                school.average_duration = 0  # Si no hay cursos, el promedio es 0

    # En el modelo school, crea un campo computado que muestre un listado de los nombres de
    # todos los estudiantes matriculados en los cursos de esa escuela.
    list_name_student = fields.Text(string="Lista nombres estudiantes", compute="_get_list_name_student")

    @api.depends('course_id.student_id')
    def _get_list_name_student(self):
        # Itero las escuelas
        for school in self:
            students = []
            # Si la escuela tiene cursos, recorro los cursos
            for course in school.course_id:
                # Si el curso tiene estudiantes, los agrego a la lista
                for student in course.student_id:
                    students.append(student.name)

            # Unifico todos los nombres en un solo string, separados por comas
            school.list_name_student = ' ,'.join(students)

    # En el modelo school, crear un campo computado para ver todos los alumnos que tiene
    # matriculados cada una de las escuelas de paddel. En la vista form de cada escuela,
    # se debe mostrar una tabla con los alumnos que tiene matriculados
    list_student = fields.Text(string="Alumnos matriculados", compute="_get_list_student")

    @api.depends('students')
    def _get_list_student(self):
        for school in self:
            list = []
            for student in school.students:
                list.append(student.name)
            school.list_student = ' ,'.join(list)

    """ tambien se puede de esta manera
        def _compute_student_names(self):
        for school in self:
            # Buscar los alumnos relacionados con la escuela mediante los cursos
            students = self.env["padelschool.student"].search([
                ("courses.school", "=", school.id)
            ])
            school.asigned_students = students
    """


    # Ejercicio 1: Crear un nuevo curso para una escuela
    # Crea un nuevo curso para una escuela existente. El curso debe tener un nombre,
    # fecha de inicio, fecha de fin y duración. Usa los métodos create y search.

    def write(name):
        # Buscamos la escuela por nombre
        schoolExists = env['padelschool.school'].search([('name', '=', school_name)], limit=1)

        if schoolExists:
            # Creamos un nuevo curso para la escuela encontrada
            new_course = env['padelschool.course'].create({
                'name': 'Nuevo Curso',  # Nombre del curso
                'start_date': datetime(2025, 2, 1),  # Fecha de inicio (en formato datetime)
                'end_date': datetime(2025, 6, 1),  # Fecha de fin (en formato datetime)
                'duration': (datetime(2025, 6, 1) - datetime(2025, 2, 1)).days,  # Duración en días
                'school_id': schoolExists.id,  # Relacionamos con la escuela encontrada
            })
            return new_course
        else:
            print("Escuela no encontrada.")
            return None


    # Ejercicio 3: Obtener todos los estudiantes de una escuela
    # Escribe un código que te devuelva todos los estudiantes matriculados en los cursos
    # de una escuela. Usa search para encontrar la escuela y luego accede a los estudiantes.
    def search(self, school_name):
        school_search = self.search(['name', '=', school_name], limit=1)
        if school_search:
            # Creamos una lista vacía para almacenar los estudiantes
            students_list = []

            # Iteramos sobre todos los cursos de la escuela
            for course in school_search.course_id:
                # Añadimos los estudiantes de cada curso a la lista
                for student in course.student_id:
                    students_list.append(student.name)  # Agregamos el nombre del estudiante

            # Devolvemos la lista de estudiantes como una cadena separada por comas
            return ', '.join(students_list)
        else:
            print("Escuela no encontrada.")
            return None