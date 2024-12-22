# -*- coding: utf-8 -*-
# from odoo import http


# class Manageestela(http.Controller):
#     @http.route('/manageestela/manageestela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manageestela/manageestela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manageestela.listing', {
#             'root': '/manageestela/manageestela',
#             'objects': http.request.env['manageestela.manageestela'].search([]),
#         })

#     @http.route('/manageestela/manageestela/objects/<model("manageestela.manageestela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manageestela.object', {
#             'object': obj
#         })
