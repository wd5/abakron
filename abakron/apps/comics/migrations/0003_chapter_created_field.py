# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Chapter.created'
        db.add_column('comics_chapters', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Chapter.created'
        db.delete_column('comics_chapters', 'created')

    models = {
        'comics.chapter': {
            'Meta': {'object_name': 'Chapter', 'db_table': "'comics_chapters'"},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
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