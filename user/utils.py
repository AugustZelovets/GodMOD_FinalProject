import re

from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core import validators


class UsernameValidator(validators.RegexValidator):
    regex = r"[\w.]\Z"
    message = (
        "Enter a valid username. Length 20 characters or less, may contain only English letters, "
        "numbers, and . _ characters."
    )
    flags = re.ASCII
