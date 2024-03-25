from django.core.validators import RegexValidator

class item:
    username_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._-]+$',
        message='Username can only contain letters, numbers, and ._-'
    )
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z]+$',
        message='Name can only contain letters'
    )
    password_validator = RegexValidator(
        regex=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=\-{}[\]:;"\'|,.<>/?]).{8,}$',
        message='Password must contain at least 8 characters, including uppercase, lowercase, numbers, and special characters'
    )
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        message='Enter a valid email address'
    )