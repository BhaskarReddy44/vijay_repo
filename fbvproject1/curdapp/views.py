from django.shortcuts import render,redirect
from curdapp.models import Employee
from curdapp.forms import EmployeeForm
# Create your views here.
def show_view(request):
    employee=Employee.objects.all()
    return render(request,'curdapp/index.html',{'employee':employee})

def Insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'curdapp/insert.html',{'form':form})

def Delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee= Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'curdapp/update.html',{'employee':employee})
