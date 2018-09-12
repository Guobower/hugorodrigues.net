"""Used to set default values on some models"""
import logging

from odoo import models, api, fields


class ResCompany(models.Model):
    """Used to set default values on some models"""
    _inherit = 'res.company'

    social_gitlab = fields.Char(string="GitLab Account")

    social_mastodon = fields.Char(string="Mastodon Account")
