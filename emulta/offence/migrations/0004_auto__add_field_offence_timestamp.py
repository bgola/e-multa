# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Offence.timestamp'
        db.add_column('offence_offence', 'timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 6, 15, 12, 4, 2, 55712), auto_now=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Offence.timestamp'
        db.delete_column('offence_offence', 'timestamp')


    models = {
        'offence.offence': {
            'Meta': {'object_name': 'Offence'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_plate': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 15, 12, 4, 2, 55712)', 'auto_now': 'True', 'blank': 'True'}),
            'vehicle_type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['offence']
