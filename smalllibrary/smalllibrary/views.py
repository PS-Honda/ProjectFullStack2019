from django.shortcuts import render, redirect
from .models import Bindding,Book,Borrow,Pubilsher,Transaction,User
from .forms import BinddingForm,PubilsherForm,BookForm,BorrowForm
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict   
# Create your views here.

@csrf_exempt
def lib_admin(request) :
    context = dict()
    if request.method == 'POST' :
        data = QueryDict(request.body)
        typeMethod = data.get('type')
        action = data.get('cmd')
        
        if 'delete' == typeMethod :
            print('delete key ' ,data.get('pk'))
            Bindding.objects.get(pk=data.get('pk')).delete()
        elif 'post'== typeMethod :
            if action == 'binddings' :
                form = BinddingForm(request.POST) 
                form.save()
            elif action == 'pubilsher' :
                form = PubilsherForm(request.POST) 
                form.save()
            elif action == 'book' :
                form = BookForm(request.POST) 
                form.save()
            elif action == 'borrow' : 
                form = BorrowForm(request.POST)  
                form.save()
    else :
        form = BinddingForm()

    context['borrowForm'] = Pubilsher.objects.all()
    context['pubilsher'] = Pubilsher.objects.all()
    context['binddings'] = Bindding.objects.all()
    context['book'] = Bindding.objects.all()
    return render(request,'lib_admin.html',context)