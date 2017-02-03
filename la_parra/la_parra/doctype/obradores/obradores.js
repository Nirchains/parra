// Copyright (c) 2016, ADH Ingeniería y Formación and contributors
// For license information, please see license.txt

frappe.ui.form.on('Obradores', {
	refresh: function(frm) {
		if(!frm.doc.__islocal) {
			frm.add_custom_button(__('Ver salas de fermentación'), function() {
				frappe.set_route("List", "Salas de Fermentacion",{"obrador": frm.doc.nombre });
			})
		}
	}
});
