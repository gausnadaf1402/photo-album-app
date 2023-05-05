from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.photo,name='photo'),
    path('add/',views.add,name='add')
]