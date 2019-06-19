from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.db.models import Count, F
from django.utils import timezone
from django.http import JsonResponse
from taekonline.models import Student, RankHistory, Attendance, Income, Product, IncomeProduct
from taekonline.tables import StudentTable, BeltExamTable, AttendanceTable, IncomeTable, \
	IncomeProductTable
from taekonline.forms import StudentForm, StudentContactForm, StudentContactFormSet, \
	IncomeForm, IncomeProductFormSet
from django.forms import formset_factory, inlineformset_factory
from taekonline.business import StudentBusiness
import datetime
from django.db import transaction
from django_tables2 import RequestConfig
from taekonline.filters import IncomeProductFilter



def home(request):
	return render(request, 'home.html')

def profile(request):
	return render(request, 'profile.html')

def student(request, template_name='students/student_list.html'):

	students_table = StudentTable(Student.objects.all())
	return render(request, template_name, {'students_table':students_table })

@transaction.atomic
def student_add(request, template_name='students/student_form.html'):
	if request.POST:
		form = StudentForm(request.POST)
		formset = StudentContactFormSet(request.POST, request.FILES, instance=form.instance)
		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
			return redirect('student')
		else:
			return render(request, template_name, {'form':form, 'formset':formset})
	else:
		form = StudentForm()
		formset = StudentContactFormSet()
	return render(request, template_name, {'form':form, 'formset':formset})

@transaction.atomic
def student_change(request, id, template_name='students/student_form.html'):
	student = Student.objects.get(id=int(id))
	if request.POST:
		form = StudentForm(request.POST, instance=student)
		formset = StudentContactFormSet(request.POST, request.FILES, instance=student)

		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
			return redirect('student')
		else:
			return render(request, template_name, {'form':form, 'formset':formset})
	else:
		form = StudentForm(instance=student)
		formset = StudentContactFormSet(instance=student)
	return render(request, template_name, {'form':form, 'formset':formset})

def rank_history(request, id, template_name='students/student_rank_history.html'):
	student = Student.objects.get(id=int(id))
	rank_history = list(RankHistory.objects.filter(student__id=int(id)).values('rank__description', 'exam_date').order_by('exam_date'))
	attendance = Attendance.objects.filter(student__id=int(id)).order_by('class_date').values()

	for rh in rank_history:
		rh['attendances'] = []
	for att in attendance:
		for rh in rank_history:
			if att['class_date'] < rh['exam_date']:
				rh['attendances'].append(att['class_date'])
				break

	return render(request, template_name, {'student': student, 'rank_history': rank_history})

def student_activate(request, id):
	pass

def student_deactivate(request, id):
	pass

def belt_exam(request, template_name='students/belt_exam.html'):
	students_table = BeltExamTable(Student.objects.filter(active=True))
	if request.POST:
		exam_date = request.POST.get('exam_date')
		exam_time = request.POST.get('exam_time')
		datetime_str = exam_date + ' ' + exam_time
		exam_datetime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

		# Get the list and transform in a list of integers
		selected_student = list(map(int, request.POST.getlist('selected_student')))
		sb = StudentBusiness()
		for sid in selected_student:
			sb.increase_rank(request=request, student_id=sid, exam_date=exam_datetime)

	return render(request, template_name, {'students_table':students_table })


def attendance(request, template_name='students/attendance.html'):
	students_table = AttendanceTable(Student.objects.filter(active=True))
	if request.POST:
		class_date = request.POST.get('class_date')
		class_time = request.POST.get('class_time')
		datetime_str = class_date + ' ' + class_time
		class_datetime = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

		# Get the list and transform in a list of integers
		selected_student = list(map(int, request.POST.getlist('selected_student')))
		students = Student.objects.filter(id__in=selected_student)
		for student in students:
			attendance = Attendance(student=student, class_date=class_datetime)
			attendance.save()

		msg = 'Atterndance for {dt} registred sucessfully.'.format(dt=datetime_str)
		messages.success(request, msg)

	return render(request, template_name, {'students_table':students_table })



def product(request):
	return render(request, "products/product_list.html")

def about_us(request):
	return render(request, "about_us.html")

def project(request):
	return render(request, "project.html")	

def income(request, template_name='income/income_list.html'):

	income_table = IncomeTable(Income.objects.all())
	return render(request, template_name, {'income_table':income_table })

@transaction.atomic
def income_add(request, template_name='income/income_form.html'):
	if request.POST:
		form = IncomeForm(request.POST)
		formset = IncomeProductFormSet(request.POST, request.FILES, instance=form.instance, prefix='products')
		if formset.is_valid():
			for f in formset:
					cd = f.cleaned_data
					f_product = cd.get('product')
					f_quantity = cd.get('quantity')
					if f_product.keep_inventory:
						if f_product.quantity > int(f_quantity):
							f_product.quantity = f_product.quantity - int(f_quantity)
							f_product.save()
						else:
							f.add_error('quantity', 'Quantity is greater than the quantity in inventory')
		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()
			return redirect('income')
		else:
			return render(request, template_name, {'form':form, 'formset':formset})
	else:
		form = IncomeForm()
		#formset = IncomeProductFormSet()
		formset = IncomeProductFormSet(prefix='products')
	return render(request, template_name, {'form':form, 'formset':formset})


def incomeproduct(request, template_name='incomeproduct/incomeproduct_list.html'):

	queryset = IncomeProduct.objects.all()
	f = IncomeProductFilter(request.GET, queryset=queryset)
	table = IncomeProductTable(f.qs)
	dtable = f.qs.all()

	RequestConfig(request).configure(table)
	return render(request, template_name, {'table':table, 'filter':f, 'dtable':dtable })
	#incomeproduct_table = IncomeProductTable(Income.objects.all())
	#return render(request, template_name, {'incomeproduct_table':incomeproduct_table })



'''

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
import requests
from django.contrib import messages
import datetime
from estatistica_pje import settings
from .forms import FiltroProcessoForm
from estatistica_pje.tables import ProcessoTable
from django_tables2 import RequestConfig
from .models import VwProcessoAcervo as Processo, TbOrgaoJulgador as Relator
from .filters import ProcessoFilter

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
 

def home(request):
    
    return render(request, 'home.html') 

def processo_list(request):
    
    form = FiltroProcessoForm()
    queryset = Processo.objects.all().using('pje')
    f = ProcessoFilter(request.GET, queryset=queryset)
    table = ProcessoTable(f.qs)
    dtable = f.qs.all()
    
    RequestConfig(request).configure(table)
    return render(request, 'processos.html', {'form': form, 'table':table, 'filter':f, 'dtable':dtable })

'''