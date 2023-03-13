# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):

    _name = 'library.book'
    _description = 'Libreria'

    name = fields.Char(string="Title", required=True)