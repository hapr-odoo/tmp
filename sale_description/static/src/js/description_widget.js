/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

class LinesHtmlDescription extends Component {
    static props = { ...standardFieldProps,
                    // description : String
                };

    setup() {
        super.setup();
        // debugger
        this.actionService = useService("action");
        this.active_id = this.props.record.evalContext.active_id
    }

    onClickAddButton() {
        this.actionService.doAction({
            name: "html desscription",
            type: 'ir.actions.act_window',
            res_model: 'sale.order.line.description',
            views: [[false, 'form']],
            view_mode : "form",
            target:"new",
            context: {
                default_description: this.props.record.data.description,
                form_view_ref : 'sale_description.html_description_wizard_actions',
                active_id : this.active_id
            }
        });
    }
}

LinesHtmlDescription.template = "sale_description.html_description_widget";
registry.category("fields").add("lines_html_description", {
    component: LinesHtmlDescription,
});
