from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core import validators
from django.db import models

from ham_radio_quiz.validators import validate_letters_only


class AppUser(AbstractUser):
    MIN_LEN_FIRST_NAME = 5
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 5
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_CALL_SIGN = 4
    MAX_LEN_CALL_SIGN = 6

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_letters_only,
        ),
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_letters_only,
        ),
        blank=True,
        null=True,
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    call_sign = models.CharField(
        max_length=MAX_LEN_CALL_SIGN,
        unique=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_CALL_SIGN),
        ),
        blank=True,
        null=True,
    )

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.replace('None', '').strip()
