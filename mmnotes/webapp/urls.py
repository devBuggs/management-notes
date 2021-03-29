from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# import views here
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contactus'),
]