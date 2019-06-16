from taekonline.models import Student
import django_tables2 as tables
from django.utils.html import format_html

class StudentTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank', 'active'] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value):
        if value.lower() in ("white", "none"):
            return format_html('<span class="badge badge-light">{}</span>', value)
        elif value.lower() in ("yellow"):
            return format_html('<span class="badge badge-warning">{}</span>', value)
        return format_html('<span class="badge badge-dark" style="background-color: {};">{}</span>', value.lower(), value)
        
class BeltExamTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    #action = tables.TemplateColumn('<a class="btn btn-small" onclick="return nextBelt({{record.id}})">Next Belt</a>')
    class Meta:
        model = Student
        fields = ['select', 'id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank',] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value):
        if value.lower() in ("white", "none"):
            return format_html('<span class="badge badge-light">{}</span>', value)
        elif value.lower() in ("yellow"):
            return format_html('<span class="badge badge-warning">{}</span>', value)
        return format_html('<span class="badge badge-dark" style="background-color: {};">{}</span>', value.lower(), value)


class AttendanceTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    #action = tables.TemplateColumn('<a class="btn btn-small" onclick="return nextBelt({{record.id}})">Next Belt</a>')
    class Meta:
        model = Student
        fields = ['select', 'id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank',] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value):
        if value.lower() in ("white", "none"):
            return format_html('<span class="badge badge-light">{}</span>', value)
        elif value.lower() in ("yellow"):
            return format_html('<span class="badge badge-warning">{}</span>', value)
        return format_html('<span class="badge badge-dark" style="background-color: {};">{}</span>', value.lower(), value)