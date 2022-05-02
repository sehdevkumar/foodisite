import email
from functools import partial
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_409_CONFLICT, HTTP_201_CREATED
from django.contrib.auth.models import User
from .serializer import UserRegisterSerializer

# Create the User


class RegisterView(APIView):

    def post(self, request):
        # data = request.data
        username = request.query_params.get('name').split(' ')[0]
        first_name = request.query_params.get('name')
        email = request.query_params.get('email')
        password = request.query_params.get('password')

        data = {
            'username': username,
            'first_name': first_name,
            'email': email,
            'password': password,
        }

        serializer = UserRegisterSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data, status=HTTP_201_CREATED)
        else:
            emailExists = User.objects.filter(
                email=email).exists()
            usernasmeExists = User.objects.filter(
                username=username).exists()
            if emailExists or usernasmeExists:
                return Response(serializer.errors, status=HTTP_409_CONFLICT)

            return Response(serializer.errors, status=HTTP_409_CONFLICT)