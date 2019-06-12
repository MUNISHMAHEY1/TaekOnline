from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.db.models import Count, F
from django.utils import timezone
from django.http import JsonResponse
from taekonline.models import Student
from taekonline.tables import StudentTable
from taekonline.forms import StudentForm, StudentContactForm, StudentContactFormSet
from django.forms import formset_factory, inlineformset_factory



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



def student_activate(request, id):
	pass

def student_deactivate(request, id):
	pass

def product(request):
	return render(request, "products/product_list.html")
'''
@login_required
def car_list(request, template_name='cars/car_list.html'):
	car = Car.objects.filter(owner=request.user)
	data = {}
	data['object_list'] = car
	return render(request, template_name, data)

@login_required
def car_view(request, pk, template_name='cars/car_detail.html'):
	car= get_object_or_404(Car, pk=pk)    
	return render(request, template_name, {'object':car})

@login_required
def car_create(request, template_name='cars/car_form.html'):
	if request.POST:
		form = CarForm(request.POST)
		if form.is_valid:
			obj = form.save(commit=False)
			obj.owner = request.user
			obj.save()
	else:
		form = CarForm(initial={'owner': request.user})
	if form.is_valid():
		form.save()
		return redirect('car_list')
	return render(request, template_name, {'form':form})

@login_required
def car_update(request, pk, template_name='cars/car_form.html'):
	car= get_object_or_404(Car, pk=pk)
	form = CarForm(request.POST or None, instance=car)
	if form.is_valid():
		form.save()
		return redirect('car_list')
	return render(request, template_name, {'form':form})

@login_required
def car_delete(request, pk, template_name='cars/car_confirm_delete.html'):
	car= get_object_or_404(Car, pk=pk)    
	if request.method=='POST':
		car.delete()
		return redirect('car_list')
	return render(request, template_name, {'object':car})

@login_required
def passenger_join_ride(request, ride_id):
	ride = Ride.objects.get(id=ride_id)
	if ride.available_seats > 0:
		if ride.passengers.filter(id=request.user.id).count() > 0:
			messages.error(request, 'You are already a passenger of the ride')
			return redirect('join_ride')
		passenger = Passenger()
		passenger.user = request.user
		passenger.ride = ride
		passenger.save()
		#ride.passengers.add(passenger)
		#ride.save()    
	return redirect('my_rides_as_passenger')


@login_required
def rating_list(request, template_name='rating/rating_list.html'):
	drivers_rating = Passenger.objects.filter(user=request.user).filter(driver_rating__isnull=True) 
	passengers_rating = Passenger.objects.filter(ride__driver=request.user).filter(rating__isnull=True)
	data = {}
	data['drivers_rating'] = drivers_rating
	data['passengers_rating'] = passengers_rating
	return render(request, template_name, data)


def rating_driver(request, passenger_id, rating):
	passenger = Passenger.objects.get(id=passenger_id)
	passenger.driver_rating = rating
	passenger.save()
	return JsonResponse({'message':'ok'})
	


def rating_passenger(request, passenger_id, rating):
	passenger = Passenger.objects.get(id=passenger_id)
	passenger.rating = rating
	passenger.save()
	return JsonResponse({'message':'ok'})
'''