from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
from . import achilles
#from PredictFromModel import prediction
import joblib
import json
# Create your views here.


def home(request):
    return render(request, 'realsecurity/home.html')


def contact(request):
    if(request.method == 'POST'):
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        comment = request.POST.get("comment", "")
        feedback = Feedback(name=name, email=email,
                            phone=phone, comment=comment)
        feedback.save()

    return render(request, 'realsecurity/home.html')


def Services(request):
    return render(request, 'realsecurity/Services.html')


def pawn_check(request):
    return render(request, 'realsecurity/pawn_check.html')


@csrf_exempt
def pawn_user(request):
    username = request.POST["username"]
    if(username == ""):

        result = "Seems like you forgot to enter a username!"
        return render(request, 'realsecurity/pawn_check.html', {'result': result})

    username += '\n'
    result = ""
    with open('word_list.txt', 'r') as f:
        for line in f:
            if line == username:
                result = "Oh no - You have been Pwned!!! :("
                return render(request, 'realsecurity/pawn_check.html', {'result': result})
        result = "Good news — no pwnage found :)"
        return render(request, 'realsecurity/pawn_check.html', {'result': result})


@csrf_exempt
def pawn_pass(request):
    password = request.POST["password"]
    if(password == ""):
        result = "Seems like you forgot to enter a Password!"
        return render(request, 'realsecurity/pawn_check.html', {'result': result})
    password += '\n'
    result = ""
    with open('/home/priyal/Desktop/word_list.txt', 'r') as f:
        for line in f:
            if line == password:
                result = "Oh no - Pwned!!!"
                return render(request, 'realsecurity/pawn_check.html', {'result': result})
        result = "Good news — no pwnage found"
        return render(request, 'realsecurity/pawn_check.html', {'result': result})


def vulnerability_check(request):
    return render(request, 'realsecurity/vulnerability_check.html')


def vuln(request):
    url = request.POST["url"]
    if(url == ""):
        vulnerabilities = "Seems like you forgot to enter a URL"
        description = ""
    else:
        vulnerabilities, description = achilles.basics(url)
    if description == "":
        return render(request, 'realsecurity/result.html', {'vulnerabilities': vulnerabilities})
    else:
        vulnerable = vulnerabilities.split("\n")
        des = description.split("\n")
        vulnerable.pop()
        des.pop()
        zipped_list = zip(vulnerable, des)
        return render(request, 'realsecurity/result.html', {'vulnerable': zipped_list})
