from taekonline.models import Student, Income, IncomeProduct
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
    #id = tables.TemplateColumn('<a href="/income/{{record.id}}/change">{{record.id}}</a>')
    
    class Meta:
        model = Income
        fields = ['id', 'income_datetime', 'student', 'products'] # fields to display
        attrs = {'id': 'income_table'}

    '''
    def render_income_time(self, value):
        return value.strftime("%H:%M")

    def render_income_date(self, value):
        return value.strftime("%Y-%m-%d")

    def render_income_datetime(self, value, record):
        return record.income_date.strftime("%Y-%m-%d")
        return ' '.join((record.income_date.strftime("%Y-%m-%d"), record.income_time.strftime("%H:%M")))
    '''

class IncomeProductTable(tables.Table):

    '''
    income = models.ForeignKey(Income, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    profit = models.DecimalField(null=True, blank=True, max_digits=18, decimal_places=2)
    '''
    income_date = tables.Column(accessor='income.income_date', verbose_name='Income date')
    income_datetime = tables.Column(accessor='income.income_datetime', verbose_name='Income date')
    income_student = tables.Column(accessor='income.student.name', verbose_name='Student')


    class Meta:
        model = IncomeProduct
        fields = ['id', 'income_datetime', 'product', 'quantity', 'profit', 'income_student'] # fields to display
        attrs = {'id': 'incomeproduct_table'}

    
    def render_income_date(self, value, record):
        return value.strftime("%Y-%m-%d")
    