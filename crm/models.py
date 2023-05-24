from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



class Customer(models.Model):
    cust_id = models.CharField(max_length=254,default="")
    cust_name = models.CharField(max_length=254,default="")
    cust_address = models.CharField(max_length=254,default="")	
    cust_con_per = models.CharField(max_length=254,default="")	
    cust_mobile = models.CharField(max_length=254,default="")	
    cust_tele = models.CharField(max_length=254)	
    cust_whatsapp = models.CharField(max_length=254,default="")	
    cust_email = models.CharField(max_length=254,default="")	
    cust_website = models.CharField(max_length=254,default="")	
    cust_gst = models.CharField(max_length=254,default="")	
    cust_city = models.CharField(max_length=254,default="")	
    cust_state = models.CharField(max_length=254,default="")	
    cust_country = models.CharField(max_length=254,default="")	
    cust_pin = models.CharField(max_length=254,default="")
    cust_org = models.CharField(max_length=254,default="")


class Worksheet(models.Model):
    cust_id = models.CharField(max_length=254,default="")
    cust_name = models.CharField(max_length=254,default="")
    worktype = models.CharField(max_length=254,default="")
    workprogress = models.CharField(max_length=254,default="")
    remarks = models.CharField(max_length=50,default="")
    cust_org = models.CharField(max_length=254,default="")
    current_date = models.DateField()


   


class Credentials(models.Model):
    cust_id = models.CharField(max_length=254,default="")
    cust_name = models.CharField(max_length=254,default="")
    item = models.CharField(max_length=254,default="")
    type = models.CharField(max_length=254,default="")
    plateform = models.CharField(max_length=254,default="")
    username = models.CharField(max_length=254,default="")
    password = models.CharField(max_length=254,default="")
    remark = models.CharField(max_length=254,default="")
    status = models.CharField(max_length=254,default="")
    cust_org = models.CharField(max_length=254,default="")


class Renewal(models.Model):
    cust_id = models.CharField(max_length=254,default="")
    cust_name = models.CharField(max_length=254,default="")
    cust_org = models.CharField(max_length=254,default="")
    product = models.CharField(max_length=254,default="")
    rdc = models.DateField()
    rde = models.DateField()
    remark = models.CharField(max_length=254,default="")
    status = models.CharField(max_length=254,default="")
    








    
    
