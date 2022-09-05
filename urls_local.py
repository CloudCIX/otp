from django.urls import include, path

urlpatterns = [
    path('', include('otp.urls')),
]
