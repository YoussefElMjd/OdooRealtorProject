from curses import termname
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    # apartment_ids = fields.One2many('apartment.sell',inverse_name="best_offerer",string="Best Offerer")

    password = fields.Char('password',required=True)


