# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Post', fields ['slug']
        db.create_unique(u'blog_posts', ['slug'])

    def backwards(self, orm):
        # Removing unique constraint on 'Post', fields ['slug']
        db.delete_unique(u'blog_posts', ['slug'])

    models = {
        'blogs.post': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Post', 'db_table': "u'blog_posts'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['blogs']