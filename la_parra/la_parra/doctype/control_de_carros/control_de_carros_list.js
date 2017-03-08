frappe.listview_settings['Control de Carros'] = {
	add_fields: ["Estado"],
	get_indicator: function(doc) {
		return [__(doc.estado   ), {
			"En ejecución": "blue",
			"Finalizado": "green",
			"No válido": "red"
		}[doc.estado], "estado,=," + doc.estado];
	}
};