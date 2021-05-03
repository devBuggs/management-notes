from django.urls import path
from .views import initiate_payment, callback, paymentCallback

urlpatterns = [
    path('pay/', initiate_payment, name='pay'),
    path('callback/', callback, name='callback'),
    path('payment_info/<slug:received_data>', paymentCallback ),
]