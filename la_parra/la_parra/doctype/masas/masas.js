// Copyright (c) 2016, ADH Ingeniería y Formación and contributors
// For license information, please see license.txt
frappe.ui.form.on('Masas', {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			frm.add_custom_button(__('Ver panes'), function() {
				frappe.route_options = {"masa": frm.doc.name };
				frappe.set_route("List", "Panes");
			})
		}
	}
});
