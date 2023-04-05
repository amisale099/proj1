from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,'homepage.html')

def about(request,id):
    #all_users=Contact.objects.all().exclude(fname='abhi')  # we are getting  objects in to x varibale from database 
    all_users=Contact.objects.all()

    print('x',all_users)         # testing purpose
    return render(request,'about.html',{'all_users':all_users})  # context object in the form of dictionary 

def contact(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        text  = request.POST.get('text')
        c=Contact.objects.create(fname=fname,lname=lname,email=email,phone=phone,text=text) #contructor
        c.save()
    
    x=Contact.objects.all()
    print('x',x) 
    return render(request,'contact.html',{'x':x})


