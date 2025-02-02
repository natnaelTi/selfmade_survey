from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "survey",
            "label": _("Survey"),
            "fieldtype": "Link",
            "options": "Survey Form",
            "width": 200
        },
        {
            "fieldname": "started",
            "label": _("Started"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "completed",
            "label": _("Completed"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "completion_rate",
            "label": _("Completion Rate"),
            "fieldtype": "Percent",
            "width": 150
        },
        {
            "fieldname": "average_completion_time",
            "label": _("Avg. Completion Time (min)"),
            "fieldtype": "Float",
            "width": 180
        }
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.sql("""
        SELECT 
            sr.survey,
            COUNT(DISTINCT sr.name) as started,
            COUNT(DISTINCT CASE WHEN sr.status = 'Completed' THEN sr.name END) as completed,
            (COUNT(DISTINCT CASE WHEN sr.status = 'Completed' THEN sr.name END) * 100.0 / COUNT(DISTINCT sr.name)) as completion_rate,
            AVG(CASE WHEN sr.status = 'Completed' 
                THEN TIMESTAMPDIFF(MINUTE, sr.creation, sr.modified)
                END) as average_completion_time
        FROM `tabSurvey Response` sr
        WHERE {conditions}
        GROUP BY sr.survey
    """.format(conditions=conditions), filters, as_dict=1)
    
    return data

def get_conditions(filters):
    conditions = "1=1"
    if filters.get("survey"):
        conditions += " AND sr.survey = %(survey)s"
    if filters.get("from_date"):
        conditions += " AND sr.creation >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND sr.creation <= %(to_date)s"
    return conditions