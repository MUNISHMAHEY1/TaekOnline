from taekonline.models import Student, Income,Product
import django_tables2 as tables
from django.utils.html import format_html

class StudentTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank', 'active'] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value, record):
        if value.lower() in ("white", "none"):
            return format_html('<a href="/student/{}/rank_history"><span class="badge badge-light">{}</span></a>', record.id, value)
        elif value.lower() in ("yellow"):
            return format_html('<a href="/student/{}/rank_history"><span class="badge badge-warning">{}</span></a>', record.id, value)
        return format_html('<a href="/student/{}/rank_history"><span class="badge badge-dark" style="background-color: {};">{}</span></a>', record.id, value.lower(), value)
        
class BeltExamTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Student
        fields = ['select', 'id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank'] # fields to display
        attrs = {'id': 'student_table'}


    def render_rank(self, value, record):
        if value.lower() in ("white", "none"):
            return format_html('<a href="/student/{}/rank_history"><span class="badge badge-light">{}</span></a>', record.id, value)
        elif value.lower() in ("yellow"):
            return format_html('<a href="/student/{}/rank_history"><span class="badge badge-warning">{}</span></a>', record.id, value)
        return format_html('<a href="/student/{}/rank_history"><span class="badge badge-dark" style="background-color: {};">{}</span></a>', record.id, value.lower(), value)


class AttendanceTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    #action = tables.TemplateColumn('<a class="btn btn-small" onclick="return nextBelt({{record.id}})">Next Belt</a>')
    class Meta:
        model = Student
        fields = ['select', 'id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank',] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value, record):
        if value.lower() in ("white", "none"):
            return format_html('<a href="/student/{}/rank_history"><span class="badge badge-light">{}</span></a>', record.id, value)
        elif value.lower() in ("yellow"):
            return format_html('<a href="/student/{}/rank_history"><span class="badge badge-warning">{}</span></a>', record.id, value)
        return format_html('<a href="/student/{}/rank_history"><span class="badge badge-dark" style="background-color: {};">{}</span></a>', record.id, value.lower(), value)



class IncomeTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    id = tables.TemplateColumn('<a href="/income/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Income
        fields = ['id', 'date', 'student'] # fields to display
        attrs = {'id': 'income_table'}

class ProductTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    #select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    #id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    #action = tables.TemplateColumn('<a class="btn btn-small" onclick="return nextBelt({{record.id}})">Next Belt</a>')
    class Meta:
        model = Product
        fields = ['id','name','description','cost_price','selling_price','quantity','keep_inventory'] # fields to display
        attrs = {'id': 'products_table'}