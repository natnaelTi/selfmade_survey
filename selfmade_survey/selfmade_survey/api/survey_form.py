import frappe
from frappe import _
from frappe.utils import now_datetime

@frappe.whitelist()
def create_survey():
    try:
        survey_data = frappe.request.get_json()
        
        if not survey_data.get('title'):
            frappe.throw(_('Survey title is required'))
            
        survey = frappe.get_doc({
            'doctype': 'Survey Form',
            'title': survey_data.get('title'),
            'description': survey_data.get('description'),
            'status': 'Draft',
            'survey_json': survey_data.get('survey_json'),
            'is_public': survey_data.get('is_public', 0)
        })
        
        survey.insert()
        return survey.as_dict()
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _('Survey Creation Failed'))
        frappe.throw(_('Failed to create survey'))

@frappe.whitelist()
def get_survey(survey_id):
    try:
        survey = frappe.get_doc('Survey Form', survey_id)
        return survey.as_dict()
    except frappe.DoesNotExistError:
        frappe.throw(_('Survey not found'))
    except Exception as e:
        frappe.throw(_('Failed to fetch survey'))