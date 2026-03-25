from bot.client import BinanceSpotClient

client = BinanceSpotClient()


def execute_order(symbol, side, order_type, quantity, price=None):
    try:
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("ORDERS.PY RESPONSE:", response)
        return response

    except Exception as e:
        print(f"❌ Error executing order: {str(e)}")
        return None