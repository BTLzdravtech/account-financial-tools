import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    cr = env.cr

    _logger.info("START add user_id to account_move_line")
    openupgrade.add_columns(env, [
        ("account.move.line", "user_id", "many2one"),
    ])

    openupgrade.logged_query(cr, """
        UPDATE account_move_line aml
           SET user_id = rp.user_id
          FROM res_partner rp
         WHERE aml.partner_id = rp.id
           AND aml.user_id IS NULL
           AND rp.user_id IS NOT NULL
    """)

    _logger.info("END add user_id to account_move_line")