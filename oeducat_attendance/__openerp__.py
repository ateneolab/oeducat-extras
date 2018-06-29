# -*- coding: utf-8 -*-
{
    'name': "Openeducat Attendance Fixes",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Solem Consulting",
    'website': "www.solemconsulting.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Openeducat',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_erp', 'oeducat_roll_state'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/op_attendance_sheet_view.xml',
        'views/op_attendance_line_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
