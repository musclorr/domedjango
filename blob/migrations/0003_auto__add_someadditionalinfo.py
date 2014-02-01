# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SomeAdditionalInfo'
        db.create_table(u'blob_someadditionalinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blob', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blob.Blob'])),
            ('sometext', self.gf('django.db.models.fields.CharField')(max_length=17)),
        ))
        db.send_create_signal(u'blob', ['SomeAdditionalInfo'])


    def backwards(self, orm):
        # Deleting model 'SomeAdditionalInfo'
        db.delete_table(u'blob_someadditionalinfo')


    models = {
        u'blob.blob': {
            'Meta': {'object_name': 'Blob'},
            'datext': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'someotherfield': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40'})
        },
        u'blob.someadditionalinfo': {
            'Meta': {'object_name': 'SomeAdditionalInfo'},
            'blob': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blob.Blob']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sometext': ('django.db.models.fields.CharField', [], {'max_length': '17'})
        }
    }

    complete_apps = ['blob']