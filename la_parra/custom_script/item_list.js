/*
frappe.listview_settings['Item']['onload'] =
    function(listview) {
		frappe.route_options = {
			"has_variants": "No"
		};
	}
*/

frappe.listview_settings['Item']['refresh'] =
	function(me) {
		// Filtros
		me.page.add_sidebar_label(__("Filtros:"));

		me.page.add_sidebar_item(__("Ver productos"), function() {
			var publish_filter = me.filter_list.get_filter("item_group");
			publish_filter && publish_filter.remove(true);
			me.filter_list.add_filter(me.doctype, "item_group", '=', "Producto");
			me.run();
		});

		me.page.add_sidebar_item(__("Ver masas"), function() {
			var publish_filter = me.filter_list.get_filter("item_group");
			publish_filter && publish_filter.remove(true);
			me.filter_list.add_filter(me.doctype, "item_group", '=', "Masa");
			me.run();
		});

		me.page.add_sidebar_item(__("Ver materias primas"), function() {
			var publish_filter = me.filter_list.get_filter("item_group");
			publish_filter && publish_filter.remove(true);
			me.filter_list.add_filter(me.doctype, "item_group", '=', "Materia prima");
			me.run();
		});

		me.page.add_sidebar_label(__("----------"));

       	me.page.add_sidebar_item(__("* Limpiar filtros"), function() {
			var publish_filter = me.filter_list.get_filter("item_group");
			publish_filter && publish_filter.remove(true);
			me.filter_list.add_filter(me.doctype, "item_group", '=', "");
			me.run();
		});
	}
