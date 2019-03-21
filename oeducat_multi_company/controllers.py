# -*- coding: utf-8 -*-
from openerp import http

# class OeducatMultiCompany(http.Controller):
#     @http.route('/oeducat_multi_company/oeducat_multi_company/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oeducat_multi_company/oeducat_multi_company/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oeducat_multi_company.listing', {
#             'root': '/oeducat_multi_company/oeducat_multi_company',
#             'objects': http.request.env['oeducat_multi_company.oeducat_multi_company'].search([]),
#         })

#     @http.route('/oeducat_multi_company/oeducat_multi_company/objects/<model("oeducat_multi_company.oeducat_multi_company"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oeducat_multi_company.object', {
#             'object': obj
#         })