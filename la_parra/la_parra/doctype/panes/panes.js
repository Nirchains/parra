// Copyright (c) 2016, ADH Ingeniería y Formación and contributors
// For license information, please see license.txt

frappe.ui.form.on('Panes', {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			frm.add_custom_button(__('Ver masa'), function() {
				frappe.set_route("Form", "Masas", frm.doc.masa);
			})
		}
	}
});
