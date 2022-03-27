from .serializers import *

from rest_framework import  generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework.exceptions import ValidationError

# Airdrop:
class AirdropView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AirdropSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Burn:
class BurnView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BurnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Peer To Peer:
class PeerView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PeerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# list balance +  token
class SingleBalance(generics.ListAPIView):

    permission_classes = (IsAuthenticated, ) 
    serializer_class = BalanceSerializer

    def get_queryset(self, *args, **kwargs):

        _id = self.kwargs["pk"]     
        t = self.request.auth
        tu = Token.objects.get(user_id=_id)
        if t == tu:
            return Balance.objects.filter(user=_id)
        raise ValidationError(detail='Invalid Token')


# list log
class SingleLog(generics.ListAPIView):
    serializer_class = LogSerializer

    def get_queryset(self, *args, **kwargs):
        _id = self.kwargs["pk"]
        b = Balance.objects.filter(user=_id)[0]
        return LogEntry.objects.filter(balance__user=b.user)
