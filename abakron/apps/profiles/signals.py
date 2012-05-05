# -*- coding: utf-8 -*-

import os.path

import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from social_auth.signals import pre_update
from social_auth.backends.twitter import TwitterBackend
from social_auth.backends.facebook import FacebookBackend

def twitter_extra_values(sender, user, response, details, **kwargs):
    image = NamedTemporaryFile(delete=True)
    image.write(requests.get(response['profile_image_url']).content)
    image.flush()

    ext = os.path.splitext(response['profile_image_url'])[1]
    user.profile.image.save('%05d%s' % (user.pk, ext), File(image), save=True)

    return True

def facebook_extra_values(sender, user, response, details, **kwargs):
    try:
        image = NamedTemporaryFile(delete=True)
        image.write(requests.get('https://graph.facebook.com/%s/picture' % response['id']).content)
        image.flush()

        user.profile.image.save('%05d.jpg' %user.pk, File(image), save=True)
    except Exception as e:
        import traceback; traceback.print_exc()
        print e
    return True

def connect():
    pre_update.connect(twitter_extra_values, sender=TwitterBackend)
    pre_update.connect(facebook_extra_values, sender=FacebookBackend)