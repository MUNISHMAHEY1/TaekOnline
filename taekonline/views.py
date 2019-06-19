from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.db.models import Count, F
from django.utils import timezone
from django.http import JsonResponse
from taekonline.models import Student, RankHistory, Attendance, Income, Product
from taekonline.tables import StudentTable, BeltExamTable, AttendanceTable, IncomeTable, ProductTable
from taekonline.forms import StudentForm, StudentContactForm, StudentContactFormSet,ProductForm
from django.forms import formset_factory, inlineformset_factory
from taekonline.business import StudentBusiness
import datetime



def home(request):
	return render(request, 'home.html')

def profile(request):
	return render(request, 'profile.html')

def student(request, template_name='students/student_list.html'):

	students_table = StudentTable(Student.objects.all())
	return render(request, template_name, {'students_table':students_table })

def student_add(request, template_name='students/student_form.html'):
	if request.POST:
		form = StudentForm(request.POST)
		formset = StudentContactFormSet(request.POST, request.FILES)
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


def income(request, template_name='income/income_list.html'):

	income_table = IncomeTable(Income.objects.all())
	return render(request, template_name, {'income_table':income_table })

def income_add(request, template_name='income/income_form.html'):
	'''
	if request.POST:
		form = StudentForm(request.POST)
		formset = StudentContactFormSet(request.POST, request.FILES)
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
	'''
	return render(request, template_name)
