# -*- coding: utf-8 -*-
{
    'name': "Openeducat Student Filter by Branch Office",

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
    'category': 'OpenEducat',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'oeducat_multi_company', 'l10n_ec_reports'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/student_view.xml',
        'wizard/student_wizard.xml',
        'report/student_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}