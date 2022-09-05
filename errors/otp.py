"""
Error codes for all of the methods in OTP service
"""

# Create
otp_create_101 = 'The "secret" parameter is invalid. "secret" is required.'
otp_create_102 = 'The "secret" parameter is invalid. "secret" must be 16 characters.'
otp_create_103 = 'The "secret" parameter is invalid. "secret" must be a valid Base32 hash.'
otp_create_201 = 'You do not have permission to make this request. Your Member must be self managed.'

# Update
otp_update_101 = 'The "secret" parameter is invalid. "secret" is required.'
otp_update_102 = 'The "secret" parameter is invalid. "secret" must be 16 characters.'
otp_update_103 = 'The "secret" parameter is invalid. "secret" must be a valid Base32 hash.'
