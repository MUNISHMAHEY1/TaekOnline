import django_filters
from taekonline.models import IncomeProduct, Student, Product

class IncomeProductFilter(django_filters.FilterSet):
    income__income_date = django_filters.DateFromToRangeFilter(label='Period', widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'YYYY-MM-DD', 'type':'date'}))
    income__student = django_filters.ModelChoiceFilter(queryset=Student.objects.all())
    product = django_filters.ModelChoiceFilter(queryset=Product.objects.all())
    class Meta:
        model = IncomeProduct
        fields = {}
