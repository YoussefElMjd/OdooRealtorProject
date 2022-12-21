from odoo import models, fields, api, exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging


class Apartment(models.Model):
    _name = 'apartment.sell'
    _logger = logging.getLogger(__name__)

    name = fields.Char(string="", required=True)
    description = fields.Char(string="")
    image = image = fields.Binary('Image')
    availability = fields.Datetime()
    price = fields.Float('Price')
    apartment_surface = fields.Integer('Apartment surface')
    terrace_surface = fields.Integer('Terrace surface')
    total_surface = fields.Integer('Total surface',readonly="1")
    best_offerer = fields.Many2one(
        'res.partner', string='Best offerer', ondelete='set null')
    best_price_offer = fields.Float('Best price offer')
    idProduct = fields.Many2one(
        'product.template', string='Product', ondelete='set null')

    _sql_constraints = [
        ('uniq_name',
         'UNIQUE (name)',
         'Name already exists')
    ]

    @api.constrains('price')
    def _check_price(self):
        if self.price <= 0:
            raise exceptions.ValidationError('Price must be strictly positive')

    @api.constrains('availability')
    def _check_date_availability(self):
        for apartment in self:
            date_3_month_after = apartment.create_date + \
                relativedelta(months=3)
        if apartment.availability < date_3_month_after:
            raise exceptions.ValidationError(
                'Availability date must be 3 month after today.')

    @api.constrains('apartment_surface')
    def _check_apartment_surface(self):
        if self.apartment_surface <= 0:
            raise exceptions.ValidationError(
                'Apartment surface must be strictly positive')

    @api.constrains('terrace_surface')
    def _check_terrace_surface(self):
        if self.terrace_surface < 0:
            raise exceptions.ValidationError(
                'Terrace surface must be positive or null')

    @api.depends('apartment_surface', 'terrace_surface')
    def _change_total_surface(self):
        self.total_surface = self.apartment_surface + self.terrace_surface

    @api.onchange('terrace_surface')
    def _change_total_surface(self):
        self.total_surface = self.apartment_surface + self.terrace_surface

    @api.constrains('best_price_offer')
    def _check_best_price(self):
        if self.best_price_offer < self.price * 0.90:
            raise exceptions.ValidationError(
                'Best price must be 90 purcent of the price')
            
