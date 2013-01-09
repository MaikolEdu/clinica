# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paciente'
        db.create_table('principal_paciente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('dni', self.gf('django.db.models.fields.DecimalField')(unique=True, max_digits=8, decimal_places=0)),
            ('hist_clinica', self.gf('django.db.models.fields.DecimalField')(unique=True, max_digits=8, decimal_places=0)),
        ))
        db.send_create_signal('principal', ['Paciente'])

        # Adding model 'Cita'
        db.create_table('principal_cita', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_cita', self.gf('django.db.models.fields.DateField')()),
            ('hora_cita', self.gf('django.db.models.fields.DateTimeField')()),
            ('fecha_aten', self.gf('django.db.models.fields.DateField')()),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Paciente'])),
        ))
        db.send_create_signal('principal', ['Cita'])

        # Adding model 'Pago'
        db.create_table('principal_pago', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_pago', self.gf('django.db.models.fields.DateField')()),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('cita', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Cita'])),
        ))
        db.send_create_signal('principal', ['Pago'])


    def backwards(self, orm):
        # Deleting model 'Paciente'
        db.delete_table('principal_paciente')

        # Deleting model 'Cita'
        db.delete_table('principal_cita')

        # Deleting model 'Pago'
        db.delete_table('principal_pago')


    models = {
        'principal.cita': {
            'Meta': {'object_name': 'Cita'},
            'fecha_aten': ('django.db.models.fields.DateField', [], {}),
            'fecha_cita': ('django.db.models.fields.DateField', [], {}),
            'hora_cita': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Paciente']"})
        },
        'principal.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'dni': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'max_digits': '8', 'decimal_places': '0'}),
            'hist_clinica': ('django.db.models.fields.DecimalField', [], {'unique': 'True', 'max_digits': '8', 'decimal_places': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'principal.pago': {
            'Meta': {'object_name': 'Pago'},
            'cita': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['principal.Cita']"}),
            'fecha_pago': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['principal']