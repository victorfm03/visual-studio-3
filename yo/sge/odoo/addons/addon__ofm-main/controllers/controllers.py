# -*- coding: utf-8 -*-
# from odoo import http


# class AddonOfm-main(http.Controller):
#     @http.route('/addon__ofm-main/addon__ofm-main/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addon__ofm-main/addon__ofm-main/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addon__ofm-main.listing', {
#             'root': '/addon__ofm-main/addon__ofm-main',
#             'objects': http.request.env['addon__ofm-main.addon__ofm-main'].search([]),
#         })

#     @http.route('/addon__ofm-main/addon__ofm-main/objects/<model("addon__ofm-main.addon__ofm-main"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addon__ofm-main.object', {
#             'object': obj
#         })
