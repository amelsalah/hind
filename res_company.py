from odoo import fields, models, api

# class ResPartner(models.Model) :

#     _inherit="res.partner"

    # name = fields.Char(index=True, default_export_compatible=True , translate=True)
class ResCompany(models.Model):
    _inherit = 'res.company'

    # Arabic Company Fields
    name = fields.Char(related='partner_id.name', string='Company Name', required=True, store=True, readonly=False, translate=True)
    street = fields.Char(compute='_compute_address', inverse='_inverse_street', translate=True)
    street2 = fields.Char(compute='_compute_address', inverse='_inverse_street2', translate=True)
    city = fields.Char(compute='_compute_address', inverse='_inverse_city', translate=True)
    state_id = fields.Many2one(
        'res.country.state', compute='_compute_address', inverse='_inverse_state',
        string="Fed. State", domain="[('country_id', '=?', country_id)]"
    )
    country_id = fields.Many2one('res.country', compute='_compute_address', inverse='_inverse_country', string="Country")
