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
            "fieldname": "total_responses",
            "label": _("Total Responses"),
            "fieldtype": "Int",
            "width": 150
        },
        {
            "fieldname": "completion_rate",
            "label": _("Completion Rate"),
            "fieldtype": "Percent",
            "width": 150
        },
        {
            "fieldname": "average_time",
            "label": _("Average Time (minutes)"),
            "fieldtype": "Float",
            "width": 150
        }
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    data = frappe.db.sql("""
        SELECT 
            survey,
            COUNT(*) as total_responses,
            AVG(TIMESTAMPDIFF(MINUTE, created_at, modified)) as average_time
        FROM `tabSurvey Response`
        WHERE {conditions}
        GROUP BY survey
    """.format(conditions=conditions), filters, as_dict=1)
    
    return data

def get_conditions(filters):
    conditions = "1=1"
    if filters.get("survey"):
        conditions += " AND survey = %(survey)s"
    if filters.get("from_date"):
        conditions += " AND submission_date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND submission_date <= %(to_date)s"
    return conditions