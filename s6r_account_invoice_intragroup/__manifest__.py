# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "Scalizer Account Invoice Intragroup",
    "version": "19.0.1.0.0",
    "author": "Scalizer",
    "website": "https://github.com/OCA/account-invoicing",
    "category": "Accounting/Accounting",
    "summary": "Detect intragroup invoices based on internal company partners.",
    "description": """
This module detects intragroup invoices by checking whether the document partner is one
of the internal company partners.
    """,
    "depends": [
        "account",
    ],
    "data": [
        "views/account_move_views.xml",

    ],
    "post_init_hook": "post_init_hook",
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
