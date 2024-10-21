# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api,Command
from odoo.tools.translate import html_translate


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    description = fields.Html(string='Description', store=True, readonly=False, compute="_compute_description", translate=html_translate)

    #  NOT NULL constraint of name field for Section and notes
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('display_type') and not vals.get('is_downpayment'):
                vals['name'] = vals['description']
        return super(SaleOrderLine , self).create(vals_list)

    # compute description for sale order line
    @api.depends('name')
    def _compute_description(self):
        for line in self:
            lang = line.order_id.partner_id.lang 
            line.description = line.with_context(lang=lang).name

    # set description value for invoice generate from sale order
    def _prepare_invoice_line(self, **optional_values):
        result = super(SaleOrderLine,self)._prepare_invoice_line(**optional_values)
        result['description'] = result['name']
        return result

class tmp(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def tmp(self):
        x = self.env['sale.order.line'].browse(1)
        for rec in self.order_line:
            self.update({'order_line': [Command.update(rec.id,{'description':"agsh"})]})
