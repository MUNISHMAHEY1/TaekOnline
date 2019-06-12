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
    #path('student/add'), views.student_add, name='student_add'),
    path('product', views.product, name='product'),
]
