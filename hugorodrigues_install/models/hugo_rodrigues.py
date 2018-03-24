# coding: utf-8
"""Used to set default values on some models"""
import logging

from odoo import models


class ResConfigSettings(models.AbstractModel):
    """Used to set default values on some models"""
    _name = 'hugo.rodrigues'

    def init(self):
        """Sets default data"""
        logger = logging.getLogger(__name__)
        logger.info('Setting website data')
        res_config = self.env['res.config.settings'].create({})
        res_config.write({'website_name': 'Hugo Rodrigues'})
        res_config.execute()

        company_values = {
            'name': 'Hugo Rodrigues',
            'email': 'public@hugorodrigues.net',
            'website': 'https://hugorodrigues.net',
            'city': 'Lisboa',
            'state_id': self.env.ref('base.state_pt_pt-11').id,
            'country_id': self.env.ref('base.pt').id,
            'tz': 'Europe/Lisbon',
            }

        logger.info('Setting root data')
        root = self.env.ref('base.user_root')
        root.write(company_values)
        root.write({
            'signature': '<p><span data-o-mail-quote="1">-- <br data-o-mail-quote="1">Hugo Rodrigues</span><br data-o-mail-quote="1"><a href="https://github.com/hmrodrigues/" data-o-mail-quote="1"><span class="fa fa-1x fa-github-square text-beta" style="" title="" data-o-mail-quote="1"></span></a><font style="" data-o-mail-quote="1" class=" text-beta">&nbsp;</font><a href="https://twitter.com/hmatosrodrigues" data-o-mail-quote="1"><span class="fa fa-twitter-square fa-1x text-beta" style="" data-o-mail-quote="1"></span></a><font style="" data-o-mail-quote="1" class=" text-beta">&nbsp;</font><a href="https://www.linkedin.com/in/hmatosrodrigues/" data-o-mail-quote="1"><span class="fa fa-linkedin-square fa-1x text-beta" style="" title="" data-o-mail-quote="1"></span><span data-o-mail-quote="1"> </span></a></p>',
            'email': 'me@hugorodrigues.net',
            })

        logger.info('Setting company data')
        company = self.env.ref('base.main_company')
        company.write({
            'report_header': 'Geek since 1995',
            'social_twitter': 'https://twitter.com/hmatosrodrigues',
            'social_github': 'https://github.com/hmrodrigues',
            'social_linkedin': 'https://linkedin.com/in/hmatosrodrigues'
            })
        company.partner_id.write(company_values)

        logger.info('Disable Odoo SA call home')
        try:
            cron = self.env.ref('mail.ir_cron_module_update_notification')
            cron.write({'active': False})
        except:
            logger.warning("Can't find call home cron")
        return True
