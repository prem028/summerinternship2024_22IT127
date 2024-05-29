from django.shortcuts import render,HttpResponse
from .models import Author
# Create your views here.
def first(request):
    return HttpResponse("This is Love website.")

def second(request):
    return render(request,'first.html')

def table(request):
    authordata = Author.objects.all()
    print(authordata)
    # for i in authordata:
    #         print(i.name)
    #         print(i.email)
    
    return render(request,'table.html',{'author': authordata})