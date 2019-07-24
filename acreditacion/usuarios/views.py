from django.shortcuts import render
from .models import *
from Process.models import Process
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from datetime import *
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth

from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.
class UserDetailCreateAPIView(APIView):
	def post(self, request, format=None):
		first_name = request.data.get('first_name')
		last_name = request.data.get('last_name')
		username = request.data.get('username')
		password = request.data.get('password')
		id_usertype = request.data.get('id_usertype')
		photo = request.data.get('photo')
		status = request.data.get('status')	
		if username == None or password == None:
			print("no se puede registrar")
			return Response({'response':'failed'})
		else:
			user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
			user.set_password(password)
			user.save()
			id_user = user.id
			user_detail= UserDetail(id_user=id_user, id_usertype=id_usertype,photo=photo, status=status)
			user_detail.save()
			return Response({'response':'succes'})

# Update User
class UserDetailUpdateAPIView(APIView):
	def put(self, request, pk, format=None):
		first_name = request.data.get('first_name')
		last_name = request.data.get('last_name')
		username = request.data.get('username')
		id_usertype = request.data.get('id_usertype')
		photo = request.data.get('photo')
		status = request.data.get('status')

		user = User.objects.get(id=pk)
		id_user = user.id
		user.first_name = first_name
		user.last_name = last_name
		user.save()

		user_detail= UserDetail.objects.get(id_user=id_user)
		user_detail.id_usertype = id_usertype
		user_detail.photo = photo
		user_detail.status = status 
		user_detail.save()
		return Response({'response':'succes'})

class UserSelectProcess(APIView):
	def get(self, request, pk, format=None):
		proces = Process.objects.get(id=pk)
		list_user = proces.user_list
		lista = list_user.split(',')
		data = []
		for l in lista:
			try:
				name1 = User.objects.get(id=l).first_name
			except:
				name1 = ""
			try:
				name2 = User.objects.get(id=l).last_name
			except:
				name2 = ""
			name = name1 +" "+ name2
			serializer = UserSelect(data={'id':l,'first_name':name})
			serializer.is_valid()
			data.append(serializer.data)
		return Response(data)


class UserDetailActiveAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = UserDetailUpdateAPIView
	queryset = UserDetail.objects.all().order_by('created')

# all users fields 
class UserAllAPIView(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		data = []
		for user in users:
			try:
				photo = UserDetail.objects.get(id_user=user.id).photo
			except:
				photo = ""
			try:
				id_user_type= UserDetail.objects.get(id_user=user.id).id_usertype
			except:
				id_user_type = ""
			try:
				user_type= UserType.objects.get(id=id_user_type).name
			except:
				user_type = ""
			try:
				id_usertype= UserType.objects.get(id=id_user_type).id
			except:
				id_usertype = ""
			try:
				status = UserDetail.objects.get(id_user=user.id).status
			except:
				status = ""
			serializer = UserDetailSerializer(data={'id':str(user.id),'username':user.username,'first_name':user.first_name,'last_name':user.last_name,'status':status,'photo':photo,'id_usertype':id_usertype,'user_type':user_type})
			serializer.is_valid()
			data.append(serializer.data)
		return Response(data)

class UserTypeCreateAPIView(ListCreateAPIView):
	serializer_class = UserTypeSerializer
	def get_queryset(self):
		return UserType.objects.all().order_by('created')

class UserTypeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all().order_by('created')

class UserTypeUpdateAPIView(RetrieveUpdateDestroyAPIView):
	serializer_class = UserTypeUpdateSerializer
	queryset = UserType.objects.all().order_by('created')



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	username = request.data.get("username")
	password = request.data.get("password")
	if username is None or password is None:
		return Response({'error': 'Porfavor insertar username y password'},
					status=HTTP_400_BAD_REQUEST)
	user = authenticate(username=username, password=password)
	if not user:
		return Response({'error': 'Validacion Incorrecta'},
						status=HTTP_404_NOT_FOUND)
	token, _ = Token.objects.get_or_create(user=user)
	try:
		user_detail = UserDetail.objects.get(id_user=user.id)
		serializer = UserDetailTokenSerializer(data={'id':str(user.id),'username':user.username,'first_name':user.first_name,'token':token.key,'last_name':user.last_name,'status':user_detail.status,'photo':user_detail.photo,'user_type':user_detail.id_usertype})
	except:
		serializer = UserDetailTokenSerializer(data={'id':str(user.id),'username':user.username,'first_name':user.first_name,'token':token.key,'last_name':user.last_name})
	serializer.is_valid()
	return Response(serializer.data,
					status=HTTP_200_OK)