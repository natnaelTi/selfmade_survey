frappe.provide('selfmade_survey');

selfmade_survey.SurveyBuilder = class SurveyBuilder {
    constructor(wrapper) {
        this.wrapper = wrapper;
        this.make();
    }

    make() {
        this.survey = new Survey.Model(this.get_default_config());
        this.survey_creator = new SurveyCreator.SurveyCreator(this.wrapper, {
            showLogicTab: true,
            isAutoSave: true,
            showTranslationTab: true,
        });
        
        this.setup_events();
    }

    setup_events() {
        this.survey_creator.saveSurveyFunc = (saveNo, callback) => {
            this.save_survey()
                .then(() => callback(saveNo, true))
                .catch(() => callback(saveNo, false));
        };
    }

    get_default_config() {
        return {
            pages: [{
                name: 'page1',
                elements: []
            }],
            showProgressBar: 'bottom',
            showQuestionNumbers: 'on'
        };
    }

    async save_survey() {
        try {
            const survey_json = this.survey_creator.text;
            await frappe.call({
                method: 'selfmade_survey.api.survey_form.create_survey',
                args: {
                    title: this.survey_creator.survey.title,
                    survey_json: survey_json
                }
            });
            frappe.show_alert({
                message: __('Survey saved successfully'),
                indicator: 'green'
            });
        } catch (e) {
            frappe.throw(__('Failed to save survey'));
        }
    }
}