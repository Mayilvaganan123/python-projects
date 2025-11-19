from django.shortcuts import render,redirect
from .forms import QR_form, RegistrationForm
import qrcode
import os
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

def qr_page(request):
    current_site = get_current_site(request)
    host = current_site.domain

    dash_url = f"http://{host}:8000/dashboard"

    return render(request, 'QR.html',{"dash_url":dash_url})



def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'Login.html')  
        else:
            messages.error(request,"invalid details")
            return render(request, 'log.html')
    else:
       return render(request,'log.html')
        
def register_account(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created")
            return redirect('log.html')
        else:
            messages.error(request, 'Please enter valid detail')
            return render(request, 'register.html',{'form':form})
    else:
         form=RegistrationForm()
         return render(request,'register.html',{'form':form})

def QR(request):
    if request.method=='POST':
        form2=QR_form(request.POST)
        if form2.is_valid():
           Res_name=form2.cleaned_data['Rest']
           url=form2.cleaned_data['url'] 
           qr=qrcode.make(url)
           file_name=Res_name.replace(' ','').lower()+'_menu.png'
           file_path=os.path.join(settings.MEDIA_ROOT,file_name)
           qr_url=os.path.join(settings.MEDIA_URL,file_name)
           qr.save(file_path)
           context={'Res_name':Res_name,'qr_url':qr_url}
           return render(request,'QR.html',context)
        else:
            form2=QR_form()
            return render(request,'Login.html',{'form2':form2})
    else:
        form2 = QR_form()
        return render(request,'Login.html',{'form2':form2})
    
