"""Custom settings for projects and taks"""
from odoo import models, api


class Project(models.Model):
    """Project ext"""
    _inherit = 'project.project'

    @api.model
    def create(self, vals):
        """Auto add stages to project"""
        project = super(Project, self).create(vals)
        stages = self.env['project.task.type'].search([])
        stages.write({'project_ids': [(4, project.id)]})
        return project


class TaskType(models.Model):
    """TaskType (stage) ext"""
    _inherit = 'project.task.type'

    @api.model
    def create(self, vals):
        """Add stage to all projects"""
        stage = super(TaskType, self).create(vals)
        projects = self.env['project.project'].search([])
        stage.write({'project_ids': [(6, 0, projects.ids)]})
        return stage
