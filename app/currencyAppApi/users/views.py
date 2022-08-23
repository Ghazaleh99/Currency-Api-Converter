from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegistrationSerializer,UserfavSerializer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Userfav
from rest_framework import generics


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)

class Registeration(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)

class Watchlist(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Userfav
    serializer_class = UserfavSerializer

    def get_queryset(self):
        user = self.request.user
        return Userfav.objects.filter(user = user)