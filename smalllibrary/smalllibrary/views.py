from django.shortcuts import render, redirect
def test(request):
    return render(request, 'test.html')

from django.shortcuts import render, redirect
from .models import Bindding,Book,Borrow,Pubilsher,Transaction,User
from .forms import BinddingForm 
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict   
# Create your views here.

@csrf_exempt
def lib_admin(request) :
    context = dict()
    if request.method == 'POST' :
        data = QueryDict(request.body)
        typeMethod = data.get('type')
        form = BinddingForm(request.POST) 
        if 'delete' == typeMethod :
            print('delete key ' ,data.get('pk'))
            Bindding.objects.get(pk=data.get('pk')).delete()
        elif 'post'== typeMethod :
            if form.is_valid():
                form.save()
                form = BinddingForm()
    else :
        form = BinddingForm()

    context['pubilsher'] = Pubilsher.objects.all()
    context['binddings'] = Bindding.objects.all()
    context['form']  = form

    return render(request,'lib_admin.html',context)

