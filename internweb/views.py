from django.shortcuts import render,HttpResponse,redirect
from .models import Author,category,product,userregister
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
            upauthor= Author.objects.get(name = 'P') 
            upauthor.name = request.POST['name']
            upauthor.email = request.POST['email']
            #print(upauthor)
            upauthor.save()
            return render(request,'update.html',{'author':upauthor})
        else:
            upauthor=Author.objects.get(name = 'P')
            return render(request,'update.html',{'author':upauthor})
        
    except Exception as e:
        return render(request,'update.html')

def index(request):
    catdata = category.objects.all()
    return render(request,'index.html',{'cat':catdata})

def productshow(request):
    prodata=product.objects.all()
    return render(request,'product.html',{'prod':prodata})

def register(request):
    if request.method == 'POST':
        user=userregister()
        user.name = request.POST['name']
        user.email =request.POST['email']
        user.add = request.POST['add']
        user.password=request.POST['password']
        user.mob =request.POST['mob']
        useralready = userregister.objects.filter(email = request.POST['email'])
        if useralready: # or if len(useralready) > 0 :
            return render(request,'register.html',{'already':"You are already registered by using this email  !!!!!!!!!"})
        else:
            user.save()
            return render(request,'register.html',{'store':"You are registered successfully!!!!!!!!!"})

    else : 
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        useremail= userregister.objects.get(email = request.POST['email'])
        if useremail.password == request.POST['password'] :
            return redirect('index')
        else:
            return render(request,'login.html',{'passmat':"password is incorrect!!!!"})
        return render(request,'login.html')
    else : 
        return render(request,'login.html')