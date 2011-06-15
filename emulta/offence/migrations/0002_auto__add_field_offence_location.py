# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Offence.location'
        db.add_column('offence_offence', 'location', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Offence.location'
        db.delete_column('offence_offence', 'location')


    models = {
        'offence.offence': {
            'Meta': {'object_name': 'Offence'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_plate': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'vehicle_type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['offence']
