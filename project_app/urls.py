from django.urls import path,include
from project_app import views

#app_name='project_app'

urlpatterns=[
    path('sign_up/',views.register,name="register"),
    path('sign_in/',views.logn,name='logn'),
]
