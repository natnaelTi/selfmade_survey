frappe.provide('selfmade_survey');

selfmade_survey.SurveyDisplay = class SurveyDisplay {
    constructor(wrapper, survey_id) {
        this.wrapper = wrapper;
        this.survey_id = survey_id;
        this.make();
    }

    async make() {
        try {
            const survey_data = await this.fetch_survey();
            this.render_survey(survey_data);
        } catch (e) {
            frappe.throw(__('Failed to load survey'));
        }
    }

    async fetch_survey() {
        const { message } = await frappe.call({
            method: 'selfmade_survey.api.survey_form.get_survey',
            args: { survey_id: this.survey_id }
        });
        return message;
    }

    render_survey(survey_data) {
        const survey = new Survey.Model(JSON.parse(survey_data.survey_json));
        survey.onComplete.add(this.handle_complete.bind(this));
        
        new Survey.SurveyWindow(survey);
    }

    async handle_complete(sender) {
        try {
            await frappe.call({
                method: 'selfmade_survey.api.survey_response.submit_response',
                args: {
                    survey: this.survey_id,
                    response_data: sender.data
                }
            });
            frappe.show_alert({
                message: __('Response submitted successfully'),
                indicator: 'green'
            });
        } catch (e) {
            frappe.throw(__('Failed to submit response'));
        }
    }
}