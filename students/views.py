from django.shortcuts import render, redirect
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@api_view(['GET','POST'])
def std_api(request):
    if request.method=='GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account successfully created')
            return redirect('login')
        else:
            messages.error(request,'Please enter valid information')
            return render(request,'students/register.html',{'form':form})
    else:
        form = RegistrationForm()
        return render(request,'students/register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request,"invalid username or password")
            return render(request, 'students/login.html')
    else:
        return render(request, 'students/login.html') 

def logout_user(request):
    logout(request)
    return redirect('login')

