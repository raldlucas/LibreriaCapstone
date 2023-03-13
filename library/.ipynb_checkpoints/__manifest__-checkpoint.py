# -*- coding: utf-8 -*-

{
    'name': 'Library ',
    'summary': """ Library Manager""",

    'description': """
        Module to manage a library
        """,

    'licence': 'OPL-1',

    'author': 'Odoo',

    'website': 'https://www.odoo.com',

    'category': 'Trainingg',

    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        #'views/book_menuitems.xml',
        #'views/book_view.xml',

    ],

    'demo': [

    ],

}