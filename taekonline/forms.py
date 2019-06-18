from django import forms
from taekonline.models import Student, StudentContact, Income, IncomeProduct, Product
from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, SplitDateTimeField, Row, \
    Column, ButtonHolder, Submit, ButtonGroup, Button
from django.forms.models import inlineformset_factory

class StudentForm(forms.ModelForm):

    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Student
        fields = '__all__'
        #fields = ['pub_date', 'headline', 'content', 'reporter']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        #self.helper.form_id = 'id-student-form'
        self.helper.form_method = 'post'
        #self.helper['date_of_birth'].widget.attrs.update({'type': 'date'})
        #self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Fieldset(
                'Personal Data',
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
                Row(
                    Column('active', css_class='form-group col-md-12 mb-0'),
                    css_class='form-row'
                )
            ),
            Fieldset(
                'Address',
                Row(
                    Column('address_number', css_class='form-group col-md-2 mb-0'),
                    Column('address_street', css_class='form-group col-md-10 mb-0'),
                    css_class='form-row'
                ),
                'address_complement',
                Row(
                    Column('address_zip_code', css_class='form-group col-md-4 mb-0'),
                    Column('address_city', css_class='form-group col-md-8 mb-0'),
                    css_class='form-row'
                ),
            )
            
        )

class StudentContactForm(forms.ModelForm):

    class Meta:
        model = StudentContact
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.render_required_fields = True
        self.helper.render_hidden_fields = True
        self.helper.form_method = 'post'
        self.helper.form_show_errors = True
        self.helper.layout = Layout(
            Row(
                Column('student'),
                Column('contact_type', css_class='form-group col-md-4 mb-0'),
                Column('contact', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('phone_number', css_class='form-group col-md-4 mb-0'),
                Column('email', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            )
        )

    def clean(self):
        cleaned_data = super().clean()
        contact_type = cleaned_data.get("contact_type")
        contact = cleaned_data.get("contact")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        phone_number = cleaned_data.get("phone_number")
        email = cleaned_data.get("email")
        student = cleaned_data.get("student")

        if contact_type:
            if not contact:
                if not first_name:
                    msg = "This field is mandatory if the contact is not a student"
                    self.add_error('first_name', msg)
                if not last_name:
                    msg = "This field is mandatory if the contact is not a student"
                    self.add_error('last_name', msg)
                if not phone_number:
                    msg = "This field is mandatory if the contact is not a student"
                    self.add_error('phone_number', msg)
                if not email:
                    msg = "This field is mandatory if the contact is not a student"
                    self.add_error('email', msg)
        if student:
            if contact:
                if student == contact:
                    msg = "The student contact can not be himself"
                    self.add_error('contact', msg)
            

StudentContactFormSet = inlineformset_factory(
    Student, StudentContact, fk_name='student', form=StudentContactForm,
    extra=2, max_num=2,can_delete=True)




class IncomeForm(forms.ModelForm):

    income_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    income_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))

    class Meta:
        model = Income
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.render_required_fields = True
        self.helper.render_hidden_fields = True
        self.helper.form_method = 'post'
        self.helper.form_show_errors = True
        self.helper.layout = Layout(
            Row(
                Column('student', css_class='form-group'),
                css_class='form-row'
            ),
            Row(
                Column('income_date', css_class='form-group col-md-6'),
                Column('income_time', css_class='form-group col-md-6'),
                css_class='form-row'
            )
        )

class IncomeProductForm(forms.ModelForm):  
    class Meta:  
        model = IncomeProduct  
        exclude = ('profit',)
    
IncomeProductFormSet = inlineformset_factory(
    Income, IncomeProduct, fk_name='income', form=IncomeProductForm,
    extra=1, can_delete=True)
