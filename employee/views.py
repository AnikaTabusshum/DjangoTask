from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.



def index(request):
    with open('C:/Users/sabbir/Desktop/django crud/crudexample/static/stock_market_data.json') as json_file:
        my_data = json.load(json_file)
        return render(request, 'index.html', {'my_data': my_data})
    


    