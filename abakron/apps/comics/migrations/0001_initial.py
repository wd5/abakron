# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chapter'
        db.create_table('comics_chapters', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('comics', ['Chapter'])

        # Adding model 'Comics'
        db.create_table('comics_comics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chapter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comics', to=orm['comics.Chapter'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('comics', ['Comics'])

    def backwards(self, orm):
        # Deleting model 'Chapter'
        db.delete_table('comics_chapters')

        # Deleting model 'Comics'
        db.delete_table('comics_comics')

    models = {
        'comics.chapter': {
            'Meta': {'object_name': 'Chapter', 'db_table': "'comics_chapters'"},
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'comics.comics': {
            'Meta': {'object_name': 'Comics'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comics'", 'to': "orm['comics.Chapter']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['comics']