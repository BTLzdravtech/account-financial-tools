from . import models
from . import report
from . import wizard


def post_init_hook(env):
    """Clear stock expense accounts only for accounts used exclusively in Argentina."""
    accounts = env["account.account"].sudo().search([("account_stock_expense_id", "!=", False)])
    accounts.filtered(
        lambda account: account.company_ids and all(company.country_code == "AR" for company in account.company_ids)
    ).write({"account_stock_expense_id": False})
