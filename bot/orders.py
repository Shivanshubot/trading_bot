from binance.exceptions import BinanceAPIException
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
import logging

logger = logging.getLogger("trading_bot")


def place_order(client, symbol, side, order_type, quantity, price=None, leverage=10):
    try:

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)


        client.futures_change_leverage(
            symbol=symbol,
            leverage=leverage
        )

        logger.info(f"Leverage set to {leverage}x")
        print(f"⚙️ Leverage set to {leverage}x")


        ticker = client.futures_mark_price(symbol=symbol)
        current_price = float(ticker["markPrice"])

        print(f"\n📊 Current Market Price: {current_price}")
        logger.info(f"Current Market Price: {current_price}")


        if order_type == "LIMIT":
            if side == "SELL" and price < current_price:
                raise ValueError(
                    f"SELL LIMIT price must be >= market price ({current_price})"
                )

            if side == "BUY" and price > current_price:
                raise ValueError(
                    f"BUY LIMIT price must be <= market price ({current_price})"
                )


        logger.info(
            f"Placing order: {symbol} | {side} | {order_type} | qty={quantity} | price={price}"
        )

        balance_info = client.futures_account_balance()

        usdt_balance = 0
        for asset in balance_info:
            if asset["asset"] == "USDT":
                usdt_balance = float(asset["balance"])
                break

        print(f"💰 Available Balance: {usdt_balance} USDT")
        logger.info(f"Available Balance: {usdt_balance} USDT")
        if usdt_balance < 10:
            raise ValueError("Insufficient balance (<10 USDT)")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )


        order_id = response["orderId"]

        final_status = client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        logger.info(f"Final Order Status: {final_status}")

        return final_status

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        print(f"\n❌ Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"General Error: {e}")
        print(f"\n❌ Error: {e}")
        raise
 
    notional = quantity * current_price

    print(f"📦 Order Notional: {notional:.2f} USDT")
    logger.info(f"Order Notional: {notional}")