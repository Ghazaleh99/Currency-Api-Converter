from rest_framework import generics
from .models import Currency
# from django.db.models import Q
from .serializers import CurrencySerializer
from users.models import Userfav
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView

class ListCurrency(generics.ListAPIView):
    #  ListAPIView to display all
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class DetailCurrency(generics.RetrieveAPIView): 
    # RetrieveAPIView to display a single model instance
    permission_classes = [permissions.IsAuthenticated]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class Addfavorite(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        fav_currency = get_object_or_404(Currency,pk=pk)
        print(fav_currency)
        if Userfav.objects.filter(user = request.user, favCur = fav_currency).exists():
            return Response(status=status.HTTP_200_OK)
        else:
            if Userfav.objects.filter(user = request.user).exists():
                new = Userfav.objects.get(user = request.user)
                new.favCur.add(fav_currency)
                new.save()
            else:
                new = Userfav(user = request.user)
                new.save()
                new.favCur.add(fav_currency)
        return Response(status=status.HTTP_200_OK)

class Removefavorite(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        fav_currency = get_object_or_404(Currency,pk=pk)
        if Userfav.objects.filter(user = request.user, favCur = fav_currency).exists():
            new = Userfav.objects.get(user = request.user)
            new.favCur.remove(fav_currency)
            new.save()
        return Response(status=status.HTTP_200_OK)