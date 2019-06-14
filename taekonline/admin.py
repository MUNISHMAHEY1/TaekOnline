from django.contrib import admin
from taekonline.models import Student, ContactType, StudentContact, Rank, RankHistory

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'active']
 

class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ['description']

class RankAdmin(admin.ModelAdmin):
    list_display = ['description']

class RankHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'rank', 'exam_date']

class StudentContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'contact', 'first_name', 'last_name', 'phone_number']


admin.site.register(Student, StudentAdmin)
admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(StudentContact, StudentContactAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(RankHistory, RankHistoryAdmin)
