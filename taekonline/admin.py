from django.contrib import admin
from taekonline.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'active')
 

admin.site.register(Student, StudentAdmin)
