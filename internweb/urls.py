from django.urls import path ,include
from .views import first
from .views import *
urlpatterns = [
    path('internweb/',first,name='website'), # we need to write /app1/internweb/ to jump in first function.
      # or path('',first,name='website') directly jump into first function
    path('second/',second,name='second'),
    path('table/',table,name='Table'),
    path('category/',table_cat,name='Category'),
    path('form/',form,name='form'),
    path('catform',catform,name='categoryform'),
    path('update/',update,name='update'),
    path('index/',index,name='index'),
    path('product/',productshow,name='Productdetails'),
    path('reg/',register,name='Registerform'),
    path('login/',login,name='Login')
]
