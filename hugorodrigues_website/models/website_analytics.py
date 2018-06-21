# coding: utf-8
"""Used to set track visitors"""

try:
    from geoip import geolite2
    geolite2.lookup("127.0.0.1")  # Check if lookup is available
except (ImportError, RuntimeError):
    geolite2 = False

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

    browser_ids = fields.Many2many(comodel_name="website.analytics.browser",
                                   string="Browsers")

    @api.depends("ip")
    def _compute_country(self):
        ResCountry = self.env["res.country"].sudo()
        for user in self:
            if geolite2:
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

    analytics_user_id = fields.Many2one(comodel_name="website_analytics.user",
                                        required=True, string="Visitor")

    page = fields.Char()
    source = fields.Char()


class WebsiteAnalyticsBrowsers(models.Model):
    """
    Used to map browsers
    """
    _name = "website.analytics.browser"

    name = fields.Char(required=True)
    version = fields.Char()
    user_agent = fields.Char(required=True)
