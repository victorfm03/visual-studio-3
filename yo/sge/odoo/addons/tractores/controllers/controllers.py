# -*- coding: utf-8 -*-
# from odoo import http


# class Tractores(http.Controller):
#     @http.route('/tractores/tractores/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tractores/tractores/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tractores.listing', {
#             'root': '/tractores/tractores',
#             'objects': http.request.env['tractores.tractores'].search([]),
#         })

#     @http.route('/tractores/tractores/objects/<model("tractores.tractores"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tractores.object', {
#             'object': obj
#         })
