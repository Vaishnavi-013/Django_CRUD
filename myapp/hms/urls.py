from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",hms_home),
    path("add-doctor/",add_doctor),
    path("delete-hms/<int:doctor_id>",delete_hms), 
    path("update-hms/<int:doctor_id>",update_hms),
    path("do-update-hms/<int:doctor_id>",do_update_hms),



    
    
]