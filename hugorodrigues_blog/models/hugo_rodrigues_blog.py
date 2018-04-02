# coding: utf-8
"""Used to set default values on some models"""
import logging

from odoo import models, api


class HugoRodriguesBlog(models.TransientModel):
    """Used to set default values on some models"""
    _name = 'hugo.rodrigues.blog'

    @api.model
    def doconfig(self):
        """Sets default data"""
        logger = logging.getLogger(__name__)
        logger.info('Setting blog data')
        blog = self.env.ref('website_blog.blog_blog_1')
        blog.write({
            'name': 'A geeks blog',
            'subtitle': False,
            })

        logger.info('Setting config data')
        res_config = self.env['res.config.settings'].create({})
        res_config.write({
            'auth_signup_uninvited': 'b2c',
            'auth_signup_reset_password': True,
            'module_auth_oauth': True})
        res_config.execute()

        logger.info('Disable odoo oauth')
        self.env.ref('auth_oauth.provider_openerp').write({'enabled': False})

        return True
