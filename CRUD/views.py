from django.shortcuts import render, redirect
from django.http import HttpResponse
from CRUD.models import Employees

# Create your views here.
def index(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp
    }

    return render(request,'Home.html',context)


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    return render(request,'Home.html')