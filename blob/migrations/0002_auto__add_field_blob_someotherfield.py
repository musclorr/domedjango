# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Blob.someotherfield'
        db.add_column(u'blob_blob', 'someotherfield',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Blob.someotherfield'
        db.delete_column(u'blob_blob', 'someotherfield')


    models = {
        u'blob.blob': {
            'Meta': {'object_name': 'Blob'},
            'datext': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'someotherfield': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['blob']