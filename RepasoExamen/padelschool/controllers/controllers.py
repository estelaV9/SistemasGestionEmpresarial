# -*- coding: utf-8 -*-
# from odoo import http


# class Padelschool(http.Controller):
#     @http.route('/padelschool/padelschool', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/padelschool/padelschool/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('padelschool.listing', {
#             'root': '/padelschool/padelschool',
#             'objects': http.request.env['padelschool.padelschool'].search([]),
#         })

#     @http.route('/padelschool/padelschool/objects/<model("padelschool.padelschool"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('padelschool.object', {
#             'object': obj
#         })
