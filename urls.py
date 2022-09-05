from django.urls import path
from . import views

urlpatterns = [
    # OTP
    path(
        'otp/',
        views.OTPCollection.as_view(),
        name='otp_collection',
    ),
    # OTP Auth
    path(
        'otp_auth/<email>/',
        views.OTPAuthCollection.as_view(),
        name='otp_auth_collection',
    ),
]
