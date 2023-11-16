from web3 import Web3
from Data import * #<<== Store your infuria key in Data.py or insert here
#                                                                 v
web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infuria_key}'))

def get_whale_transactions(threshold_wei):
    latest_block_number = web3.eth.block_number

    # Set a block range to search for whale transactions (adjust as needed)
    start_block = max(0, latest_block_number - 10000)
    end_block = latest_block_number

    for block_number in range(start_block, end_block + 1):
        block = web3.eth.get_block(block_number, full_transactions=True)

        for tx in block.transactions:
            value_wei = tx.get('value', 0)
            if value_wei > threshold_wei:
                from_address = tx.get('from', 'Unknown')
                to_address = tx.get('to', 'Unknown')
                value_eth = web3.from_wei(value_wei, 'ether')
                
                data = {
                    "Block Number":block_number,
                    "Transaction":f"https://etherscan.io/tx/{tx['hash'].hex()}",
                    "Sender":{from_address},
                    "Receiver":{to_address},
                    "Value":{float(value_eth)}
                }
                
                print(data) # Store in JSON files to run Vector Analysis

if __name__ == "__main__":
    threshold_wei = 1000000000000000000000 # 1000 ETH I think, and or delete zeroes to adjust
    
    while True:
        get_whale_transactions(threshold_wei)
        import time
        time.sleep(1) # 1 seconds wait before checking again
