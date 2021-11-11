from django.contrib import admin
from django.urls import path,include
from algo import views

urlpatterns = [
    path('', views.home),
    path('systeme_1/', views.system_1,name="systeme1"),
    path('systeme_1_verify_1/', views.system_1_verify_1,name="systeme1_verify_1"),
    path('systeme_2/', views.system_2,name="systeme2"),
    path('admin/', admin.site.urls),
]
