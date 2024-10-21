# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    #  Information
    'name': "SDATAWAY - Sale Description",
    'version': '17.0.1.0',
    'category': 'Customization',
    'summary': " Change description field in the sales lines in order to have an HTML instead of a text one",
    'description': """
Sale Description| TaskID: 3802473
=================================================
This module modifies the description field in sales lines within Odoo to support HTML formatting instead of plain text. 
It enhances the functionality of sales orders by allowing users to provide more visually appealing and informative descriptions for each sales line item.
""",
    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',

    # Dependency
    'depends': ['sale','sale_management','sale_renting','account','website'],

    'data': [
        'security/ir.model.access.csv',
        
        'reports/account_report.xml',
        'reports/sale_report.xml',
        
        'views/sale_order.xml',
        'views/sale_order_template_views.xml',
        'views/account_move.xml',
        'views/sale_order_line_description_wizard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sale_description/static/src/js/section_and_note_field.js',
            'sale_description/static/src/js/description_widget.js',
            'sale_description/static/src/js/description_widget.xml',
        ],
    },
    # Other
    'installable': True,
}
