# -*- coding: utf-8 -*-
from openerp import http

# class OeducatRollState(http.Controller):
#     @http.route('/oeducat_roll_state/oeducat_roll_state/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oeducat_roll_state/oeducat_roll_state/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oeducat_roll_state.listing', {
#             'root': '/oeducat_roll_state/oeducat_roll_state',
#             'objects': http.request.env['oeducat_roll_state.oeducat_roll_state'].search([]),
#         })

#     @http.route('/oeducat_roll_state/oeducat_roll_state/objects/<model("oeducat_roll_state.oeducat_roll_state"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oeducat_roll_state.object', {
#             'object': obj
#         })