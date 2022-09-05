"""
Management of OTP
"""
# libs
from cloudcix_rest.exceptions import Http400
from django.conf import settings
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
# local
from otp.controllers import OTPCreateController, OTPUpdateController
from otp.models import OTP
from otp.permissions.otp import Permissions


class OTPCollection(APIView):

    def post(self, request: Request) -> Response:
        """
        summary: Create a new OTP record

        description: Create a new OTP record using the data supplied by the User.

        responses:
            200:
                description: OTP record was updated successfully
            201:
                description: OTP record was created successfully
            400: {}
            403: {}
        """
        tracer = settings.TRACER

        # Check the permission
        with tracer.start_span('checking_permissions', child_of=request.span):
            err = Permissions.create(request)
            if err is not None:
                return err

        with tracer.start_span('retrieving_requested_object', child_of=request.span) as span:
            try:
                obj = OTP.objects.get(
                    pk=request.user.email,
                )
            except (OTP.DoesNotExist, AttributeError):
                # Add user and secret
                with tracer.start_span('validating_create_controller', child_of=span):
                    controller = OTPCreateController(
                        data=request.data,
                        request=request,
                        span=span,
                    )
                    if not controller.is_valid():
                        return Http400(errors=controller.errors)
                with tracer.start_span('saving_object', child_of=span):
                    controller.cleaned_data['email'] = request.user.email
                    controller.instance.save()

                return Response({'otp': 'created'}, status=status.HTTP_201_CREATED)

        # update user
        with tracer.start_span('validating_updating_controller', child_of=request.span) as span:
            controller = OTPUpdateController(
                instance=obj,
                data=request.data,
                request=request,
                span=span,
            )
            if not controller.is_valid():
                return Http400(errors=controller.errors)
        with tracer.start_span('saving_object', child_of=span):
            controller.cleaned_data['email'] = request.user.email
            controller.instance.save()

        return Response({'otp': 'updated'}, status=status.HTTP_200_OK)
