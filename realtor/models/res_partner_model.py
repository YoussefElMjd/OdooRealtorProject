from curses import termname
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    password = fields.Char('password',required=True)


