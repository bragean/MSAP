from django.shortcuts import render
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from datetime import *
import json
from django.contrib.auth.models import User

from rest_framework.parsers import FileUploadParser
from rest_framework import status

from datetime import datetime
from . import notification

#report
from django.http import HttpResponse
import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
# Create your views here.

# Vistas para Documentos
class DocumentCreateAPIView(ListCreateAPIView):
	serializer_class = DocumentSerializer
	def get_queryset(self):
		return Document.objects.all().order_by('created')

class DocumentUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = DocumentSerializer
	queryset = Document.objects.all().order_by('created')

class DocumentActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = DocumentUpdateAPIView
	queryset = Document.objects.all().order_by('created')

# Vistas para Procesos
class ProcessCreateAPIView(ListCreateAPIView):
	serializer_class = ProcessSerializer
	def get_queryset(self):
		return Process.objects.all().order_by('created')
# Actualizar Proceso 
class ProcessUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = ProcessSerializer
	queryset = Process.objects.all().order_by('created')
# Cambiar estado del proceso
class ProcessActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = ProcessUpdateAPIView
	queryset = Process.objects.all().order_by('created')
# Vistas para Calcular avance del proceso
class ProcessCalculate(APIView):
	def get(self,request,format=None):
		phases  = Phase.objects.filter(status='1')
		data = []
		for p in phases:
			tasks = Task.objects.filter(id_phase=p.id,status='1')
			print("here")
			total_tasks = 0
			complete_tasks = 0
			for t in tasks:
				total_tasks = total_tasks + 1 
				if t.status_task=='2':
					complete_tasks = complete_tasks + 1
			if total_tasks == 0:
				percentage = 0
			else: 
				percentage = (complete_tasks*100)/total_tasks
			serializer = ProcessCalculateSerializer(data={'id_phase':p.id,'name':p.name,'total_task':total_tasks,'completed_task':complete_tasks,'percentage':percentage})
			serializer.is_valid()
			data.append(serializer.data)
			print(serializer.data)
		return Response(data)

# Vistas para combo box proceso por usuario
class ProcessSelectUser(APIView):
	def get(self, request, pk, format=None):
		proceces = Process.objects.all()
		data = []
		for p in proceces:
			lista = p.user_list.split(',')
			lista.append(p.id_user)
			for l in lista:
				if l == pk:
					try:
						name_user = User.objects.get(id=p.id_user).first_name
					except:
						name_user = ""
					serializer = ProcessAllSerializer(data={'id':p.id,'name':p.name,'id_user':p.id_user,'name_user':name_user,'user_list':p.user_list,'documents_list':p.documents_list,'created':p.created,'last_updated':p.last_updated,'description':p.description,'status_process':p.status_process,'status':p.status})
					serializer.is_valid()
					data.append(serializer.data)
		return Response(data)
	
class ProcessSelect(APIView):
	def get(self,request,format=None):
		proceces = Process.objects.all()
		data = []
		for p in proceces:
			try:
				name_user = User.objects.get(id=p.id_user).first_name
			except:
				name_user = ""
			serializer = ProcessAllSerializer(data={'id':p.id,'name':p.name,'id_user':p.id_user,'name_user':name_user,'user_list':p.user_list,'documents_list':p.documents_list,'created':p.created,'last_updated':p.last_updated,'description':p.description,'status_process':p.status_process,'status':p.status})
			serializer.is_valid()
			data.append(serializer.data)
		return Response(data)
# Vistas para Fases
class PhaseCreateAPIView(ListCreateAPIView):
	serializer_class = PhaseSerializer
	def get_queryset(self):
		return Phase.objects.all().order_by('created')

class PhaseUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = PhaseSerializer
	queryset = Phase.objects.all().order_by('created')
    
class PhaseActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = PhaseUpdateAPIView
	queryset = Phase.objects.all().order_by('created')

class PhaseSelectProcess(APIView):
	def get(self,request,pk, format=None):
		phases = Phase.objects.filter(id_process=pk)
		serializer = PhaseSerializer(phases,many=True)
		return Response(serializer.data)

class PhaseCalculate(APIView):
	def get(self,request,pk,format=None):
		tasks = Task.objects.filter(id_phase=pk,status='1')
		total_tasks = 0
		complete_tasks = 0
		for t in tasks:
			total_tasks = total_tasks + 1 
			if t.status_task=='2':
				complete_tasks = complete_tasks + 1
		if total_tasks == 0:
			percentage = 0
		else: 
			percentage = (complete_tasks*100)/total_tasks
		return Response({"total":total_tasks,"completed":complete_tasks,"percentage":percentage})

