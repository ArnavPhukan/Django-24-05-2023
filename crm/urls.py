
from django.urls import path
from crm import views

urlpatterns = [

    path('home/',views.home,name='home'),
    path('',views.login_user,name='login_user'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout_user'),

    path('profile_save/', views.uploadCustomer, name="profile_save"),
    path('work_save/', views.uploadWorksheet, name="work_save"),
    path('cred_save/', views.uploadCredentials, name="cred_save"),
    path('renew_save/', views.uploadRenewal, name="renew_save"),

    path('customer',views.customer,name='customer'),
    path('worksheet',views.worksheet,name='worksheet'),
    path('credentials',views.credentials,name='credentials'),
    path('renewals',views.renewal,name='renewals'),

    path('getworksheet',views.getworksheet,name='getworksheet'),
    path('getcustomer',views.getcustomer,name='getcustomer'),
    path('getrenewal',views.getrenewal,name='getrenewal'),
    path('getcredentials',views.getcredentials,name='getcredentials')

]


   