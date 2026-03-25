import click
from bot.orders import execute_order


@click.command()
@click.option('--symbol', required=True, help='Trading pair (e.g., BTCUSDT)')
@click.option('--side', required=True, type=click.Choice(['BUY', 'SELL']), help='Order side')
@click.option('--type', 'order_type', required=True, type=click.Choice(['MARKET', 'LIMIT']), help='Order type')
@click.option('--quantity', required=True, type=float, help='Order quantity')
@click.option('--price', required=False, type=float, help='Price (required for LIMIT orders)')
def main(symbol, side, order_type, quantity, price):
    print("\n====== ORDER SUMMARY ======")
    print(f"Symbol     : {symbol}")
    print(f"Side       : {side}")
    print(f"Type       : {order_type}")
    print(f"Quantity   : {quantity}")
    if price:
        print(f"Price      : {price}")

    # Execute order
    response = execute_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price
    )

    print("\nRAW RESPONSE:", response)

    print("\n====== ORDER RESPONSE ======")
    if response:
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Price        : {response.get('price', 'MARKET')}")
    else:
        print("⚠️ No response received from API")

    print("\n✅ Order placed successfully!")


if __name__ == "__main__":
    main()