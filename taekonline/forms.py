from django import forms
from taekonline.models import Student, StudentContact
from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms_foundation.layout import Layout, Fieldset, SplitDateTimeField, Row, Column, ButtonHolder, Submit, ButtonGroup, Button

class StudentForm(forms.ModelForm):

    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'})
)

    class Meta:
        model = Student
        fields = '__all__'
        #fields = ['pub_date', 'headline', 'content', 'reporter']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-student-form'
        self.helper.form_method = 'post'
        #self.helper['date_of_birth'].widget.attrs.update({'type': 'date'})
        #self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('date_of_birth', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_number', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Fieldset(
                'Address',
                Row(
                    Column('address_number', css_class='form-group col-md-2 mb-0'),
                    Column('address_street', css_class='form-group col-md-10 mb-0'),
                    css_class='form-row'
                ),
            ),
            'address_complement',
            Row(
                Column('address_zip_code', css_class='form-group col-md-4 mb-0'),
                Column('address_city', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            'active',
            ButtonHolder(
                Submit('cancel', 'Cancel', css_class="btn btn-secondary"),
                Submit('save', 'Save', css_class="btn btn-primary"),
            ),
        )
