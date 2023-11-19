from pybit.unified_trading import WebSocket

ws = WebSocket(
    testnet=False,
    channel_type='linear'
)

prices = [] # Stores the prices in this array
def handleMessage(message):
    try:
        prices.append(message['data']['bid1Price'])
        print(message['data']['bid1Price'])
    except Exception as f:
        print("Error occured in the function `handle message` : ",f)
        
ws.ticker_stream(
    symbol='ETHUSDT',
    callback=handleMessage
)

print("Starting")
while True:
    time.sleep(0.1)

# NOTE: if want to store the array, use the h5 file saving function `SaveH5` importing from _general_functions.py file
