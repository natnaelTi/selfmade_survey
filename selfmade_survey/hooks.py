app_name = "selfmade_survey"
app_title = "Selfmade Survey"
app_publisher = "Selfmade Cloud Solutions"
app_description = "A survey builder and manager application for Frappe instances."
app_email = "natnael.tilaye@earaldtradinget.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "selfmade_cs_customization",
# 		"logo": "/assets/selfmade_cs_customization/logo.png",
# 		"title": "Selfmade CS",
# 		"route": "/selfmade_cs_customization",
# 		"has_permission": "selfmade_cs_customization.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/selfmade_cs_customization/css/selfmade_cs_customization.css"
# app_include_js = "/assets/selfmade_cs_customization/js/selfmade_cs_customization.js"

# include js, css files in header of web template
web_include_css = "/assets/selfmade_survey/css/survey.min.css"
web_include_js = [
    "/assets/selfmade_survey/js/survey.jquery.min.js",
    "/assets/selfmade_survey/js/survey_web_form.js"
]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "selfmade_cs_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "selfmade_cs_customization/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "selfmade_cs_customization.utils.jinja_methods",
# 	"filters": "selfmade_cs_customization.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "selfmade_cs_customization.install.before_install"
# after_install = "selfmade_cs_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "selfmade_cs_customization.uninstall.before_uninstall"
# after_uninstall = "selfmade_cs_customization.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "selfmade_cs_customization.utils.before_app_install"
# after_app_install = "selfmade_cs_customization.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "selfmade_cs_customization.utils.before_app_uninstall"
# after_app_uninstall = "selfmade_cs_customization.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selfmade_cs_customization.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Survey Form": {
#         "after_insert": "selfmade_survey.selfmade_survey.api.survey_form.after_survey_created",
#         "on_trash": "selfmade_survey.selfmade_survey.api.survey_form.before_survey_delete"
#     }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"selfmade_cs_customization.tasks.all"
# 	],
# 	"daily": [
# 		"selfmade_cs_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"selfmade_cs_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"selfmade_cs_customization.tasks.weekly"
# 	],
# 	"monthly": [
# 		"selfmade_cs_customization.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "selfmade_cs_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "selfmade_cs_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "selfmade_cs_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Fixtures
# --------
# Fixtures and customizations

# fixtures = [
#     {
#         "dt": "Web Form",
#         "filters": [["name", "in", ["webinar-feedback"]]],
#     },
#     {
#         "dt": "Survey",
#         "filters": [["name", "in", ["Webinar Feedback"]]],
#     },
# ]

# Request Events
# ----------------
# before_request = ["selfmade_cs_customization.utils.before_request"]
# after_request = ["selfmade_cs_customization.utils.after_request"]

# Job Events
# ----------
# before_job = ["selfmade_cs_customization.utils.before_job"]
# after_job = ["selfmade_cs_customization.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"selfmade_cs_customization.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

