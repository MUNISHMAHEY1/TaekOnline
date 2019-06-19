<<<<<<< HEAD
from taekonline.models import Student, Income,Product
=======
from taekonline.models import Student, Income, IncomeProduct
>>>>>>> 66d9a42b32e66c20cf5da6883621d0b9ddaedff4
import django_tables2 as tables
from django.utils.html import format_html

def global_render_rank(value, record):
    if value.lower() in ("white", "none"):
        return format_html('<a href="/student/{}/rank_history" target="_blank"><span class="badge badge-light">{}</span></a>', record.id, value)
    elif value.lower() in ("yellow"):
        return format_html('<a href="/student/{}/rank_history" target="_blank"><span class="badge badge-warning">{}</span></a>', record.id, value)
    return format_html('<a href="/student/{}/rank_history" target="_blank"><span class="badge badge-dark" style="background-color: {};">{}</span></a>', record.id, value.lower(), value)


class StudentTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank', 'active'] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value, record):
        return global_render_rank(value, record)
        
class BeltExamTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    class Meta:
        model = Student
        fields = ['select', 'id', 'name', 'date_of_birth', 'phone_number', 'email', 'rank'] # fields to display
        attrs = {'id': 'student_table'}

    def render_rank(self, value, record):
        return global_render_rank(value, record)

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
        return global_render_rank(value, record)

class IncomeTable(tables.Table):
    #id = tables.TemplateColumn('<a href="/income/{{record.id}}/change">{{record.id}}</a>')
    
    class Meta:
        model = Income
        fields = ['id', 'income_datetime', 'student', 'products'] # fields to display
        attrs = {'id': 'income_table'}

<<<<<<< HEAD
class ProductTable(tables.Table):
    #actions = ProductActions(orderable=False) # custom tables.Column()
    #select = tables.TemplateColumn('<input type="checkbox" name="selected_student" value="{{record.id}}" />')
    #id = tables.TemplateColumn('<a href="/student/{{record.id}}/change">{{record.id}}</a>')
    #action = tables.TemplateColumn('<a class="btn btn-small" onclick="return nextBelt({{record.id}})">Next Belt</a>')
    class Meta:
        model = Product
        fields = ['id','name','description','cost_price','selling_price','quantity','keep_inventory'] # fields to display
        attrs = {'id': 'products_table'}
=======
class IncomeProductTable(tables.Table):

    income_datetime = tables.Column(accessor='income.income_datetime', verbose_name='Income date')
    income_student = tables.Column(accessor='income.student.name', verbose_name='Student')

    class Meta:
        model = IncomeProduct
        fields = ['id', 'income_datetime', 'product', 'quantity', 'profit', 'income_student'] # fields to display
        attrs = {'id': 'incomeproduct_table'}
   
    def render_income_date(self, value, record):
        return value.strftime("%Y-%m-%d")
    
>>>>>>> 66d9a42b32e66c20cf5da6883621d0b9ddaedff4
