from rest_framework import serializers
from .models import Balance, LogEntry, Ticker
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.db import transaction

class AirdropSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=200)
    ticker = serializers.CharField(max_length=200)
    saldo = serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        
        u = User.objects.get(id=validated_data['user'])
        tk = Ticker.objects.get(id=validated_data['ticker'])

        try:
            with transaction.atomic():
                e = Balance.objects.select_for_update().get(user=u, ticker=tk)
                e.saldo += validated_data['saldo']
                e.save()
            return Balance.objects.get(user=u, ticker=tk)
        
        except ObjectDoesNotExist:
            e = Balance.objects.create(
                user=u, ticker=tk, saldo=validated_data['saldo'])
            return Balance.objects.get(user=u, ticker=tk)
        

class BurnSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=200)
    ticker = serializers.CharField(max_length=200)
    saldo = serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        u = User.objects.get(id=validated_data['user'])
        tk = Ticker.objects.get(id=validated_data['ticker'])

        try:
            e = Balance.objects.get(user=u, ticker=tk)
        except:
            raise serializers.ValidationError('error')

        if e:
            if e.saldo-validated_data['saldo'] > 0:
                e.saldo -= validated_data['saldo']
                e.save()
            else:
                raise serializers.ValidationError("monto insuficiente")

        return Balance.objects.get(user=u, ticker=tk)


class PeerSerializer(serializers.Serializer):
    emisor =   serializers.CharField(max_length=200)
    receptor = serializers.CharField(max_length=200)
    ticker =   serializers.CharField(max_length=200)
    saldo =    serializers.DecimalField(max_digits=5, decimal_places=2)

    def create(self, validated_data):
        u = User.objects.get(id=validated_data['receptor'])
        u2 = User.objects.get(id=validated_data['emisor'])
        tk = Ticker.objects.get(id=validated_data['ticker'])

        # debit emisor
        try:
            e = Balance.objects.get(user=u2, ticker=tk)
        except:
            raise serializers.ValidationError('error')

        if e:
            if e.saldo-validated_data['saldo'] > 0:
                e.saldo -= validated_data['saldo']
                e.save()
            else:
                raise serializers.ValidationError("monto insuficiente")

        # add receptor
        try:
            e2 = Balance.objects.get(user=u, ticker=tk)
        except ObjectDoesNotExist:
            e2 = Balance.objects.create(
                user=u, ticker=tk, saldo=validated_data['saldo'])
            return {'emisor': u2, 'receptor': u, 'ticker': tk, 'saldo': e.saldo}

        e2.saldo += validated_data['saldo']
        e2.save()

        return {'emisor': u2, 'receptor': u, 'ticker': tk, 'saldo': e.saldo}

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'