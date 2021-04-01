from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import subject_view

urlpatterns = [
    path('subject', subject_view, name='subject'),
]