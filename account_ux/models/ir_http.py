from odoo import fields, models


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(IrHttp, self).session_info()
        if "user_companies" in res and "allowed_companies" in res["user_companies"]:
            RC = self.env["res.company"]
            for key in res["user_companies"]["allowed_companies"].keys():
                country_code = RC.browse(key).country_code
                res["user_companies"]["allowed_companies"][key]["country_code"] = country_code
        return res
