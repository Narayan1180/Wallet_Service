from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AssetType, User, Wallet, Ledger

admin.site.register(AssetType)
admin.site.register(User)
admin.site.register(Wallet)
admin.site.register(Ledger)
