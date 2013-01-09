from django.db import models

class Paciente(models.Model):  
	nombre = models.CharField(max_length=15)
	apellido= models.CharField(max_length=25)
	correo=models.EmailField(max_length=75)
	direccion= models.CharField(max_length=75)
	dni=models.DecimalField(max_digits=8, decimal_places=0, unique=True) 
	hist_clinica= models.DecimalField(max_digits=8, decimal_places=0, unique=True)

	def __unicode__ (self): 
		return '%s %s' %(self.nombre,self.apellido)


class Cita(models.Model):
	fecha_cita=models.DateField()
	hora_cita=models.DateTimeField()
	fecha_aten=models.DateField()
	paciente= models.ForeignKey(Paciente)	

	def __unicode__	(self):
		return '%s' %(self.paciente)

class Pago(models.Model):
	fecha_pago= models.DateField()
	monto=models.DecimalField(max_digits=10, decimal_places=2)
	cita=models.ForeignKey(Cita)

	def __unicode__(self):
		return '%s' %(self.cita.paciente)
