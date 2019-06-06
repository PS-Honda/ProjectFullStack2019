from django.forms import ModelForm
from .models import Bindding

class BinddingForm(ModelForm)  :
    class Meta :
        model = Bindding 
        fields = '__all__'
        exclude = ['id']


