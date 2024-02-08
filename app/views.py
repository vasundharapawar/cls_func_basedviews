from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

#Returning string as response by using FBV
def fbv_string(request):
    return HttpResponse('<h1> this is the string from fbv_string')

#Returning string as response by using class based views

class CbvString(View):
    def get(self,request):
        return HttpResponse('string of cbvstring')


# rendering html by fbv

def fbvhtml(request):
    return render(request,'fbvhtml.html')

# rendering html by class based views
class Cbvhtml(View):
    def get(self,request):
        return render(request,'Cbvhtml.html')

# insert data by fbv through model forms

def insert_school_by_fbv(request):
    ESF0=SchoolForm()
    d={'ESFO':ESF0}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if  SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')

    return render(request,'insert_school_by_fbv.html',d)

 #insert data by class based views through model formss

class insert_school_by_cbv(View):
    def get(self,request):
         ESFO=SchoolForm()
         d={'ESFO':ESFO}
         return render(request,'insert_school_by_cbv.html',d)

    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_cbv is done')



class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'






