# -*- coding: utf-8 -*-

import os

from django.db import models
from django.contrib.auth.models import User

from utils.fields.autoonetoone import AutoOneToOneField
from utils.files.storage.overwrite import OverwriteStorage

def image_upload(instance, filename):
    return 'profiles/%(id)05d%(ext)s' % {
        'id': instance.pk,
        'ext': os.path.splitext(filename)[1],
    }


class Profile(models.Model):
    user = AutoOneToOneField(User)
    image = models.ImageField(upload_to=image_upload, blank=True, storage=OverwriteStorage())

    class Meta:
        db_table = 'auth_profile'
