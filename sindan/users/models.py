from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import django.contrib.auth.models as auth


class User(auth.AbstractBaseUser, auth.PermissionsMixin):
    """
    Custom user model that behaves like Django default one.
    """
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_(
            'Username should contains 30 characters or fewer, '
            'including Letters, digits and - only.'
        ),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _(
                "A user with that email address already exists."
            ),
        },
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this '
            'admin site.'
        ),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = auth.UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
