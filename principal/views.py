from principal.models import Paciente,Cita,Pago
from django.shortcuts import render_to_response

def lista_pacientes(request):
	paciente = Paciente.objects.all()
	return render_to_response('lista_pacientes.html',{'paciente':paciente})