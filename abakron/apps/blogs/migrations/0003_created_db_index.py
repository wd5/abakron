# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Post', fields ['created']
        db.create_index(u'blog_posts', ['created'])

    def backwards(self, orm):
        # Removing index on 'Post', fields ['created']
        db.delete_index(u'blog_posts', ['created'])

    models = {
        'blogs.post': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'Post', 'db_table': "u'blog_posts'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['blogs']