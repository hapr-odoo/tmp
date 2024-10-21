# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
    
from odoo import models,fields,api


class SaleOrderTemplateLine(models.Model):
    _inherit = 'sale.order.template.line'

    description = fields.Html(string='Description',compute="_compute_description",default='',translate=True,required=True,store=True,copy=True,readonly=False)

    # not null constraint of name field for section and notes
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('display_type'):
                vals['name'] = vals['description']
        return super(SaleOrderTemplateLine , self).create(vals_list)

    @api.depends('product_id')
    def _compute_name(self):
        super(SaleOrderTemplateLine,self)._compute_name()
        if self.description:
            self.name = self.description

    # compute description from product's description
    @api.depends('product_id')
    def _compute_description(self):
        for line in self:
            if line.product_id.description_sale:
                line.description = line.product_id.description_sale
            else:
                line.description = line.product_id.name
