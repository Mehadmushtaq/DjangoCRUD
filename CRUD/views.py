from django.shortcuts import render, redirect
from django.http import HttpResponse
from CRUD.models import Employees

# Create your views here.
#R-Read
def index(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp
    }
    return render(request,'Home.html',context)


#C-Create
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


#U-Update
def update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,              #to update specific row -- pass id else new row will be created
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    return render(request,'Home.html')

#D-Delete
def delete(response,id):
    emp = Employees.objects.filter(id=id)
    emp.delete()

    context={                       #context processor add data to the context automatically.
        'emp':emp
    }

    return redirect('home')

