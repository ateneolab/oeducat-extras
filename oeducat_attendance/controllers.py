# -*- coding: utf-8 -*-
from openerp import http

# class OeducatAttendance(http.Controller):
#     @http.route('/oeducat_attendance/oeducat_attendance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oeducat_attendance/oeducat_attendance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oeducat_attendance.listing', {
#             'root': '/oeducat_attendance/oeducat_attendance',
#             'objects': http.request.env['oeducat_attendance.oeducat_attendance'].search([]),
#         })

#     @http.route('/oeducat_attendance/oeducat_attendance/objects/<model("oeducat_attendance.oeducat_attendance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oeducat_attendance.object', {
#             'object': obj
#         })