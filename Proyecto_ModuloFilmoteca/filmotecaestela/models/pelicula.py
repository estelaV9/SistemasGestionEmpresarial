# -*- coding: utf-8 -*-
from encodings.punycode import selective_find

from odoo import models, fields, api
import datetime


class pelicula(models.Model):
    _name = 'filmotecaestela.pelicula'
    _description = 'filmotecaestela.pelicula'

    code = fields.Char(string="Código", compute = "_get_code")

    name = fields.Char(string="Nombre", readonly=False, required=True, help="Introduzca el nombre")
    description = fields.Text()
    film_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_spanish = fields.Boolean()
    image = fields.Image(string="Cartel de la pelicula")
    language = fields.Selection(
        selection=[
            ("es", "Español"),
            ("en", "Inglés"),
            ("de", "Alemán"),
            ("fr", "Francés"),
        ], default='es', string="Idioma"
    )

    opinion = fields.Selection(
        selection=[
            ("0", "Mala"),
            ("1", "Regular"),
            ("2", "Buena"),
        ], default='2', string="Opinion"
    )

    color = fields.Boolean(string="¿La película es en color?", help="Seleccione si la película es en color o en blanco y negro")

    genero_id = fields.Many2one("filmotecaestela.genero", string="Género", required=True, ondelete="cascade")
    tecnica_id = fields.Many2many(comodel_name= "filmotecaestela.tecnica",
                                  relation = "tecnicas_peliculas",
                                  column1 = "tecnicas_ids",
                                  column2 = "peliculas_ids")

    #@api.one PARA RECIBIR UN UNICO OBJETO
    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.code = "FILM_"+str(pelicula.id)
            else:
                pelicula.code = str(pelicula.genero_id.name).upper()+"_"+str(pelicula.id)


    def toggle_color(self):
        self.color = not self.color

    def f_create(self):
        pelicula = {
            "name": "Prueba ORM",
            "color": True,
            "genero_id": 1,
            "start_date": str(datetime.date(2022, 8, 8))
        }
        print(pelicula)
        self.env['filmotecaestela.pelicula'].create(pelicula)