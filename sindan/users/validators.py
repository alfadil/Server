from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import string

# Allowed characters in username field
ALLOWED_USERNAME_CHARS = set([
    # ascii lowercase
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z',
    # ascii uppercase
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z',
    # numbers & special characters
    '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', '_', '-'
])

def username_validator(username):
    m = set(username) - ALLOWED_USERNAME_CHARS
    if len(m) == 0:
        return
    raise ValidationError(
        _('Username should contains 30 characters or fewer, including Letters, digits and _ only.')
    )
