from django.shortcuts import render, redirect
def test(request):
    return render(request, 'test.html')

from django.shortcuts import render, redirect
from .models import Bindding,Book,Borrow,Pubilsher,Transaction,User
from .forms import BinddingForm 
# Create your views here.

def lib_admin(request) :
    context = dict()
    if request.method == 'POST' :
        form = BinddingForm(request.POST)
        if form.is_valid():
            form.save()
            form = BinddingForm()
    else :
        form = BinddingForm()
        
    context['binddings'] = Bindding.objects.all()
    context['form']  = form

    return render(request,'lib_admin.html',context)

