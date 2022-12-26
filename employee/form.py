from django import forms  
from .models import Jsontable  
class NewForm(forms.ModelForm):  
    class Meta:  
        model = Jsontable  
        fields = "__all__"  