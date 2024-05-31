from django.urls import path ,include
from .views import first
from .views import second,table,table_cat,form,catform
urlpatterns = [
    path('internweb/',first,name='website'), # we need to write /app1/internweb/ to jump in first function.
      # or path('',first,name='website') directly jump into first function
    path('second/',second,name='second'),
    path('table/',table,name='Table'),
    path('category/',table_cat,name='Category'),
    path('form/',form,name='form'),
    path('catform',catform,name='categoryform')
]