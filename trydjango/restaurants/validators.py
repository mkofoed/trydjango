from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
            )


CATEGORIES = ['Mexican', 'Asian', 'American', 'Other']
CATEGORIES = [_.title() for _ in CATEGORIES]


def validate_category(value):
    cat = value.title()
    if not value.title() in CATEGORIES:
        raise ValidationError(f'{value.title()} is not a valid catgory.')