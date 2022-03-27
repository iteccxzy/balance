from django.db.models.signals import post_save
from .models import Balance, LogEntry

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# registro de todas las operaciones que impactan un balance
# de un usuario
def log(sender, instance, created,  **kwargs):

    i = LogEntry.objects.filter(balance=instance).last()

    if i is None:
        LogEntry.objects.create(balance=instance, monto_anterior=None,
                                monto_posterior=instance.saldo, monto_operado=instance.saldo, trans='ai')
    else:
        anterior = i.monto_posterior

        if instance.saldo > 0:
            trans = 'ai'
        else:
            trans = 'bu'

        LogEntry.objects.create(balance=instance,
                                monto_anterior=anterior,
                                monto_posterior=instance.saldo,
                                monto_operado=instance.saldo-anterior,
                                trans=trans)


post_save.connect(log, sender=Balance)


# token para usuarios
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
