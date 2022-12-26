from django.shortcuts import redirect, render
import json
from django.http import JsonResponse
from .models import Jsontable
from employee.form import NewForm  
# Create your views here.



#def index(request):
    #with open('C:/Users/sabbir/Desktop/django crud/crudexample/static/stock_market_data.json') as json_file:
        #my_data = json.load(json_file)
        #return render(request, 'index.html', {'my_data': my_data})


def index(request):
    my_data = Jsontable.objects.all()
    return render(request, 'index.html', {'my_data': my_data})

def update(request, volume):  
    my_data2 = Jsontable.objects.get(volume=volume)  
    form = NewForm(request.POST, instance = my_data2)  
    if form.is_valid():  
        form.save()  
       
        return render(request, 'edit.html', {'my_data2': my_data2})  
def destroy(request, v):  
    employee = Jsontable.objects.get(volume=v)  
    employee.delete()  
    return redirect("/")      



    