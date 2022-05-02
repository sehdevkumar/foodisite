from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from django.contrib.auth.models import User


class LoginView(APIView):

    def post(self, request):
        if not request.data['username'] or not request.data['password']:
            return Response('Invalid Credentials', status=HTTP_404_NOT_FOUND)
        username = User.objects.filter(
            username=request.data['username']).exists()
        password = User.objects.filter(
            password=request.data['password']).exists()
        print(username, password)
        if username is False:
            return Response('Username is not exist', status=HTTP_404_NOT_FOUND)
        elif password is False:
            return Response('Invalid Password', status=HTTP_404_NOT_FOUND)

        return Response("User is logged in", status=HTTP_200_OK)
