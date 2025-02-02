import frappe
from frappe import _
from frappe.utils import now_datetime

@frappe.whitelist()
def submit_response():
    try:
        response_data = frappe.request.get_json()
        
        if not response_data.get('survey'):
            frappe.throw(_('Survey reference is required'))
            
        response = frappe.get_doc({
            'doctype': 'Survey Response',
            'survey': response_data.get('survey'),
            'respondent': frappe.session.user if not response_data.get('is_public') else None,
            'response_data': response_data.get('response_data'),
            'submission_date': now_datetime(),
            'ip_address': frappe.local.request_ip
        })
        
        response.insert()
        return response.as_dict()
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _('Survey Response Submission Failed'))
        frappe.throw(_('Failed to submit survey response'))