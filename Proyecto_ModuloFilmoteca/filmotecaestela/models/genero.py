
from odoo import models, fields, api


class genero(models.Model):
    _name = 'filmotecaestela.genero'
    _description = 'filmotecaestela.genero'

    name = fields.Char(string = "Nombre", readonly = False,
                       required = True, help = "Introduzca el nombre")
    description = fields.Text()

    peliculas_id = fields.One2many(string = "Películas", comodel_name = "filmotecaestela.pelicula", inverse_name = "genero_id")