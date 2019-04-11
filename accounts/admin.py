from django.contrib import admin
from .models import Allergy, Account

# Register your models here.
admin.site.register(Account)
admin.site.register(Allergy)