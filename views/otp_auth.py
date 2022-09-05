"""
Management of OTP Auth
"""
# python
from datetime import datetime, timedelta
import pyotp
# libs
from cloudcix_rest.exceptions import Http400
from cloudcix_rest.views import APIView
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
# local
from ..models.otp import OTP


class LoginPermission(BasePermission):
    """
    Custom DRF Permission for this class
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False


class OTPAuthCollection(APIView):

    permission_classes = (LoginPermission,)

    def post(self, request: Request, email: str) -> Response:
        """
        summary: validate an otp request

        description: Validate an OTP record using the data supplied by the User.

        responses:
            200:
                description: OTP record was validated successfully
            400: {}
            403: {}
            404: {}
        """
        time = datetime.now()
        tracer = settings.TRACER
        data = request.data
        with tracer.start_span('checking_for_required_fields', child_of=request.span):
            if 'otp' not in data:
                return Http400(error_code='otp_otp_auth_create_001')

        with tracer.start_span('retrieving_requested_object', child_of=request.span):
            try:
                obj = OTP.objects.get(pk__iexact=email)
            except (OTP.DoesNotExist, AttributeError):
                return Http400(error_code='otp_otp_auth_create_001')

        with tracer.start_span('get_otp', child_of=request.span):
            otp1 = pyotp.totp.TOTP(obj.secret).at(time)
            time = time - timedelta(seconds=30)
            otp2 = pyotp.totp.TOTP(obj.secret).at(time)
        # check if users otp and otp created using the time and secret are the same
        with tracer.start_span('validate_otp', child_of=request.span):
            if otp1 != data['otp'] and otp2 != data['otp']:
                return Http400(error_code='otp_otp_auth_create_001')

        return Response({'valid': True}, status=status.HTTP_200_OK)
