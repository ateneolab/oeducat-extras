# -*- coding: utf-8 -*-
from openerp import http

# class OeducatStudentFilter(http.Controller):
#     @http.route('/oeducat_student_filter/oeducat_student_filter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oeducat_student_filter/oeducat_student_filter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oeducat_student_filter.listing', {
#             'root': '/oeducat_student_filter/oeducat_student_filter',
#             'objects': http.request.env['oeducat_student_filter.oeducat_student_filter'].search([]),
#         })

#     @http.route('/oeducat_student_filter/oeducat_student_filter/objects/<model("oeducat_student_filter.oeducat_student_filter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oeducat_student_filter.object', {
#             'object': obj
#         })