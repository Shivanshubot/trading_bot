# Binance Futures Testnet Trading Bot

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Working-success)
![API](https://img.shields.io/badge/API-Binance%20Futures-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

# Binance Futures Testnet Trading Bot

## Overview

This is a Python-based CLI trading bot that interacts with Binance Futures Testnet (USDT-M).
It supports MARKET and LIMIT orders with proper validation, logging, and error handling.

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file:

```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

Get API keys from:
https://testnet.binancefuture.com

---

## How to Run

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 72000
```

### Optional (with leverage)

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002 --leverage 10
```

---

## Features

* MARKET and LIMIT order support
* BUY / SELL support
* CLI input via argparse
* Input validation
* Logging of requests & responses
* Error handling
* Leverage configuration
* Balance check
* Market price validation

---

## Logging

Logs are stored in:

```
logs/bot.log
```

---

## Sample Logs

### MARKET Order

```
INFO | Placing order: BTCUSDT BUY MARKET qty=0.002
INFO | Order Response: {...}
INFO | Final Order Status: FILLED
```

### LIMIT Order

```
INFO | Placing order: BTCUSDT SELL LIMIT qty=0.002 price=72000
INFO | Order Response: {...}
INFO | Final Order Status: NEW
```

---

## Assumptions

* Binance Futures Testnet account is active
* API keys are valid and enabled for Futures trading
* Minimum notional value (>= 100 USDT) is respected
* Sufficient margin is available or leverage is used

---

## Notes

* This bot uses Binance Futures Testnet (not real funds)
* Can be easily extended to mainnet by changing API config

---

## Leverage Support

This bot supports configurable leverage for Binance Futures trading.

Leverage allows you to trade larger positions with a smaller amount of capital.

---

### Usage with Leverage

You can specify leverage using the `--leverage` flag:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002 --leverage 10
```

---

### Example

* Quantity: `0.002 BTC`
* Price: ~`70,000 USDT`
* Notional Value: ~`140 USDT`

With **10x leverage**, required margin ≈ `14 USDT`

---

### Notes

* Default leverage is set to **10x**
* Leverage is applied per symbol before placing the order
* Higher leverage increases both potential profit and risk
* Ensure sufficient margin is available in your Futures wallet

---


## Example Output

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

Output:

```
 Order Request Summary
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

 Current Market Price: 71412.8
 Leverage set to 10x
 Available Balance: 1000 USDT

 Order Successful!
Status: FILLED
Executed Qty: 0.002
Avg Price: 71400
```

---

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 72000
```

Output:

```
 Current Market Price: 71380

 Order Successful!
Status: NEW
```


## Project Architecture

```
CLI (cli.py)
   ↓
Order Logic (orders.py)
   ↓
Validation (validators.py)
   ↓
Binance Client (client.py)
   ↓
Binance Futures API
```

* `client.py` → Handles API connection
* `orders.py` → Core trading logic
* `validators.py` → Input validation
* `logging_config.py` → Logging setup
* `cli.py` → User interface

---



