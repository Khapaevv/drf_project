from rest_framework.serializers import ValidationError

normal_link = 'youtube.com'


def validate_normal_link(value):
    if normal_link not in value.lower():
        raise ValidationError('Cсылки на сторонние сайты запрещены')
