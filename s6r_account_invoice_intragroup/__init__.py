# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from . import models


def post_init_hook(env):
    """
    Recompute stored intragroup flag for existing account.move records
    """
    Move = env["account.move"].sudo()
    moves = Move.search([("move_type", "!=", "entry")])
    moves._compute_is_intragroup_invoice()
