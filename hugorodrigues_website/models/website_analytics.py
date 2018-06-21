# coding: utf-8
"""Used to set track visitors"""

try:
    from geoip import geolite2
    geolite2.lookup("127.0.0.1")  # Check if lookup is available
except (ImportError, RuntimeError):
    geolite2 = False

try:
    import user_agents
except ImportError:
    user_agents = False

from odoo import models, api, fields


class WebsiteAnalyticsVisitor(models.Model):
    """
    Used to set track visitors.
    """
    _name = "website.analytics.visitor"

    user_id = fields.Many2one(comodel_name="res.users", string="User")
    ip = fields.Char()
    country_id = fields.Many2one(compute="_compute_country",
                                 comodel_name="res.country", string="Country",
                                 store=True)

    @api.depends("ip")
    def _compute_country(self):
        if not geolite2:
            return
        ResCountry = self.env["res.country"].sudo()
        for user in self:
            match = geolite2.lookup(user.ip)
            if match:
                country = ResCountry.search([("code", "=",
                                              match.country)], limit=1)
                if country:
                    user.country_id = country.id
                    continue


class WebsiteAnalyticsVisit(models.Model):
    """
    Used to set track visitors.
    This module will not have views we since will use Grafana to display
    statitics"""
    _name = "website.analytics.visit"

    visitor_id = fields.Many2one(comodel_name="website.analytics.visitor",
                                 required=True, string="Visitor")

    path = fields.Char()
    source = fields.Char()
    user_agent = fields.Char()
    browser_id = fields.Many2one(comodel_name="website.analytics.browser",
                                 compute="_compute_extract_ua",
                                 string="Browser", store=True)
    os_id = fields.Many2one(comodel_name="website.analytics.os",
                            compute="_compute_extract_ua",
                            string="Operating System", store=True)

    @api.depends('user_agent')
    def _compute_extract_ua(self):
        if not user_agents:
            return
        Browser = self.env['website.analytics.browser'].sudo()
        Os = self.env['website.analytics.os'].sudo()
        for visit in self:
            ua = user_agents.parse(visit.user_agent)
            browser = Browser.search([('name', '=', ua.browser.family),
                                      ('version', '=',
                                       ua.browser.version_string)],
                                     limit=1)
            if not browser:
                browser = Browser.create({'name': ua.browser.family,
                                          'version': ua.browser.version_string
                                          })
            os = Os.search([('name', '=', ua.os.family),
                            ('version', '=', ua.os.version_string)],
                           limit=1)
            if not os:
                os = Os.create({'name': ua.os.family,
                                'version': ua.os.version_string
                                })
            visit.browser_id = browser.id
            visit.os_id = os.id


class WebsiteAnalyticsBrowsers(models.Model):
    """
    Used to map browsers
    """
    _name = "website.analytics.browser"

    name = fields.Char(required=True)
    version = fields.Char()


class WebsiteAnalyticsOS(models.Model):
    """
    Used to map operating systems
    """
    _name = "website.analytics.os"

    name = fields.Char(required=True)
    version = fields.Char()
