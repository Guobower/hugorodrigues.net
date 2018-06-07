# coding: utf-8
"""Used to set track visitors"""
import logging

from odoo import models, api, fields


class WebsiteAnalytics(models.Model):
    """
    Used to set track visitors.
    This module will not have views we since will use Grafana to display
    statitics"""
    _name = 'website.analytics'

    url = fields.Char()
    page_title = fields.Char()
    source_ip = fields.Char()
    source_page = fields.Char()
