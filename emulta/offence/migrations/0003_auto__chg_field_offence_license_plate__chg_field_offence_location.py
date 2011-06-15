# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Offence.license_plate'
        db.alter_column('offence_offence', 'license_plate', self.gf('django.db.models.fields.CharField')(max_length=8))

        # Changing field 'Offence.location'
        db.alter_column('offence_offence', 'location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))


    def backwards(self, orm):
        
        # Changing field 'Offence.license_plate'
        db.alter_column('offence_offence', 'license_plate', self.gf('django.db.models.fields.CharField')(max_length=7))

        # Changing field 'Offence.location'
        db.alter_column('offence_offence', 'location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))


    models = {
        'offence.offence': {
            'Meta': {'object_name': 'Offence'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_plate': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'vehicle_type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['offence']
