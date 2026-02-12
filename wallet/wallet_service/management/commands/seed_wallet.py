from django.core.management.base import BaseCommand
from wallet_service.models import AssetType, User, Wallet

class Command(BaseCommand):
    help = 'Seed initial wallet data'

    def handle(self, *args, **options):
        # Create Asset Types
        gold = AssetType.objects.get_or_create(name='Gold Coins')[0]
        diamonds = AssetType.objects.get_or_create(name='Diamonds')[0]
        loyalty = AssetType.objects.get_or_create(name='Loyalty Points')[0]

        # Create Users
        alice = User.objects.get_or_create(name='Alice', email='alice@example.com')[0]
        bob = User.objects.get_or_create(name='Bob', email='bob@example.com')[0]

        # Create System Wallet (Treasury)
        Wallet.objects.get_or_create(user=None, asset_type=gold, balance=1000000)
        Wallet.objects.get_or_create(user=None, asset_type=diamonds, balance=500000)
        Wallet.objects.get_or_create(user=None, asset_type=loyalty, balance=100000)

        # Create User Wallets
        Wallet.objects.get_or_create(user=alice, asset_type=gold, balance=500)
        Wallet.objects.get_or_create(user=alice, asset_type=diamonds, balance=100)
        Wallet.objects.get_or_create(user=bob, asset_type=gold, balance=300)
        Wallet.objects.get_or_create(user=bob, asset_type=loyalty, balance=200)

        self.stdout.write(self.style.SUCCESS('Seed data created successfully!'))
