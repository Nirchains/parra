from __future__ import unicode_literals
import frappe
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
	doc = frappe.get_doc("Contact Us Settings", "Contact Us Settings")
	context.base_template_path = "templates/base-extend.html"

	
	if doc.query_options:
		query_options = [opt.strip() for opt in doc.query_options.replace(",", "\n").split("\n") if opt]
	else:
		query_options = ["Sales", "Support", "General"]

	address = None
	if doc.get("address"):
		address = frappe.get_doc("Address", doc.address)

	out = {
		"query_options": query_options
	}
	out.update(doc.as_dict())

	return out