from django.shortcuts import render,redirect
from django.template.context_processors import request
from django.http.response import HttpResponse
from tiger.models import info
# Create your views here.

def head(request):
    s = info.objects.all()
    context =  {'k' : s}
    return render(request,'details.html',context)

def legs(request,**kwargs):
    obj = info.objects.get(id=kwargs['info_id'])
    context =  {'o' : obj}
    return render(request,'info.html',context)