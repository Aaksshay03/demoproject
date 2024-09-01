from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',welcome,name='welcome'),
    path('view/<int:id>/',view_detail,name='view_detail'),
    path('edit/<int:id>/',edit_detail,name='edit_detail'),
    path('update/<int:id>/',update,name='update')
    
]