# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blob'
        db.create_table(u'blob_blob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datext', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'blob', ['Blob'])


    def backwards(self, orm):
        # Deleting model 'Blob'
        db.delete_table(u'blob_blob')


    models = {
        u'blob.blob': {
            'Meta': {'object_name': 'Blob'},
            'datext': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blob']