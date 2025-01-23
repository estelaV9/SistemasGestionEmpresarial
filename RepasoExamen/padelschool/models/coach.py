from odoo import fields, api, models

"""
Monitor (coach), con su nombre (no se puede dejar en blanco), 
apellidos (no se puede dejar en blanco), correo, teléfono 
"""


class coach(models.Model):
    _name = 'padelschool.coach'
    _description = 'padelschool.coach'

    # CAMPO OBLIGATORIO PARA EL NOMBRE DEL ENTRENADOR
    name = fields.Char(string="Nombre", readonly=False, required=True,
                       help="Introduzca el nombre")
    # CAMPO OBLIGATORIO PARA EL APELLIDO DEL ENTRENADOR
    last_name = fields.Char(string="Apellido", readonly=False, required=True,
                            help="Introduzca el apellido")

    mail = fields.Text(string="Correo")
    phone = fields.Text(string="Telefono")

    # UN MONITOR PUEDE IMPARTIR VARIOS CURSOS A LA VEZ
    course_coach_id = fields.One2many(string="Cursos",
                                      comodel_name="padelschool.course",
                                      inverse_name="coach_course_id")

    """ MEJORAS PARA ESTUDIAR EL CAMPO COMPUTADO """
    # Contar el número de cursos impartidos por un monitor
    total_course = fields.Integer(string="Numeros cursos por monitor", compute="_get_total_course")

    @api.depends('course_coach_id')
    def _get_total_course(self):
        for coach in self:
            coach.total_course = len(self.course_coach_id)

    # En el modelo coach, crea un campo computado que calcule la duración total
    # de todos los cursos que está impartiendo ese monitor.
    total_duration = fields.Integer(string="Duracion total de los cursos del monitor", compute="_get_total_duration")

    @api.depends('course_coach_id')
    def _get_total_duration(self):
        for coach in self:
            total_duration = sum(course.duration for course in coach.course_coach_id)
            coach.total_duration = total_duration

    # En el modelo coach, crea un campo computado que muestre cuántos
    # cursos está impartiendo un monitor en total.
    num_course = fields.Integer(string="Numero de cursos", compute="_get_num_course")

    @api.depends('course_coach_id')
    def _get_num_course(self):
        for coach in self:
            total = len(coach.course_coach_id)
            coach.num_course = total
