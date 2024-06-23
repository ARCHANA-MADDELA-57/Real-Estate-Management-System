from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('index',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('index',views.index,name='index'),
    path('service',views.service,name='service'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('registration',views.registration,name='registration'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('properties',views.properties,name='properties'),
    path('land_types',views.land_types,name='land_types'),
    path('message_admin',views.message_admin,name='message_admin'),
    path('total_users',views.total_users,name='total_users'),
    path('total_lands',views.total_lands,name='total_lands'),
    path('total_sellerlands',views.total_sellerlands,name='total_sellerlands'),
    path('add_lands',views.add_lands,name='add_lands'),
    path('sellerdash',views.sellerdash,name='sellerdash'),
    path('sellerlands',views.sellerlands,name='sellerlands'),
    path('selleraddland',views.selleraddland,name='selleraddland'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('sellerregistration',views.sellerregistration,name='sellerregistration'),
    path('sellerlogin',views.sellerlogin,name='sellerlogin'),
    path('edituser/<int:userid>/',views.edituser, name='edituser'),
    path('total_sellers',views.total_sellers,name='total_sellers'),
    path('editland/<int:land_id>/',views.editland, name='editland'),
    path('editseller/<str:seller_id>/',views.editseller, name='editseller'),
    path('editsellerland/<int:land_id>/',views.editsellerland, name='editsellerland'),
    path('logout',views.logout,name='logout'),
    path('signout',views.signout,name='signout'),
    path('logoff',views.logoff,name='logoff'),
    path('deleteuser/<str:userid>/',views.deleteuser,name='deleteuser'),
    path('deleteseller/<str:sellerid>/',views.deleteseller,name='deleteseller'),
    path('deleteland/<str:land_id>/',views.deleteland,name='deleteland'),
    path('deletesellerland/<str:sellerid>/',views.deletesellerland,name='deletesellerland'),
    path('adminprofile',views.adminprofile,name='adminprofile'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('sellerprofile',views.sellerprofile,name='sellerprofile'),
    path('change_password',views.change_password,name='change_password'),
    path('forget_password',views.forget_password,name='forget_password'),
    path('complaint',views.complaint,name='complaint'),
    path('complaints',views.complaints,name='complaints'),

    
   
]
