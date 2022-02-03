from django.contrib import admin
from django.urls import path
from cafeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('details', views.details, name='details'),
    path('details1', views.details1, name='details1'),
    path('details2', views.details2, name='details2'),
    path('details3', views.details3, name='details3'),
    path('details4', views.details4, name='details4'),
    path('details5', views.details5, name='details5'),
    path('details6', views.details6, name='details6'),
    path('details7', views.details7, name='details7'),
    path('details8', views.details8, name='details8'),
    path('details9', views.details9, name='details9'),
]
