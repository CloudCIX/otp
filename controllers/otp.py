# python
import re
from typing import Optional
# libs
from cloudcix_rest.controllers import ControllerBase
# local
from ..models import OTP


class OTPCreateController(ControllerBase):

    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific for this Controller
        """
        model = OTP
        validation_order = (
            'secret',
        )

    def validate_secret(self, secret: Optional[str]) -> Optional[str]:
        """
        description: secret is the hash used in one time password authentication
        type: string
        """
        if secret is None:
            return 'otp_create_101'
        if len(secret) != 16:
            return 'otp_create_102'
        regex = re.match('^[A-Z2-7]+=*$', secret)
        if not regex:
            return 'otp_create_103'
        self.cleaned_data['secret'] = str(secret)
        return None


class OTPUpdateController(ControllerBase):

    class Meta(ControllerBase.Meta):
        """
        Override some of the ControllerBase.Meta fields to make them more specific for this Controller
        """
        model = OTP
        validation_order = ('secret',)

    def validate_secret(self, secret: Optional[str]) -> Optional[str]:
        """
        description: secret is the hash used in one time password authentication
        type: string
        """
        if not secret:
            return 'otp_update_101'
        if len(secret) != 16:
            return 'otp_update_102'
        regex = re.match('^[A-Z2-7]+=*$', secret)
        if not regex:
            return 'otp_update_103'
        self.cleaned_data['secret'] = str(secret)
        return None
