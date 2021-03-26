from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import login_view, register_view, logout_view, home_view, template, mainTemp

urlpatterns = [
    path('home/', home_view, name='userHome'),
    path('login/', login_view, name='userLogin'),
    path('register/', register_view, name='userRegister'),
    path('logout/', logout_view, name='userLogout'),
    path('template', template, name='template'),
    path('main', mainTemp, name='main'),
]