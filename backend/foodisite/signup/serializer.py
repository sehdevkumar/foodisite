from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import  serializers


class UserRegisterSerializer(serializers.ModelSerializer):
   
   
    class Meta:
        model = User
        fields = ['username','email','first_name', 'password' ]