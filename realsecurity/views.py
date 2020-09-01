from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'realsecurity/home.html')
def Services(request):
	return render(request,'realsecurity/Services.html')
def Contact(request):
	return render(request,'realsecurity/Contact.html')
def pawn_check(request):
	return render(request,'realsecurity/pawn_check.html')
