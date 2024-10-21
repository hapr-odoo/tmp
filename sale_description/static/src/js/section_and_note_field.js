/** @odoo-module **/

import { SectionAndNoteListRenderer } from "@account/components/section_and_note_fields_backend/section_and_note_fields_backend";
import { patch } from "@web/core/utils/patch";


patch(SectionAndNoteListRenderer.prototype, {
    setup() {
        super.setup();
        const supportedModels = ['sale.order','account.move','sale.order.template'];
        if(supportedModels.includes(this.props.nestedKeyOptionalFieldsData.model)){
            this.titleField = "description";
        }
    }
})
