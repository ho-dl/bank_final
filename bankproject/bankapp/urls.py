from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('submit_form/', views.submit_form, name='submit_form'),
]
