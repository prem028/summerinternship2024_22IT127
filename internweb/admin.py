from django.contrib import admin
from .models import Blog, Author,userregister,img,category,product

admin.site.register(Blog)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name','email']
    search_fields = ['name','email']

admin.site.register(Author, AuthorAdmin)

class user_(admin.ModelAdmin) :
    list_display = ['name','email','add','password']

admin.site.register(userregister,user_)

class img1_(admin.ModelAdmin):
    list_display=['img']

admin.site.register(img,img1_)


class cat_(admin.ModelAdmin):
    list_display=['name','image']

admin.site.register(category,cat_)

class proj(admin.ModelAdmin):
    list_display=['id','name','description','image','category','qty','price']

admin.site.register(product,proj)