# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):

    _name = 'library.book'
    _description = 'Libreria'

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string='Active', default=True)

    ISBN = fields.Char(string="ISBN")
    genre = fields.Char(string="Genre")
    summary = fields.Text(string="Summary")
    author = fields.Char(string="Autor")
    format = fields.Selection(string='Level',
                              selection=[('paperback', 'Paperback'),
                                         ('hardcover', 'Hardcover'),
                                         ('audiobook', 'Audiobook'),
                                         ('ebook', 'E-Book')],
                              copy=False)

    language = fields.Selection(string='Language',
                                selection=[('en', 'English'),
                                           ('es', 'Spanish'),
                                           ('fr', 'French'),
                                           ('ptbr', 'Portuguese')],
                                copy=False)

    edition = fields.Integer(string="Edition")
    publisher = fields.Char(string="Publisher")
    publish_date = fields.Date(string="Publish date")
    price = fields.Monetary(string='Price')
    currency_id = fields.Many2one('res.currency')
