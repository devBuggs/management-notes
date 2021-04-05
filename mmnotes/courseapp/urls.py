from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import dashboard_view, sub_view, unit_view, data_view

urlpatterns = [
    path('', dashboard_view, name='userDashboard'),
    path('<slug:semester_code>/', sub_view, name='sem'),
    path('<slug:semester_code>/<slug:subject_code>/', unit_view, name='sub'),
    
    path('<slug:subject_code>/<slug:unit_code>/', data_view, name='unit'),
    path('<slug:semester_code>/<slug:subject_code>/<slug:unit_code>/', data_view),
]