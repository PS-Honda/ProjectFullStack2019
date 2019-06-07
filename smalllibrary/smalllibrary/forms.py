from django.forms import ModelForm
from .models import Bindding,Book,Borrow,Pubilsher

class BinddingForm(ModelForm)  :
    class Meta :
        model = Bindding 
        fields = '__all__'
        exclude = ['id']
class BookForm(ModelForm)  :
    class Meta :
        model = Book 
        fields = '__all__'
        exclude = ['id']
class BorrowForm(ModelForm)  :
    class Meta :
        model = Borrow 
        fields = '__all__'
        exclude = ['id']
class PubilsherForm(ModelForm)  :
    class Meta :
        model = Pubilsher 
        fields = '__all__'
        exclude = ['id']


