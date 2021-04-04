from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import subject_view, sub_view, unit_view, data_view

urlpatterns = [
    path('', subject_view, name='subject'),
    path('<slug:semester_code>/', sub_view),
    path('<slug:semester_code>/<slug:subject_code>/', unit_view),
    path('<slug:semester_code>/<slug:subject_code>/<slug:unit_code>/', data_view),
]