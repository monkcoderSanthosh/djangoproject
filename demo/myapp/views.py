from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Stud_record
from django.contrib import messages

def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def userpage(request):
    return render(request,'user.html')
def register_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        gmail = request.POST['gmail']
        user_username = request.POST['user_username']
        phone = request.POST['phone']
        save_record=Stud_record(username=username,password=password,phone=phone,gmail=gmail,user_username=user_username)
        save_record.save()
        return render(request,'create.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        filter_data = Stud_record.objects.filter(username=username,password=password)
        if filter_data.exists():
            save_record = Stud_record.objects.get(username=username)
            if username == save_record.username:
                return redirect('userpage')            
            else:
                messages.error(request, 'Invalid Username')
                return redirect('home')            
        else: 
            messages.error(request, 'Invalid Username')
            return redirect('home') 
                   
    return redirect('home') 
                
