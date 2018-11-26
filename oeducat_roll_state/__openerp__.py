# -*- coding: utf-8 -*-
{
    'name': "oeducat_roll_state",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_erp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'wizard/wizard_relocate_view.xml',
        'views/op_roll_number_view.xml',
        'cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}