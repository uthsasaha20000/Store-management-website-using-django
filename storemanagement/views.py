
from django.http import HttpResponse,HttpResponseRedirect
from requests import request
from django.shortcuts import render,redirect
from user_info.models import User_infoo
from product.models import Product
from cart.models import Cart
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def homepage(request):

  data={}
  #user= User_infoo.objects.get(username=username)
  user1=request.session.get('username')
  user=User_infoo.objects.get(username=user1)
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
  
   
   
def profile(request):
 
 #user= User_infoo.objects.get(username=username)
 user1=request.session.get('username')
 user=User_infoo.objects.get(username=user1)
 #print(user.username)

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
        #username=user.username
        request.session['userid']=user.id
        request.session['username']=user.username
        username=request.session['username']

        return redirect('homepage/')
    else:
      return redirect('/')
    

    
    
 except:
   pass
  
  
 return render(request,"login.html")

def userlogout(request):
   request.session.clear()
  
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


def cart(request,product):
  obj=Product.objects.get(product_name=product)
  print(obj.price)
  data={
    'product':obj
  }
  ob=Cart(p_name=obj.product_name)
  print(obj.product_name)
  ob.save()
  return render(request,"cartpage.html",data)

def navcart(request):
  obj=Cart.objects.all()
  data={
    'product':obj
  }

  
  return render(request,"navcart.html",data)

def deletecart(request):
  Cart.objects.all().delete()

  return render(request,"navcart.html")

  



   
      