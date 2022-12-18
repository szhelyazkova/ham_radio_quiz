from django.core.exceptions import ValidationError


def validate_letters_only(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Ensure this value contains only letters.')
