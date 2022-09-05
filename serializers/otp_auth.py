"""
Dummy Auth Serializer to generate the OTP schema
"""
# libs
import serpy  # pragma: no cover


class OTPAuthSerializer(serpy.Serializer):  # pragma: no cover
    """
    valid:
        description: Response if OTP is valid for the sent email, time, otp
        type: boolean
    """
    valid = serpy.Field()
