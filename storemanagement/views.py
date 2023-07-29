
from django.http import HttpResponse,HttpResponseRedirect
from requests import request
from django.shortcuts import render,redirect
from user_info.models import User_infoo
from product.models import Product
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def homepage(request,username):

  data={}
  user= User_infoo.objects.get(username=username)
  if user is not None:
    obj=Product.objects.all()
    if request.method=="POST":
      search=request.POST.get('search') 
      if search!=None:
       obj=Product.objects.filter(product_name=search)
    data={
      'user':user,
      'products':obj
    }
    
    return render(request,"homepage.html",data)
  else:
    return redirect('/')
  
   
   
def profile(request,username):
 
 user= User_infoo.objects.get(username=username)
 print(user.username)

 data={
  'user':user
}
 return render(request,"profile.html",data)

 
  
 
  
  

def userlogin(request):
 data={}
 username=""
 try:
  if request.method=="POST":
    Username=request.POST.get('Username')
    Password=request.POST.get('Password')

    checked=False
    user= User_infoo.objects.get(username=Username)
    if user is not None:
      if user.password==Password:
        username=user.username

        return redirect(f'/homepage/{username}')
    else:
      return redirect('/')
    

    
    
 except:
   pass
  
  
 return render(request,"login.html")

def userlogout(request):
  logout(request)
  
  return redirect('/')


     

def signup_page(request):
  data={}
  email_taken=False
  name_taken=False
  try:
   if request.method=="POST":
    user_name=request.POST.get('username')
    if User_infoo.objects.filter(username=user_name).exists():
       name_taken = True
       
    email=request.POST.get('email')
    if User_infoo.objects.filter(email=email).exists():
       email_taken = True
       data={
         'email_taken':email_taken,
         'name_taken':name_taken
    
       }
      
    password=request.POST.get('password')
    age=request.POST.get('age')
    city=request.POST.get('city')
    gender=request.POST.get('gender')
    image=request.FILES.get('photo')
    obj=User_infoo(username=user_name,email=email,password=password,age=age,city=city,gender=gender,image=image)
    obj.save()
    


    return redirect('/')
    
  except:
   pass
  return render(request,'signup.html',data)
  
  

def save_user_info(request):
 
  if request.method=="POST":
    user_name=request.POST.get('username')
    email=request.POST.get('email')
   
    password=request.POST.get('password')
    age=request.POST.get('age')
    city=request.POST.get('city')
    gender=request.POST.get('gender')
    image=request.FILES['photo']
    obj=User_infoo(username=user_name,email=email,password=password,age=age,city=city,gender=gender,image=image)
    obj.save()


  return render(request,"login.html")



   
      