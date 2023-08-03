from web3 import Web3

# Reference Link : https://web3py.readthedocs.io/en/stable/web3.eth.html

# Connect to the Ethereum network using a provider (e.g., Infura)
API_URL = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 =  Web3( Web3.HTTPProvider(API_URL))

# Function to retrieve gas prices
def getGasPrices():
    try:
        gasPrices={}

        # Retrieve the gas prices from the network
        # Returns the current gas price in Wei.
        gasPrices["current"] = web3.eth.gas_price

        # Calculate gas prices at different levels
        gasPrices["safe"] = int(gasPrices["current"] * 0.9)  # 90% of the current gas price
        gasPrices["average"] = int(gasPrices["current"] * 1.0)   # Same as the current gas price
        gasPrices["fast"] = int(gasPrices["current"] * 1.1)      # 110% of the current gas price
        gasPrices["fastest"] = int(gasPrices["current"] * 1.2)   # 120% of the current gas price
        
        return gasPrices

    except Exception as e:
        print(f"Error: {e}")
        return None
