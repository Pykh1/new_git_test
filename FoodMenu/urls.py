from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.index,name="index"),
    path('item/', views.item,name="item"),
]