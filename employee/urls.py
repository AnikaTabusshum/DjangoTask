from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('update/<str:volume>', views.update),  
    path('delete/<str:volume>', views.destroy),  
]