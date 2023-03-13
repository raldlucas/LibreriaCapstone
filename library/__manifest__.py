# -*- coding: utf-8 -*-

{
    'name': 'Biblioteca Odoo',
    'summary': """ Biblioteca para gestionar libros y clientes """,

    'description': """
        Modulo Biblioteca Odoo para manejar pratica:
        -Cursos
        -Sessions-
        -Attendees
        """,

    'licence': 'OPL-1',

    'author': 'Odoo',

    'website': 'https://www.odoo.com',

    'category': 'Training',

    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        #'views/book_menuitems.xml',
        'views/book_view.xml',

    ],

    'demo': [

    ],

}