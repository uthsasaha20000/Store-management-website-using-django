from django.contrib import admin
from user_info.models import User_infoo

class Userinfo_admin(admin.ModelAdmin):
       list_display=('username','email','password','age','city','gender','image')



admin.site.register(User_infoo,Userinfo_admin)

