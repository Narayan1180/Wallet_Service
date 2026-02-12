from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'asset_type', 'balance']


class TransactionSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    transaction_id = serializers.CharField(max_length=100)
