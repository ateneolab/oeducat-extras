# -*- coding: utf-8 -*-
{
    'name': "Estudiante en el movimiento de libros",

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
    'category': 'Open Educat',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'openeducat_erp', 'stock', 'product'],

    # always loaded
    'data': [
        'views/stock_move_view.xml',
        'views/product_template_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}