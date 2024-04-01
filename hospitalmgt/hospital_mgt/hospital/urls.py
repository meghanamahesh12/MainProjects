
from django.urls import path
from .views import About,Home,Contact, Login,Logout_admin,Index,View_Doctor,Delete_Doctor,Add_Doctor,View_Patient,Add_Patient,Delete_Patient,View_Appoinment,Add_Appoinment,Delete_Appoinment
urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('admin_login/',Login,name='admin_login'),
    path('logout/',Logout_admin,name='logout_admin'),
    path('index/', Index ,name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_patient/',View_Patient,name='view_patient'),
    path('view_appoinment/',View_Appoinment,name='view_appoinment'),
    path('add_appoinment/', Add_Appoinment, name='add_appoinment'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_doctor(?P<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient(?P<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('delete_appoinment(?P<int:pid>)/', Delete_Appoinment, name='delete_appoinment'),





    

]
