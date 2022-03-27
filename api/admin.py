from django.contrib import admin
 
# Register your models here.
from .models import Balance, LogEntry, Ticker
 
admin.site.register(Balance)
admin.site.register(LogEntry)
admin.site.register(Ticker)
