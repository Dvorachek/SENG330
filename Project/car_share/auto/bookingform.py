from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets

from django.db import models
from django.forms import ModelForm

from .models import Booking, Depot, Vehicle
from .managers import *
from .globals import TAXI_TYPES

import datetime

class CreateBookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ('depot', 'vehicle_type', 'start_date', 'end_time')
		widgets = { 'start_date': forms.DateTimeInput(attrs={'class':'datetime-input'})}

	depot_list = Depot.objects.depots()
	vehicle_list = TAXI_TYPES

	depot = forms.ChoiceField(choices=[(depot.address, depot.address) for depot in depot_list])
	vehicle_type = forms.ChoiceField(choices=[x for x in vehicle_list])
	start_date = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
	end_date = forms.DateTimeField(widget=forms.DateTimeInput)


	# vehicle = Vehicle.objects.vehicles(depot, vehicle_type)
	# v = 0
	# for item in vehicle:
	# 	bookings = Booking.objects.bookings(depot=depot, vehicle=item)
	# 	if not bookings:
	# 		v = item
	# 		break
	# 	for booking in bookings:
	# 		b_start = booking.start_time - datetime.timedelta(days=2)
	# 		b_end = booking.end_time + datetime.timedelta(days=2)
			
	# 		if start_time > b_end or end_time < b_start:
	# 			v = item
	# 			break
# =======

# 	vehicle = Vehicle.objects.vehicles(depot, vehicle_type)
# 	v = 0
# 	for item in vehicle:
# 		bookings = Booking.objects.bookings(depot=depot, vehicle=item)
# 		if not bookings:
# 			v = item
# 			break
# 		for booking in bookings:
# 			b_start = booking.start_time - datetime.timedelta(days=2)
# 			b_end = booking.end_time + datetime.timedelta(days=2)
			
# 			if start_time > b_end or end_time < b_start:
# 				v = item
# 				break
# 		if v:
# 			break

	# if not v:
	# 	print("error, no vehicles of that type available")
	
	
	
	

	
