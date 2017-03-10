frappe.ready(function() {
	frappe.require("assets/js/chosen.jquery.min.js");
	frappe.require("assets/css/chosen.css");
	$("select").chosen({
		placeholder_text_single: " ",
      	no_results_text: " "
	});
})