# Vistas para Criterios
class CriteriaCreateAPIView(ListCreateAPIView):
	serializer_class = CriteriaSerializer
	def get_queryset(self):
		return Criteria.objects.all().order_by('created')
class CriteriaUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = CriteriaSerializer
	queryset = Criteria.objects.all().order_by('created')
class CriteriaActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = CriteriaUpdateAPIView
	queryset = Criteria.objects.all().order_by('created')
class CriteriaSelectProcess(APIView):
	def get(self,request,pk, format=None):
		criterias = Criteria.objects.filter(id_process=pk, status='1')
		serializer = CriteriaSerializer(criterias,many=True)
		return Response(serializer.data)
class CriteriaCalculate(APIView):
	def get(self,request,pk,pk2,format=None):
		instanteInicial = datetime.now()
		indicators = Indicator.objects.filter(id_criteria = pk2)
		data = []
		for i in indicators:
			tasks = Task.objects.filter(id_phase=pk,id_indicator = i.id ,status='1')
			name = i.name
			total_tasks = 0
			complete_tasks = 0
			for t in tasks:
				total_tasks = total_tasks + 1 
				if t.status_task=='2':
					complete_tasks = complete_tasks + 1
			if total_tasks == 0:
				total = 0
			else:
				total = (100*complete_tasks)/total_tasks
				
			serializer = CriteriaDataSerializer(data={'name':name,'percentage':total})
			serializer.is_valid()
			data.append(serializer.data)
		instanteFinal = datetime.now()
		tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
		print("tiempo de respuesta")
		print(tiempo.microseconds)
		return Response(data)
# Vistas para Indicadores
class IndicatorCreateAPIView(ListCreateAPIView):
	serializer_class = IndicatorSerializer
	def get_queryset(self):
		return Indicator.objects.all().order_by('created')
class IndicatorUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = IndicatorSerializer
	queryset = Indicator.objects.all().order_by('created')
class IndicatorActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = IndicatorUpdateAPIView
	queryset = Indicator.objects.all().order_by('created')
class IndicatorSelectCriteria(APIView):
	def get(self,request,pk, format=None):
		indis = Indicator.objects.filter(id_criteria=pk, status='1')
		serializer = IndicatorSerializer(indis,many=True)
		return Response(serializer.data)
class IndicatorSelectProcess(APIView):
	def get(self,request,pk, format=None):
		criterias = Criteria.objects.filter(id_process=pk)
		if len(criterias) > 0:
			data = []
			for c in criterias:
				indis = Indicator.objects.filter(id_criteria=c.id)
				serializer = IndicatorSerializer(indis,many=True)
				data.append(serializer.data)
			return Response(data)
		else:
			return Response([])
class IndicatorCalculate(APIView):
	def get(self,request,pk,pk2,format=None):
		#calculate de time
		instanteInicial = datetime.now()
		tasks = Task.objects.filter(id_phase=pk,id_indicator = pk2,status='1')
		total_tasks = 0
		complete_tasks = 0
		for t in tasks:
			total_tasks = total_tasks + 1 
			if t.status_task=='2':
				complete_tasks = complete_tasks + 1
		if total_tasks == 0:
			total = 0
		else:
			total = (100*complete_tasks)/total_tasks
		instanteFinal = datetime.now()
		tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
		print("tiempo de respuesta")
		print(tiempo.microseconds)
		return Response({"total":total_tasks,"completed":complete_tasks,"total_percentage":total})
# Vistas para Tareas
class TaskCreateAPIView(ListCreateAPIView):
	serializer_class = TaskSerializer
	def get_queryset(self):
		return Task.objects.all().order_by('created')
class TaskUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = TaskSerializer
	queryset = Task.objects.all().order_by('created')
class TaskChangeStatus(APIView):
	def put(self,request,pk,format=None):
		task = Task.objects.get(id=pk)
		status = request.data.get('status_task')
		id_phase = task.id_phase
		task.status_task=status
		task.save()
		if status == '2':
			tasks = Task.objects.filter(id_phase=id_phase,status='1')
			total_tasks = 0
			complete_tasks = 0
			for t in tasks:
				total_tasks = total_tasks + 1 
				if t.status_task=='2':
					complete_tasks = complete_tasks + 1
			percentage = (complete_tasks * 100)/total_tasks

			phase = Phase.objects.get(id=id_phase)
			id_process = phase.id_process
			phase.status_phase = percentage
			phase.save()

			phases = Phase.objects.filter(id_process=id_process,status='1')
			total_phases = 0
			max_phases = 0
			for p in phases:
				total_phases = total_phases + 1
				percentage = float(p.status_phase)
				max_phases = max_phases + percentage
			
			status_process = max_phases/total_phases
			process = Process.objects.get(id=id_process)
			process.status_process = status_process
			process.save()
			print(status_process)
		return Response({'response':'succes'})
class TaskActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = TaskUpdateAPIView
	queryset = Task.objects.all().order_by('created')
# Vistas para Tarea seleccionar Indicador
class TaskSelectIndicator(APIView):
	def get(self,request,pk,format=None):
		tasks = Task.objects.filter(id_indicator=pk,status='1')
		serializer = TaskSerializer(tasks,many=True)
		return Response(serializer.data)
# Vistas para tarea seleccionar fase
class TaskSelectPhase(APIView):
	def get(self,request,pk,format=None):
		tasks = Task.objects.filter(id_phase = pk)
		data = []
		for t in tasks:
			try:
				name_indicator = Indicator.objects.get(id=t.id_indicator).name
			except:
				name_indicator = ""
			try:
				id_criteria = Indicator.objects.get(id=t.id_indicator).id_criteria
			except:
				id_criteria = ""
			try:
				name_criteria = Criteria.objects.get(id=id_criteria).name
			except:
				name_criteria = ""
			try:
				name_phase = Phase.objects.get(id=t.id_phase).name
			except:
				name_phase = ""
			
			serializer = TaskAllSerializer(data={'id':t.id,'name':t.name,'id_indicator':t.id_indicator,'name_indicator':name_indicator,'id_criteria':id_criteria,'name_criteria':name_criteria,'id_phase':t.id_phase,'name_phase':name_phase,'description':t.description,'start_date':t.start_date,'end_date':t.end_date,'close_date':t.close_date,'status_task':t.status_task,'status':t.status,'user_list':t.user_list,'created':t.created,'last_updated':t.last_updated})
			serializer.is_valid()
			data.append(serializer.data)
		return Response(data)
# Vistas para Contar las tareas
class TaskCount(APIView):
	def get(self,request,pk,format=None):
		instanteInicial = datetime.now()
		tasks = Task.objects.filter(id_phase=pk,status='1')
		total_tasks = 0
		complete_tasks = 0
		for t in tasks:
			total_tasks = total_tasks + 1 
			if t.status_task=='2':
				complete_tasks = complete_tasks + 1
		
		instanteFinal = datetime.now()
		tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
		print("tiempo de respuesta")
		print(tiempo.microseconds)
		return Response({"total":total_tasks,"completed":complete_tasks})
# Vistas para enviar notificaciones
class Notification(APIView):
	def get(self,request, format=None):
		print(notification.SendMail())
		return Response({"status":"succes"})
# up files 
class FileUploadView(APIView):
	parser_class = (FileUploadParser,)
	def post(self, request, *args, **kwargs):
		file_serializer = FileSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Report
def create_report(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename=MSAP.pdf'
	buffer = BytesIO()
	c = canvas.Canvas(buffer, pagesize=A4)
	#cabecera
	c.setLineWidth(.3)
	c.setFont('Helvetica',22)
	c.drawString(30,750,'MSAP')
	c.setFont('Helvetica',12)
	c.drawString(30,735,'Reporte del Proceso')
	c.setFont('Helvetica-Bold',12)
	print(datetime.now())
	date = str(datetime.now().date())
	c.drawString(480,750,date)
	c.line(460,747,560,747)
	#cuerpo
	proces = Process.objects.all()
	notas =[]
	i = 0
	for p in proces:
		i = i + 1
		number = round((float(p.status_process)),2)
		data={'#':i,'name':p.name,'total':number}
		notas.append(data)
	"""	
	notas = [{'#':'1','name':'Henry Aymara Apaza','total':'19.5'},
	         {'#':'1','name':'DBB','total':'20'}]
	"""
	styles = getSampleStyleSheet()
	styleBH = styles["Normal"]
	styleBH.aligment = TA_CENTER
	styleBH.fontSize = 10

	numero = Paragraph('''No.''', styleBH)
	alumno = Paragraph('''Fases''',styleBH)
	total = Paragraph('''Avance(%)''',styleBH)
	data = [[numero, total]]

	styles = getSampleStyleSheet()
	styleN = styles["BodyText"]
	styleN.aligment = TA_CENTER
	styleN.fontSize = 7

	width, height = A4
	high = 650
	for nota in notas:
		this_student = [nota['#'],nota['name'],nota["total"]]
		data.append(this_student)
		high = high - 10

	table = Table(data, colWidths=[19 * mm,95 * mm,19 * mm,19 * mm,19 * mm,19 * mm])
	table.setStyle(TableStyle([
		('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0),(-1,-1), 0.25, colors.black),
	]))
	table.wrapOn(c,width, height)
	table.drawOn(c,30,high)
	c.showPage()
	c.save()
	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)
	return response
