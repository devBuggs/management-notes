from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import login_view, register_view

urlpatterns = [
    path("login", login_view, name='login'),
    path("register", register_view, name='register'),
]