from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET"),
        testnet=True  # ✅ THIS IS CRITICAL
    )

    # Override futures testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client