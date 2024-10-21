# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api


class AccountMoveLines(models.Model):
    _inherit = 'account.move.line'
    
    description = fields.Html(string='Description', store=True, readonly=False)

    @api.depends('product_id')
    def _compute_name(self):
        super(AccountMoveLines,self)._compute_name()
        if self.name:
            self.description = self.name
