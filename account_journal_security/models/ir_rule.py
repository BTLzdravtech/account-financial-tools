##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import api, models


class IrRule(models.Model):
    _inherit = "ir.rule"

    @api.model
    def _eval_context(self):
        eval_context = super()._eval_context()
        eval_context["journal_security_hidden_journal_ids"] = self.env[
            "account.journal"
        ]._journal_security_hidden_journal_ids()
        return eval_context
