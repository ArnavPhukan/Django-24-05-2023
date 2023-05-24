from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from crm.models import *
from django.contrib.auth.hashers import make_password
from .forms import *
from django.http import JsonResponse
import mysql.connector
import pandas as pd
from django.shortcuts import render
from datetime import date
import datetime

"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="crmdb"
)
"""


# Create your views here.
def home(request):
	return render(request,'crm/home.html')	

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			request.session.set_expiry(120)
			return redirect('home')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('login_user')	
	else:
		return render(request, 'crm/login_user.html')
	

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)

        check_user = User.objects.filter(username=username).count()
        check_email = User.objects.filter(email=email).count()

        if(check_user > 0):
            messages.error(request, 'Username is already taken')
            return redirect('register')
        elif(check_email > 0):
            messages.error(request, 'Email is already taken')
            return redirect('register')
        else:
            User.objects.create(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully, Please Sign In')
            return redirect('login_user')
    else:
        return render(request, 'crm/register.html')    
    

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('login_user')


def customer(request):
      context={'status':'profile'}
      return render(request,'crm/home.html',context)


def worksheet(request):
    name = request.POST.get('cust_org')
    customer = Customer.objects.filter(cust_org=name).first()
    df1 = Customer.objects.values_list('cust_org', flat=True)
    df1 = list(df1)
    df1 = set(df1)
    current_date = date.today()
    current_time = datetime.datetime.now()
    return render(request, 'crm/home.html', {'customer': customer,'status':'work','df1':df1,'current_date':current_date,'current_time':current_time})
    

def credentials(request):
    name = request.POST.get('cust_org')
    customer = Customer.objects.filter(cust_org=name).first()
    df1 = Customer.objects.values_list('cust_org', flat=True)
    df1 = list(df1)
    df1 = set(df1)
    context={'status':'cred','customer':customer,'df1':df1}
    return render(request,'crm/home.html',context)

def renewal(request):
    name = request.POST.get('cust_org')
    customer = Customer.objects.filter(cust_org=name).first()
    df1 = Customer.objects.values_list('cust_org', flat=True)
    df1 = list(df1)
    df1 = set(df1)
    context={'status':'renewal','df1':df1,'customer':customer}
    return render(request,'crm/home.html',context)


def uploadCustomer(request):
    cust_id = request.POST['cust_id']
    cust_name = request.POST['cust_name']
    cust_address = request.POST['cust_address']	
    cust_con_per = request.POST['cust_con_per']	
    cust_mobile = request.POST['cust_mobile']	
    cust_tele = request.POST['cust_tele']	
    cust_whatsapp = request.POST['cust_whatsapp']	
    cust_email = request.POST['cust_email']	
    cust_website = request.POST['cust_website']	
    cust_gst = request.POST['cust_gst']	
    cust_city = request.POST['cust_city']	
    cust_state = request.POST['cust_state']	
    cust_country = request.POST['cust_country']	
    cust_pin = request.POST['cust_pin']
    cust_org = request.POST['cust_org']
    

    p = Customer(
    cust_id = cust_id,
    cust_name = cust_name,
    cust_address = cust_address,	
    cust_con_per = cust_con_per,
    cust_mobile = cust_mobile,	
    cust_tele = cust_tele,
    cust_whatsapp = cust_whatsapp,	
    cust_email = cust_email,
    cust_website = cust_website,	
    cust_gst = cust_gst,	
    cust_city = cust_city,	
    cust_state = cust_state,	
    cust_country = cust_country,	
    cust_pin = cust_pin,
    cust_org = cust_org)

    p.save()

    context = {'status':'there_is_profile'}

    return render(request, 'crm/home.html',context)

def uploadWorksheet(request):
    cust_id=request.POST['cust_id']
    cust_name=request.POST['cust_name']
    worktype=request.POST['worktype']
    workprogress=request.POST['workprogress']
    remarks=request.POST['remarks']
    cust_org=request.POST['cust_org']
    current_date=request.POST['current_date']


    p = Worksheet(
        cust_id=cust_id,
        cust_name=cust_name,
        worktype=worktype,
        workprogress=workprogress,
        remarks=remarks,
        cust_org=cust_org,
        current_date=current_date
    )
    
    p.save()
    
    context = {'status':'there_is_worksheet'}

    return render(request, 'crm/home.html', {'success': True, 'context':context})
    


def uploadCredentials(request):
    cust_id = request.POST['cust_id']
    cust_name = request.POST['cust_name']
    item = request.POST['item']
    type = request.POST['type']
    plateform = request.POST['plateform']
    username = request.POST['username']
    password = request.POST['password']
    remark = request.POST['remark']
    status = request.POST['status']
    cust_org = request.POST['cust_org']

    c = Credentials(
    cust_id = cust_id,
    cust_name = cust_name,
    item = item,
    type = type,
    plateform = plateform,
    username = username,
    password = password,
    remark = remark,
    status = status,
    cust_org = cust_org
    )

    c.save()

    context = {'status':'there_is_cred'}

    return render(request, 'crm/home.html', {'success': True, 'context':context})

def uploadRenewal(request):
    cust_id=request.POST['cust_id']
    cust_name=request.POST['cust_name']
    cust_org = request.POST['cust_org']
    product = request.POST['product']
    rdc = request.POST['rdc']
    rde = request.POST['rde']
    remark = request.POST['remark']
    status = request.POST['status']
   
    r = Renewal(
    cust_id=cust_id,
    cust_name=cust_name,
    cust_org=cust_org,
    product = product,
    rdc = rdc,
    rde = rde,
    remark=remark,
    status=status
    )

    r.save()

    context = {'status':'there_is_renew'}

    return render(request, 'crm/home.html', {'success': True, 'context':context})


def getworksheet(request):
    worksheet = Worksheet.objects.all()
    context={'worksheet':worksheet,'status':'wreport'}
    return render(request,'crm/home.html',context)

def getrenewal(request):
    renewal = Renewal.objects.all()
    context={'renewal':renewal,'status':'rreport'}
    return render(request,'crm/home.html',context)

def getcredentials(request):
    credential = Credentials.objects.all()
    context={'credential':credential,'status':'ccreport'}
    return render(request,'crm/home.html',context)
   
def getcustomer(request):
    customer = Customer.objects.all()
    context={'customer':customer,'status':'creport'}
    return render(request,'crm/home.html',context)






     


     


     


      
        
   
     


    

    
     












    




















      

    



     
