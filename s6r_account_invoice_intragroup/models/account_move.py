# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    is_intragroup_invoice = fields.Boolean(
        string="Intragroup Invoice",
        compute="_compute_is_intragroup_invoice",
        store=True,
        readonly=True,
        help="Checked when the document commercial partner matches "
        "an internal company commercial partner.",
    )

    @api.depends("partner_id", "partner_id.commercial_partner_id")
    def _compute_is_intragroup_invoice(self):
        """
        Mark the document as intragroup when its commercial partner matches
        the commercial partner of one of the internal companies.
        """
        companies = self.env["res.company"].sudo().search([("partner_id", "!=", False)])
        company_commercial_partner_ids = set(
            companies.mapped("partner_id.commercial_partner_id").ids
        )
        for move in self:
            if move.move_type == "entry":
                continue
            commercial_partner = move.partner_id.commercial_partner_id
            move.is_intragroup_invoice = bool(
                commercial_partner
                and commercial_partner.id in company_commercial_partner_ids
            )
