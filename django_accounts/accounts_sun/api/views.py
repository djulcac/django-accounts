from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist
from knox.models import AuthToken
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions, views
from rest_framework.response import Response

from . import serializers


class LoginAPI(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    http_method_names = ['post']
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Description:
            El campo 'identifier' sirve para ingresar
            el 'username' o 'email', entonces
            si contiene un '@' se trata de un email  y se debe aplicar
            la logica correspondiente
        """
        identifier = request.data.get('identifier')
        password = request.data.get('password')
        user = None
        if identifier and '@' in identifier:
            User = get_user_model()
            try:
                usertemp = User.objects.get(email=identifier)
                user = authenticate(username=usertemp.username, password=password)
            except ObjectDoesNotExist:
                print(f"The user with identifier '{identifier}' was not found")
        else:
            user = authenticate(username=identifier, password=password)
        if user is not None:
            return Response({
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'token': AuthToken.objects.create(user)[1],
            })
        return Response(
            {'error': 'Invalid Credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class MeAPIView(views.APIView):
    serializer_class = serializers.MeSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = serializers.MeSerializer(request.user)
        return Response(serializer.data)
