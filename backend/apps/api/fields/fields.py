import base64
import imghdr
import uuid

import six
from django.core import validators
from django.core.files.base import ContentFile
from django.db import models
from rest_framework import serializers


class ColorField(models.CharField):
    """Поле для хранения HTML-кода цвета."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)
        self.validators.append(validators.RegexValidator(r'#[a-f\d]{6}'))


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')
            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = '%s.%s' % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)
        return super().to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        if extension == 'jpeg':
            extension = 'jpg'
        return extension  # noqa R504
