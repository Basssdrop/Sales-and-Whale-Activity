import asyncio,websockets,json,hmac,hashlib,time
from Data import * #Put api_secret and api_key in Data.py file

async def authenticate(api_key, api_secret):
    timestamp = int(time.time()*1000)
    
    signature = str(hmac.new(
        bytes(api_secret,"utf-8"),
        bytes(f"GET/realtime{timestamp}","utf-8"), digestmod="sha256"
    ).hexdigest())
    
    auth_payload = {
        "op": "auth",
        "args": [api_key,timestamp,signature]
    }
    
    return json.dumps(auth_payload)

async def subscribe_to_private_stream(api_key,api_secret):
    uri = "wss://stream.bybit.com/v5/public/linear"
    
    async with websockets.connect(uri) as websocket:
        
        auth_message = await authenticate(api_key,api_secret)
        await websocket.send(auth_message)
        
        subscribe_message = {
        "op": "subscribe",
        "args": ["INSERT DATA STREAM"]
        }
        await websocket.send(json.dumps({"op":"ping"}))
        await websocket.send(json.dumps(subscribe_message))
        
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            print(data)
            
asyncio.get_event_loop().run_until_complete(subscribe_to_private_stream(api_key,api_secret))
