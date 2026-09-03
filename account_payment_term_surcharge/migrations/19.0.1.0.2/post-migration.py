from openupgradelib import openupgrade

BATCH_SIZE = 1000


@openupgrade.migrate()
def migrate(env, version):
    """Backfill stored surcharge fields without loading all invoices at once."""
    moves_model = env["account.move"].with_context(active_test=False)
    fields_to_recompute = ["next_surcharge_date", "next_surcharge_percent"]
    last_id = 0
    while moves := moves_model.search([("id", ">", last_id)], order="id", limit=BATCH_SIZE):
        last_id = moves[-1].id
        for field_name in fields_to_recompute:
            env.add_to_compute(moves._fields[field_name], moves)
        moves._recompute_recordset(fields_to_recompute)
        env.cr.commit()
