# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "la_parra"
app_title = "La Parra"
app_publisher = "ADH Ingeniería y Formación - Híspalis Digital"
app_description = "Informatización de controles de producción"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pedro@hispalisdigital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

fixtures=['Custom Field', 'Property Setter','Print Format','Custom Script','Translation']

# include js, css files in header of desk.html
app_include_css = ["/assets/css/style-desk.css", "/assets/css/material.css"]
# app_include_js = "/assets/la_parra/js/la_parra.js"
app_include_js = [
	"/assets/js/custom.js",
	"/assets/js/templates.min.js"
]

# include js, css files in header of web template
web_include_css = "/assets/css/style-front.css"
# web_include_js = "/assets/la_parra/js/la_parra.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "la_parra.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Web Form Advanced"]

# Installation
# ------------

# before_install = "la_parra.install.before_install"
# after_install = "la_parra.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "la_parra.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"la_parra.tasks.all"
# 	],
# 	"daily": [
# 		"la_parra.tasks.daily"
# 	],
# 	"hourly": [
# 		"la_parra.tasks.hourly"
# 	],
# 	"weekly": [
# 		"la_parra.tasks.weekly"
# 	]
# 	"monthly": [
# 		"la_parra.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "la_parra.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "la_parra.event.get_events"
# }

doctype_list_js = {
	"Item": ["custom_script/item_list.js"]
}