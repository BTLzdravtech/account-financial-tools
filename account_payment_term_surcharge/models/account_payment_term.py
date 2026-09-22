from odoo import api, fields, models


class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    surcharge_ids = fields.One2many(
        "account.payment.term.surcharge",
        "payment_term_id",
        string="Surcharges",
        copy=True,
    )

    show_surcharge_warning = fields.Boolean(compute="_compute_surcharge_product")

    @api.depends("company_id", "surcharge_ids")
    def _compute_surcharge_product(self):
        """Check if the surcharge product needs to be updated for the given company context."""
        for rec in self:
            if rec.surcharge_ids:
                if rec.company_id:
                    rec.show_surcharge_warning = rec.company_id.country_code != "AR" or bool(
                        rec.company_id.payment_term_surcharge_product_id
                    )
                else:
                    ar_companies = self.env["res.company"].search([("country_code", "=", "AR")])
                    rec.show_surcharge_warning = all(
                        company.payment_term_surcharge_product_id for company in ar_companies
                    )
            else:
                rec.show_surcharge_warning = True
