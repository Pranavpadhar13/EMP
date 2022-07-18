from django.http import HttpRequest
from django.http import HttpResponse
import datetime

from django.shortcuts import render

def Home(request):
    date = datetime.datetime.now()
    isActive = True
    name = "LearnTech"
    list_of_programs = [
        'Wap to check even or odd',
        'Wap to check prime no or not'
    ]
    student = {
        'student_name' : "Rahul",
        'student_college' : "Mj",
        'stud_city' : "Jalgaon"
    }
    data = {
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student': student
    }
    return render(request,"Home.html",data)

def about(request):
    # return HttpResponse("This is abount page")
    return render(request,"about.html")

def services(request):
    return render(request,"Services.html")