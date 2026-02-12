from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Wallet, Ledger
from .serializers import TransactionSerializer

def get_wallet(user_id, asset_type_id):
    return Wallet.objects.select_for_update().get(user_id=user_id, asset_type_id=asset_type_id)

class WalletBalanceView(APIView):
    def get(self, request, user_id, asset_type_id):
        try:
            wallet = Wallet.objects.get(user_id=user_id, asset_type_id=asset_type_id)
            return Response({"balance": wallet.balance})
        except Wallet.DoesNotExist:
            return Response({"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)


class WalletTopUpView(APIView):
    def post(self, request, user_id, asset_type_id):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        transaction_id = serializer.validated_data['transaction_id']

        with transaction.atomic():
            wallet = get_wallet(user_id, asset_type_id)
            if Ledger.objects.filter(transaction_id=transaction_id).exists():
                return Response({"balance": wallet.balance})
            wallet.balance += amount
            wallet.save()
            Ledger.objects.create(wallet=wallet, amount=amount, type='TOPUP', transaction_id=transaction_id)
            return Response({"balance": wallet.balance})


class WalletBonusView(APIView):
    def post(self, request, user_id, asset_type_id):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        transaction_id = serializer.validated_data['transaction_id']

        with transaction.atomic():
            wallet = get_wallet(user_id, asset_type_id)
            if Ledger.objects.filter(transaction_id=transaction_id).exists():
                return Response({"balance": wallet.balance})
            wallet.balance += amount
            wallet.save()
            Ledger.objects.create(wallet=wallet, amount=amount, type='BONUS', transaction_id=transaction_id)
            return Response({"balance": wallet.balance})


class WalletSpendView(APIView):
    def post(self, request, user_id, asset_type_id):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data['amount']
        transaction_id = serializer.validated_data['transaction_id']

        with transaction.atomic():
            wallet = get_wallet(user_id, asset_type_id)
            if Ledger.objects.filter(transaction_id=transaction_id).exists():
                return Response({"balance": wallet.balance})
            if wallet.balance < amount:
                return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
            wallet.balance -= amount
            wallet.save()
            Ledger.objects.create(wallet=wallet, amount=-amount, type='SPEND', transaction_id=transaction_id)
            return Response({"balance": wallet.balance})
