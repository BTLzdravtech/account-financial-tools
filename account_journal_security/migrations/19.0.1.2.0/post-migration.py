from odoo import api

READ_RULE_DOMAINS = {
    "journal_security_rule": "[('id', 'not in', journal_security_hidden_journal_ids)]",
    "journal_security_rule_account_move": "[('journal_id', 'not in', journal_security_hidden_journal_ids)]",
    "journal_security_rule_account_move_line": "[('journal_id', 'not in', journal_security_hidden_journal_ids)]",
    "journal_security_rule_account_payment": "[('journal_id', 'not in', journal_security_hidden_journal_ids)]",
}


def migrate(cr, version):
    env = api.Environment(cr, api.SUPERUSER_ID, {})
    for xmlid, domain in READ_RULE_DOMAINS.items():
        rule = env.ref(f"account_journal_security.{xmlid}", raise_if_not_found=False)
        if rule:
            rule.domain_force = domain
