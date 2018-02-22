# coding: utf-8
"""Used to set default values on some models"""
import logging

from odoo import models


class HugoRodriguesWebsite(models.AbstractModel):
    """Used to set default values on some models"""
    _name = 'hugo.rodrigues.website'

    def init(self):
        """Sets default data"""
        logger = logging.getLogger(__name__)
        logger.info('Hides contactus page')
        page = self.env.ref('website.contactus_page')
        page.write({'website_published': False})
        return True
