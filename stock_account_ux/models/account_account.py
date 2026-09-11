from odoo import api, models


class AccountAccount(models.Model):
    _inherit = "account.account"

    @api.model_create_multi
    def create(self, vals_list):
        accounts = super().create(vals_list)
        accounts.filtered(
            lambda account: account.company_ids and all(company.country_code == "AR" for company in account.company_ids)
        ).write({"account_stock_expense_id": False})
        return accounts

    def write(self, vals):
        if "account_stock_expense_id" not in vals:
            return super().write(vals)
        argentine_accounts = self.filtered(
            lambda account: account.company_ids and all(company.country_code == "AR" for company in account.company_ids)
        )
        result = super(AccountAccount, self - argentine_accounts).write(vals)
        if argentine_accounts:
            result = super(AccountAccount, argentine_accounts).write(dict(vals, account_stock_expense_id=False))
        return result
