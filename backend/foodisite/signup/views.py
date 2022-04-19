from functools import partial
import imp
from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.models import User
from .serializer import  UserRegisterSerializer

class RegisterView(APIView):

    def post(self,request):
        data = request.data
        serializer = UserRegisterSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response("created sucess", status=HTTP_200_OK)

class LoginView(APIView):
    
    def post(self,request):
        data = request.data
        serializer = UserRegisterSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response("created sucess", status=HTTP_200_OK)