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
def pawn_user(request):
	username=request.POST["username"]
	username+='\n'
	result=""
	with open('/usr/share/wordlists/rockyou.txt','r') as f:
		for line in f:
			if line==username:
				result="Oh no - Pwned!!!"
				return render(request,'realsecurity/result.html',{'result':result})
		result="Good news — no pwnage found"
		return render(request,'realsecurity/result.html',{'result':result})

def pawn_pass(request):
	password=request.POST["password"]
	password+='\n'
	result=""
	with open('/usr/share/wordlists/rockyou.txt','r') as f:
		for line in f:
			if line==password:
				result="Oh no - Pwned!!!"
				return render(request,'realsecurity/result.html',{'result':result})
		result="Good news — no pwnage found"
		return render(request,'realsecurity/result.html',{'result':result})