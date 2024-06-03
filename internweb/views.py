from django.shortcuts import render,HttpResponse
from .models import Author,category
# Create your views here.
def first(request):
    return HttpResponse("This is Love website.")

def second(request):
    return render(request,'first.html')

def table(request):
    authordata = Author.objects.all()
    #print(authordata)
    # for i in authordata:
    #         print(i.name)
    #         print(i.email)
    
    return render(request,'table.html',{'author': authordata})

def table_cat(request):
    category_data = category.objects.all()
    #print(authordata)
    # for i in authordata:
    #         print(i.name)
    #         print(i.email)
    
    return render(request,'category.html',{'category_c': category_data})

def form(request):
    if request.method =='POST':
        authorform = Author()
        authorform.name = request.POST['uname']
        authorform.email = request.POST['uemail']
        authorform.save()
        return render(request,'form.html')
    else :
        return render(request,'form.html')
        
def catform(request):
    if request.method =='POST':
        catform = category()
        catform.name = request.POST['uname']
        catform.image = request.FILES['ufile']
        catform.save()
        return render(request,'catform.html')
    else :
        return render(request,'catform.html')
def update(request):
    try:
        if request.method=="POST" :
            upauthor= Author.objects.get(name = 'Prem2') 
            upauthor.name = request.POST['name']
            upauthor.email = request.POST['email']
            #print(upauthor)
            upauthor.save()
            return render(request,'update.html',{'author':upauthor})
        else:
            upauthor=Author.objects.get(name = 'Prem2')
            return render(request,'update.html',{'author':upauthor})
        
    except Exception as e:
        return render(request,'update.html')
