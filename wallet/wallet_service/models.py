from django.db import models

# Create your models here.
from django.db import models, transaction
from django.utils import timezone

class AssetType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    asset_type = models.ForeignKey(AssetType, on_delete=models.CASCADE)
    balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'asset_type')

    def __str__(self):
        return f"{self.user} - {self.asset_type}"


class Ledger(models.Model):
    TRANSACTION_TYPES = [
        ('TOPUP', 'Top-up'),
        ('BONUS', 'Bonus'),
        ('SPEND', 'Spend')
    ]

    STATUS = [
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed')
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    status = models.CharField(max_length=20, choices=STATUS, default='SUCCESS')
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['transaction_id']),
        ]

    def __str__(self):
        return f"{self.wallet} - {self.amount} - {self.type}"
