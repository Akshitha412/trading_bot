from binance.client import Client

class BinanceSpotClient:
    def __init__(self):
        api_key = "jrfH3WplQIZAUUUK7GcuURD2CY9PzLrR7P6wXZ65e67bq8eniMVSbuw8LUYnFlVd"
        api_secret = "CAwawxS00VNxe8mSaryIsb8NE7JrdKnF97ISDhhfMCQxueR3SKRu4VG2EZJabdwM"

        self.client = Client(
            api_key,
            api_secret,
            testnet=True   # 🔥 THIS IS CRITICAL
        )

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == "MARKET":
                order = self.client.create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )
            else:
                order = self.client.create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            print("CLIENT RESPONSE:", order)
            return order

        except Exception as e:
            print("CLIENT ERROR:", str(e))
            raise Exception(f"API Error: {str(e)}")