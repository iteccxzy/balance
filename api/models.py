
from django.db import models
from django.contrib.auth.models import User


class Ticker(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion


class Balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.ForeignKey(Ticker,  on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_crear = models.DateTimeField(auto_now_add=True, blank=True)
    fecha_actualizar = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.user} --> {self.ticker}"

    class Meta:
        unique_together = [['user', 'ticker']]


class LogEntry(models.Model):
    AIRDROP = 'ai'
    BURN = 'bu'
    P2P = '2p'

    T_CHOICES = [
        (AIRDROP, 'airdrop'),
        (BURN, 'burn'),
        (P2P, 'psp')

    ]
    balance = models.ForeignKey(Balance,  on_delete=models.CASCADE)
    monto_anterior = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    monto_posterior = models.DecimalField(max_digits=7, decimal_places=2)
    monto_operado = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_crear = models.DateTimeField(auto_now_add=True)
    trans = models.CharField(max_length=2, choices=T_CHOICES, default=AIRDROP)
    

    def __str__(self):
        return f"anterior: {self.monto_anterior}, operado: {self.monto_operado}, posterior: {self.monto_posterior},  tipo {self.trans}, user: {self.balance} "
