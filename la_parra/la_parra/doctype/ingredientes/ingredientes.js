// Copyright (c) 2016, ADH Ingeniería y Formación - Híspalis Digital and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ingredientes', {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			frm.add_custom_button(__('Ver masas'), function() {
				frappe.route_options = {"ingrediente": frm.doc.name };
				frappe.set_route("List", "Masas");
			})
		}
	}
});
