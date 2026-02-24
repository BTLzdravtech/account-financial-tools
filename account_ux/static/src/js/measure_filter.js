/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { GraphModel } from "@web/views/graph/graph_model";
import { session } from "@web/session";

const MEASURES_TO_REMOVE = [
    "company_price_average",
    "company_price_margin",
    "company_price_subtotal",
    "company_price_total",
    "current_currency_id",
    "price_subtotal_currency",
    "discount",
    "discount_amount",
    "line_id",
    "price_unit",
    "total_cc"
];

patch(GraphModel.prototype, {
    _buildMetaData(params = {}) {
        const metaData = super._buildMetaData(...arguments);
        // const context = this.searchParams.context;
        // const allowed_company_ids = context.allowed_company_ids;
        // const companies = session.user_companies.allowed_companies;
        // const allCompanyAR = allowed_company_ids.every(
        //     (id) => companies[id]?.country_code === "AR"
        // );
        const model = this.metaData.resModel
        // if (model == 'account.invoice.report' && !allCompanyAR) {
        if (model == 'account.invoice.report') {
            metaData.measures = Object.fromEntries(
                Object.entries(metaData.measures)
                .filter(([key]) => !MEASURES_TO_REMOVE.includes(key))
            );
        }
        return metaData;
    },
});
