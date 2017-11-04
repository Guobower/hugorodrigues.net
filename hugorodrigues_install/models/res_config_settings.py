# coding: utf-8
"""res.config.settings related code"""
import logging

from odoo import models


class ResConfigSettings(models.TransientModel):
    """Extendes res.config.settings"""
    _inherit = 'res.config.settings'

    def init(self):
        """Sets default company data"""
        logger = logging.getLogger(__name__)
        logger.info('Setting website data')
        new = self.create({})
        new.write({'website_name': 'Hugo Rodrigues'})
        new.execute()
        return True
