from . import views
from django.urls import path



urlpatterns=[
    path('',views.firstpage,name='firstpage'),
    path('secondpage',views.secondpage,name='secondpage'),
    path('thirdpage',views.thirdpage,name='thirdpage'),
    path('add',views.add,name='add'),
    path('calculate',views.calculate,name='calculate'),
    path('cal',views.cal,name='cal'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('add_product_details',views.add_product_details,name='add_product_details'),
    path('showproduct',views.showproduct,name='showproduct'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('employee',views.employee,name='employee'),
    path('add_employee',views.add_employee,name='add_employee'),
    path('showemp',views.showemp,name='showemp'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editemployedetail/<int:pk>',views.editemployedetail,name='editemployedetail'),
    path('delt/<int:pk>',views.delt,name='delt'),
    path('deleteemployee/<int:pk>',views.deleteemployee,name='deleteemployee'),
    path('addstudent',views.addstudent,name='addstudent'),

    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('showstudents',views.showstudents,name='showstudents'),
    path('editstudent/<int:pk>',views.editstudent,name='editstudent'),
 
    path('delete/<int:pk>',views.delete,name='delete'),
    path(' delst/<int:pk>',views. delst,name=' delst'),
    path('studentemailid',views.studentemailid,name='studentemailid'),

    path('studentlist',views.studentlist,name='studentlist'),
    path('adddetails',views.adddetails,name='adddetails'),
    path('showstudentlist',views.showstudentlist,name='showstudentlist'),
    path('editstudentlist/<int:pk>',views.editstudentlist,name='editstudentlist'),
    path('editstlist<int:pk>',views.editstlist,name='editstlist'),
    path('stlistdel/<int:pk>',views. stlistdel,name=' stlistdel'),
    path('deletestlist/<int:pk>',views.deletestlist,name='deletestlist'),
    path('addpro',views.addpro,name='addpro'),
    path('addpr',views.addpr,name='addpr'),

   
    

]