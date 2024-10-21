# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
    
from odoo import models,fields,api, Command

class MailComposeMessage(models.TransientModel):
    _name = 'sale.order.line.description'
    
    description = fields.Html(string='Description',)
        
    def action_ad_description(self):
        sale_order_line_id = self._context.get('active_id')
        if sale_order_line_id:
            sale_order_line = self.env['sale.order.line'].browse(sale_order_line_id)
            sale_order = sale_order_line.order_id
            sale_order.update({'order_line': [Command.update(sale_order_line.id,{'description':self.description})]})
