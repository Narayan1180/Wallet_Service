# Clone repo
git clone <repo-url>
cd wallet_service

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Seed initial wallet data
python manage.py seed_wallets

# Run server
python manage.py runserver

# test command
curl -X GET http://127.0.0.1:8000/api/wallet/1/1/balance/
# top up test cmd
curl -X POST http://127.0.0.1:8000/api/wallet/1/1/topup/ \
-H "Content-Type: application/json" \
-d '{"amount": 100, "transaction_id": "txn123"}'

# bonus endf point test
curl -X POST http://127.0.0.1:8000/api/wallet/1/1/bonus/ \
-H "Content-Type: application/json" \
-d '{"amount": 50, "transaction_id": "txn124"}'

# spend wallet endpoints

curl -X POST http://127.0.0.1:8000/api/wallet/1/1/spend/ \
-H "Content-Type: application/json" \
-d '{"amount": 200, "transaction_id": "txn125"}'

