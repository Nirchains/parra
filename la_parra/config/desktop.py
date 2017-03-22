# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "La Parra",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("La Parra")
		},
		{
			"module_name": "Design",
			"color": "blue",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Diseño")
		}
	]
