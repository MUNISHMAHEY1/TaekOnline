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
	IncomeProductTable, ProductTable
from taekonline.forms import StudentForm, StudentContactForm, StudentContactFormSet, \
	IncomeForm, IncomeProductFormSet, ProductForm
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

	att_count = attendance.count()
	rh_count = len(rank_history)

	'''
	if rank_history_count == 0 or attendance_count == 0:
		return render(request, template_name, {'student': student, 'rank_history': rank_history})	
	'''

	for rh in rank_history:
		rh['attendances'] = []

	att_index = 0
	rh_index = 0
	while att_index < (att_count - 1):
		att = attendance[att_index]
		rh = rank_history[rh_index]
		if rh_index == rh_count - 1:
			rh['attendances'].append({ 'class_date': att['class_date'], 'id':att['id'] })
			att_index = att_index + 1
		elif att['class_date'] >= rh['exam_date'] and att['class_date'] < rank_history[rh_index+1]['exam_date']:
			rh['attendances'].append({ 'class_date': att['class_date'], 'id':att['id'] })
			att_index = att_index + 1
		elif att['class_date'] < rh['exam_date'] and rh_index == 0:
			rh['attendances'].append({ 'class_date': att['class_date'], 'id':att['id'] })
			att_index = att_index + 1
		else:
			rh_index = rh_index + 1
		
	
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

@transaction.atomic
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
			attendance = Attendance()
			attendance.student=student
			attendance.class_date=class_datetime
			attendance.save()

		msg = 'Atterndance for {dt} registred sucessfully.'.format(dt=datetime_str)
		messages.success(request, msg)

	return render(request, template_name, {'students_table':students_table })

def attendance_delete(request, id, template_name='students/student_rank_history.html'):
	attendance = Attendance.objects.get(id=int(id))
	student_id = attendance.student.id
	attendance.delete()
	return redirect('rank_history', id=student_id)


def product(request,template_name='products/product_list.html'):
	products_table = ProductTable(Product.objects.all())
	return render(request, template_name, {'products_table':products_table })
	#return render(request, "products/product_list.html")

def product_add(request, template_name='products/product_form.html'):
	if request.POST:
		form = ProductForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('product')
		else:
			return render(request, template_name, {'form':form})
	else:
		form = ProductForm()
	return render(request, template_name, {'form':form})

def product_delete(request, id):
	Product.objects.get(id=int(id)).delete()
	
	return redirect('product')

#@transaction.atomic
def product_change(request, id, template_name='products/product_form.html'):
	product = Product.objects.get(id=int(id))
	if request.POST:
		form = ProductForm(request.POST, instance=product)
		#formset = ProductForm(request.POST, request.FILES, instance=product)

		#if form.is_valid() and formset.is_valid():
		if form.is_valid():
			form.save()
			#formset.save()
			return redirect('product')
		else:
			#return render(request, template_name, {'form':form, 'formset':formset})
			return render(request, template_name, {'form':form})
	else:
		form = ProductForm(instance=product)
		#formset = ProductForm(instance=product)
	#return render(request, template_name, {'form':form, 'formset':formset})
	return render(request, template_name, {'form':form})

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

	RequestConfig(request).configure(table)
	return render(request, template_name, {'table':table, 'filter':f })

