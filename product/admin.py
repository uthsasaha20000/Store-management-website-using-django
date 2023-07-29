from django.contrib import admin
from product.models import Product

class product_admin(admin.ModelAdmin):
       list_display=('product_name','price','product_image','catagory')



admin.site.register(Product,product_admin)

