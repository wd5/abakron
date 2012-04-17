# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Chapter', fields ['slug']
        db.create_unique('comics_chapters', ['slug'])

        # Adding index on 'Comics', fields ['position']
        db.create_index('comics_comics', ['position'])

        # Adding unique constraint on 'Comics', fields ['chapter', 'position']
        db.create_unique('comics_comics', ['chapter_id', 'position'])

    def backwards(self, orm):
        # Removing unique constraint on 'Comics', fields ['chapter', 'position']
        db.delete_unique('comics_comics', ['chapter_id', 'position'])

        # Removing index on 'Comics', fields ['position']
        db.delete_index('comics_comics', ['position'])

        # Removing unique constraint on 'Chapter', fields ['slug']
        db.delete_unique('comics_chapters', ['slug'])

    models = {
        'comics.chapter': {
            'Meta': {'object_name': 'Chapter', 'db_table': "'comics_chapters'"},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comics.comics': {
            'Meta': {'unique_together': "(('chapter', 'position'),)", 'object_name': 'Comics'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comics'", 'to': "orm['comics.Chapter']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['comics']