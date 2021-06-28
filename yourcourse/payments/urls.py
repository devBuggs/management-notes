from django.urls import path
from .views import initiate_payment, callback, paymentCallback, enrollmentCourse

urlpatterns = [
    path('pay/', initiate_payment, name='pay'),
    path('callback/', callback, name='callback'),
    path('payment_info/', paymentCallback, name='payment_info'),
    path('enrollment/', enrollmentCourse, name='enrollment'),
]