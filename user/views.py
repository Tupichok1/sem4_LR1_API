from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

class RegistrView(ObtainAuthToken):

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response({
            "status": "succes",
        })

class Logout(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"})

class takeToken(APIView):

    def get(self, request):
        token, created = Token.objects.get_or_create(user = request.user)

        return Response({"token": token.key})
