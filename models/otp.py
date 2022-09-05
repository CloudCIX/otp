# libs
from django.db import models


class OTP(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.CharField(primary_key=True, max_length=255)
    secret = models.CharField(max_length=16)

    class Meta:
        db_table = 'otp'
