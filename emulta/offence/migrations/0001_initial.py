# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Offence'
        db.create_table('offence_offence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('license_plate', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('media_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('vehicle_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('offence', ['Offence'])


    def backwards(self, orm):
        
        # Deleting model 'Offence'
        db.delete_table('offence_offence')


    models = {
        'offence.offence': {
            'Meta': {'object_name': 'Offence'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_plate': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'vehicle_type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['offence']
