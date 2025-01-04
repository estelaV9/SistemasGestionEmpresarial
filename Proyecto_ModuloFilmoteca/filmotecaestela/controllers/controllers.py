# -*- coding: utf-8 -*-

"""
 class Filmotecaestela(http.Controller):
     @http.route('/filmotecaestela/filmotecaestela', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/filmotecaestela/filmotecaestela/objects', auth='public')
     def list(self, **kw):
         return http.request.render('filmotecaestela.listing', {
             'root': '/filmotecaestela/filmotecaestela',
             'objects': http.request.env['filmotecaestela.filmotecaestela'].search([]),
         })

     @http.route('/filmotecaestela/filmotecaestela/objects/<model("filmotecaestela.filmotecaestela"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('filmotecaestela.object', {
             'object': obj
         }"""

from odoo import http
from odoo.http import Response
import json
class pelicula_controller(http.Controller):

    @http.route('/api/peliculas', auth='public', method=['GET'], csrf=False)
    def get_peliculas(self, **kw):
        try:
            peliculas = http.request.env['filmotecaestela.pelicula'].sudo().search_read([], ['code', 'name', 'description'])
            res = json.dumps(peliculas, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)