from taekonline.models import Student
import django_tables2 as tables

class StudentTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'phone_number', 'email', 'active'] # fields to display
        attrs = {'id': 'student_table'}