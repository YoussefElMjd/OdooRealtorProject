from odoo import api, fields, models, tools

class ProductTemplate(models.Model):
    _inherit = "product.template"

    idApart = fields.Many2one("apartment.sell", string='Apartment', ondelete='set null')
    idVendor = fields.Many2one("res.partner", string='vendor', ondelete='set null')