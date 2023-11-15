from pybit.unified_trading import WebSocket
from time import sleep,time
ws = WebSocket(
    testnet=False,
    channel_type="linear",
)


def handle_message(message1):
    try:
        if float(message1['data']['b'][0][1]) - float(message1['data']['a'][0][1]) >= 20:
            print("Buy Activity : ",time())
        elif float(message1['data']['b'][0][1]) - float(message1['data']['a'][0][1]) <= -20:
            print("Sell Activity : ",time())
    except Exception as e:
        print(e)

ws.orderbook_stream(
    depth=1,
    symbol='ETHUSDT',
    callback= handle_message
)

print("Starting")
while True:
    sleep(0.1)
