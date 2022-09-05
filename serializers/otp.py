"""
Dummy OTP Serializer to generate the OTP schema
"""
# libs
import serpy  # pragma: no cover


class OTPSerializer(serpy.Serializer):  # pragma: no cover
    """
    otp:
        description: Dummy Serializer
        type: string
    """
    otp = serpy.Field()
