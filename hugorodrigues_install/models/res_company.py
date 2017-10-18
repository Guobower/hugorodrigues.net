# coding: utf-8
import logging

from odoo import models

_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = 'res.company'

    def init(self):
        _logger.info('Setting company data')
        company = self.env.ref('base.main_company')
        partner = company.partner_id
        company.write({
            'rml_header1': 'Geek since 1995',
            })
        _logger.info('Setting partner data')
        partner.write({
            'name': 'Hugo Rodrigues',
            'email': 'public@hugorodrigues.net',
            'website': 'hugorodrigues.net',
            'city': 'Lisboa',
            'state_id': self.env.ref('base.state_pt_pt-11').id,
            'country_id': self.env.ref('base.pt').id
            })
        return True
