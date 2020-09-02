from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
	return render(request,'realsecurity/home.html')
def Services(request):
	return render(request,'realsecurity/Services.html')
def Contact(request):
	return render(request,'realsecurity/Contact.html')
def pawn_check(request):
	return render(request,'realsecurity/pawn_check.html')
def vulnerability_check(request):
	return render(request,'realsecurity/vulnerability_check.html')

@csrf_exempt
def pawn_user(request):
	username=request.POST["username"]
	if(username==""):
	
		result="Seems like you forgot to enter a username!"
		return render(request,'realsecurity/pawn_check.html',{'result':result})
	
	username+='\n'
	result=""
	with open('/home/priyal/Desktop/word_list.txt','r') as f:
		for line in f:
			if line==username:
				result="Oh no - You have been Pwned!!! :("
				return render(request,'realsecurity/pawn_check.html',{'result':result})
		result="Good news — no pwnage found :)"
		return render(request,'realsecurity/pawn_check.html',{'result':result})

@csrf_exempt
def pawn_pass(request):
	password=request.POST["password"]
	if(password==""):
		result="Seems like you forgot to enter a Password!"
		return render(request,'realsecurity/pawn_check.html',{'result':result})
	password+='\n'
	result=""
	with open('/home/priyal/Desktop/word_list.txt','r') as f:
		for line in f:
			if line==password:
				result="Oh no - Pwned!!!"
				return render(request,'realsecurity/pawn_check.html',{'result':result})
		result="Good news — no pwnage found"
		return render(request,'realsecurity/pawn_check.html',{'result':result})