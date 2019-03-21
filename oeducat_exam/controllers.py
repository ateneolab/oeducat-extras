# -*- coding: utf-8 -*-
from openerp import http

# class OeducatExam(http.Controller):
#     @http.route('/oeducat_exam/oeducat_exam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oeducat_exam/oeducat_exam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oeducat_exam.listing', {
#             'root': '/oeducat_exam/oeducat_exam',
#             'objects': http.request.env['oeducat_exam.oeducat_exam'].search([]),
#         })

#     @http.route('/oeducat_exam/oeducat_exam/objects/<model("oeducat_exam.oeducat_exam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oeducat_exam.object', {
#             'object': obj
#         })