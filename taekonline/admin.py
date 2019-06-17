from django.contrib import admin
from taekonline.models import Student, ContactType, StudentContact, Rank, \
    RankHistory, ClassAgenda, ClassCathegory, Attendance

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

class ClassAgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cathegory', 'start_time', 'end_time','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

class ClassCathegoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'class_date']





admin.site.register(Student, StudentAdmin)
admin.site.register(ContactType, ContactTypeAdmin)
admin.site.register(StudentContact, StudentContactAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(RankHistory, RankHistoryAdmin)
admin.site.register(ClassAgenda, ClassAgendaAdmin)
admin.site.register(ClassCathegory, ClassCathegoryAdmin)
admin.site.register(Attendance, AttendanceAdmin)