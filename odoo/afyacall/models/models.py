# -*- coding: utf-8 -*-

from odoo import models, fields, api


class afyacall(models.Model):
    _name = 'afyacall.products'
    _description = 'these are Afyacall products'

    name = fields.Char()
    product_id = fields.Integer()
    description = fields.Text()
    price = fields.Float(string="Price", digits=(16, 2), required=True)