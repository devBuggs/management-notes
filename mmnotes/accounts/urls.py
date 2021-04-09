from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import login_view, register_view, logout_view, profile_view, editprofile_view, payment_view, payment_info, payment_notify, editContact_view

urlpatterns = [
    path('profile/', profile_view, name='userProfile'),
    path('login/', login_view, name='userLogin'),
    path('register/', register_view, name='userRegister'),
    path('logout/', logout_view, name='userLogout'),
    path('editprofile/', editprofile_view, name='editprofile'),
    path('editcontact/', editContact_view, name='editcontact'),
    path('checkout/', payment_view, name='checkout'),
    path('payment_info/', payment_info, name="paymentSuccess"),
    path('payment_notify', payment_notify, name="paymentNotify"),
]