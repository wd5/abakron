# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    user = models.ForeignKey(User)
    question = models.TextField()
    answer = models.TextField(blank=True)
    visible = models.BooleanField(default=False)
    created = models.DateTimeField()

    class Meta:
        db_table = 'faq_entries'
