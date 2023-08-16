"""storemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from storemanagement import views
from django.conf import settings 
from django.conf.urls.static import static
from user_info.models import User_infoo

admin.site.site_header = "Admin's Section"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Here owner can manage products and track orders and users."

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.userlogin),
    path('user_signin_form/',views.signup_page),
    path('saveuserform/',views.save_user_info,name="saveuserform"),   
    path('homepage/',views.homepage,name="homepage"),
    path('profile/',views.profile,name="profile"),
    path('cart/<str:product>',views.cart,name="cart"),
    path('navcart/',views.navcart),
    path('deletecart/',views.deletecart),
    path('logout/',views.userlogout,name="logout")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
