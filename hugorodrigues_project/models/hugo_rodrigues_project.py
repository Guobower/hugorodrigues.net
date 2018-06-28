"""Used to set default values on some models"""
import logging

from odoo import models, api


class HugoRodrigues(models.TransientModel):
    """Used to set default values on some models"""
    _name = "hugo.rodrigues.project"

    @api.model
    def doconfig(self):
        """Sets default data"""
        # pylint: disable=line-too-long
        logger = logging.getLogger(__name__)
        logger.info("Setting project data")
        res_config = self.env["res.config.settings"].create({})
        res_config.write({"group_subtask_project": True})
        res_config.execute()

        return True
