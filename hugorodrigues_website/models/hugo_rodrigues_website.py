"""Used to set default values on some models"""
import logging

from odoo import models, api


class HugoRodriguesWebsite(models.TransientModel):
    """Used to set default values on some models"""
    _name = 'hugo.rodrigues.website'

    @api.model
    def doconfig(self):
        """Sets default data"""
        logger = logging.getLogger(__name__)
        logger.info('Hides contactus page')
        page = self.env.ref('website.contactus_page')
        page.write({'website_published': False})

        logger.info('Setting website data')
        res_config = self.env['res.config.settings'].create({})
        res_config.write({'website_name': 'Hugo Rodrigues'})
        res_config.execute()
        return True
