

import email
from MySQLdb import Date
from django.shortcuts import redirect, render


from django.core.mail import send_mail
from django.conf import settings

from app1.models import StudentList

from app1.models import Product




















# Create your views here.

def firstpage(request):
    return render(request,'first.html',{'Animal':'cat'})

def secondpage(request):
    return render(request,'secondpage.html')

def thirdpage(request):
    return render(request,'thirdpage.html')  

def add(request):
    n1=int(request.GET['num1'])
    n2=int(request.GET['num2'])
    sum=n1+ n2
    return render(request,'result.html',{'result': sum})    

def calculate(request):
    return render(request,'calculate.html') 



def cal(request):
    c=''


    if request.method=='POST':
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        opr=request.POST.get('opr')


        if opr=='+':
            c=n1+n2
        elif opr=='-':

            c=n1-n2
        elif opr=='*':
            c=n1*n2
        elif opr=='/':
            c=n1//n2
    print(c)        

    return render(request,'calculate.html',{'result':c})      


def addproduct(request):
    return render(request,'addproduct.html')


def add_product_details(request):
    if request.method=='POST':
        pname=request.POST['product_name']
        des=request.POST['description']
        qty=request.POST['quantity']
        Price=request.POST['price']


        product=ProductDetails(
        product_name=pname,
        description=des,
        quantity=qty,
        price=Price
        )

        product.save()
        print("saved")
        return redirect('/')

def showproduct(request):
    products=ProductDetails.objects.all()
    return render(request,'show.html',{'product':products})


def editproduct(request,pk):
    products=ProductDetails.objects.get(id=pk)
    return render(request,'edit.html',{'product':products})



def employee(request):
    return render(request,'employee.html')


def add_employee(request):
    if request.method=='POST':
        fname=request.POST['firstname']    
        lname=request.POST['lastname']
        titl=request.POST['title']
        mail=request.POST['emailid']
        ph=request.POST['phone']


        employe=EmployeDeatils(
            firstname=fname,
            lastname=lname,
            title=titl,
            emailid=mail,
            phone=ph,
        )

        employe.save()
        print('saved')
        return redirect('showemp')


def showemp(request):
    emp=   EmployeDeatils.objects.all()
    return render(request,'showemp.html',{'empy': emp})     
    

def edit(request,pk):
    empl=EmployeDeatils.objects.get(id=pk)  
    return render(request,'editemp.html',{'em' : empl})  


def editemployedetail(request,pk):
    if request.method=='POST':
        emp=EmployeDeatils.objects.get(id=pk)    
        emp.firstname=request.POST.get('firstname')
        emp.lastname=request.POST.get('lastname')
        emp.title=request.POST.get('title')
        emp.emailid=request.POST.get('emailid')
        emp.phone=request.POST.get('phone')
        emp.save()
        return redirect('showemp')

def delt(request,pk):
    empdel=EmployeDeatils.objects.get(id=pk)
    return render(request,'deleteemp.html',{'deem' : empdel}) 

def deleteemployee(request,pk):
    demp=EmployeDeatils.objects.get(id=pk)
    demp.delete()
    return redirect('showemp')    


def addstudent(request):
    form = Studentdetailsform()
    return render(request,'addstudent.html',{'form' : form})           



def studentdetails(request):
    if request.method=='POST':
       form=Studentdetailsform(request.POST)
       if form.is_valid():
        form.save()
        return redirect('showstudents')

def showstudents(request):
    std=StudentDetails.objects.all()
    return render(request,'showstudent.html',{'student' : std})        

def editstudent(request,pk):
    st=StudentDetails.objects.get(id=pk)
    form=Studentdetailsform(instance=st)
    if request.method=='POST':
        form=Studentdetailsform(request.POST,instance=st)
        if form.is_valid():
            form.save()
            return redirect('showstudents')
    return render(request,'editstudent.html',{'form' : form})


    

def delete(request,pk):
    delstdnt=StudentDetails.objects.get(id=pk)
    return render(request,'deletestudent.html',{'delst' : delstdnt})   

def delst(request,pk):
    dst=StudentDetails.objects.get(id=pk)
    dst.delete()
    return redirect('showstudents')   


def studentemailid(request):
    Form = Studentemailform()
    if request.method=='POST':
        Form =Studentemailform(request.POST)
        if Form.is_valid():
            Form.save()
            subject = 'Learning'
            message = 'hai'
            recipient = Form.cleaned_data.get('email')
            send_mail(subject,message,settings.EMAIL_HOST_USER, [recipient])
            return redirect('/')
    return render(request,'studentmailid.html',{'form': Form})     



def studentlist(request):
    return render(request,'studentlist.html')        


def adddetails(request):
    if request.method=='POST':
        sname=request.POST['name']
        sage=request.POST['age']
        saddress=request.POST['address']
        semail=request.POST['email']
        sgenter=request.POST['genter']
        sph=request.POST['phone']
        squalification=request.POST['qualification']
        sdate=request.POST['join_date']


        std=StudentList(
            name=sname,
            age=sage,
            address=saddress,
            email=semail,
            genter=sgenter,
            phone=sph,
            qualification=squalification,
            join_date=sdate
        )
        std.save()
        subject = 'Learning'
        message = 'hai'
        recipient=(semail)
        send_mail(subject,message,settings.EMAIL_HOST_USER, [recipient])
        return redirect('showstudentlist')



def showstudentlist(request):
    showst=StudentList.objects.all()
    return render(request,'showstudentlist.html',{'shst': showst})   


def editstudentlist(request,pk):
    editstd=StudentList.objects.get(id=pk)
    return render(request,'editstudentlist.html',{'ed' : editstd})     


def editstlist(request,pk):
    if request.method=='POST':
         student=StudentList.objects.get(id=pk)
         student.name=request.POST.get('name')
         student.age=request.POST.get('age')
         student.address=request.POST.get('address')
         student.email=request.POST.get('email')
         student.genter=request.POST.get('genter')
         student.phone=request.POST.get('phone')
         student.qualification=request.POST.get('qualification')
         student.join_date=request.POST.get('join_date')

         student.save()
         return redirect('showstudentlist')



def stlistdel(request,pk):
    delete=StudentList.objects.get(id=pk)
    return render(request,'deletestudent.html',{'delst' :delete})    

def deletestlist(request,pk):
    delist=StudentList.objects.get(id=pk)
    delist.delete()
    return redirect('showstudentlist')     


def addpro(request):
    return render(request,'new.html')

def addpr(request):
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        count=request.POST['count']
        category1=request.POST['category']
        user_image=request.FILES.get('user_image')

        prdct=Product(
            name=name,
            price=price,
            count=count,
            user_image=user_image,
            category=category1

        )
        prdct.save()
        return redirect('')    
