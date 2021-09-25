from django.urls import path

# import views here
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contactus'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('about/', views.about_view, name='aboutus'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('tou/', views.tou_view, name='tou'),
]