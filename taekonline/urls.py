"""taekonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from taekonline import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('student', views.student, name='student'),
    path('student/<int:id>/change', views.student_change, name='student_change'),
    path('student/add', views.student_add, name='student_add'),
    path('student/<int:id>/deactivate', views.student_change, name='student_deactivate'),
    path('student/<int:id>/ativate', views.student_change, name='student_activate'),
    path('student/<int:id>/rank_history', views.rank_history, name='rank_history'),
    path('belt_exam', views.belt_exam, name='belt_exam'),
    path('attendance', views.attendance, name='attendance'),
    path('income', views.income, name='income'),
    path('income/add', views.income_add, name='income_add'),
    path('incomeproduct', views.incomeproduct, name='incomeproduct'),

    #path('/studentcontact/<int:id>/delete', views.studentcontact_delete, name='studentcontact_delete'),

    #path('student/add'), views.student_add, name='student_add'),
    path('product', views.product, name='product'),
    path('about_us', views.about_us, name='about_us'),
    path('project', views.project, name='project'),

]
