import requests
from datetime import datetime

def get_erc20_token_transfers(address, api_key, contract_address=None, startblock=0, endblock=99999999, page=1, offset=100, sort='asc'):
    """
    Fetches ERC20 token transfer events for a given Ethereum address using the Etherscan API.

    Parameters:
        address (str): Ethereum address to query.
        api_key (str): Your Etherscan API key.
        contract_address (str): (Optional) ERC20 token contract address to filter by.
        startblock (int): Starting block number (default is 0).
        endblock (int): Ending block number (default is 99999999).
        page (int): Page number for pagination (default is 1).
        offset (int): Number of transactions per page (default is 100, max is 10000).
        sort (str): Sort order: 'asc' or 'desc' (default is 'asc').

    Returns:
        list: A list of token transfer event dictionaries.
    """
    url = 'https://api.etherscan.io/api'
    params = {
        'module': 'account',
        'action': 'tokentx',
        'address': address,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }
    if contract_address:
        params['contractaddress'] = contract_address

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == '1':
            token_transfers = data['result']
            return token_transfers
        elif data['status'] == '0' and data['message'] == 'No transactions found':
            print('No token transfer events found for this address.')
            return []
        else:
            print('Error:', data['message'])
            return []
    except Exception as e:
        print('An error occurred:', e)
        return []

# Example usage
if __name__ == '__main__':
    # Replace with your Ethereum address and Etherscan API key
    address = '0x7b54194220Ed6928EB222705304A6571f6243C9e'
    api_key = '9ZUCWCDSQ5E521UR5PCSBXFNHNAZCICYYB'
    # Optional: specify a contract address to filter by a specific ERC20 token
    contract_address = 0xc944e90c64b2c07662a292be6244bdf05cda44a7  # e.g., '0xdAC17F958D2ee523a2206206994597C13D831ec7' for USDT

    token_transfers = get_erc20_token_transfers(
        address,
        api_key,
        contract_address=contract_address,
        offset=100,
        sort='desc'
    )

    if token_transfers:
        for tx in token_transfers:
            print(f"Token Name: {tx['tokenName']}")
            print(f"Token Symbol: {tx['tokenSymbol']}")
            print(f"Token Decimal: {tx['tokenDecimal']}")
            print(f"Contract Address: {tx['contractAddress']}")
            print(f"From: {tx['from']}")
            print(f"To: {tx['to']}")
            amount = int(tx['value']) / (10 ** int(tx['tokenDecimal']))
            print(f"Value: {amount} {tx['tokenSymbol']}")
            print(f"Transaction Hash: {tx['hash']}")
            print(f"Block Number: {tx['blockNumber']}")
            timestamp = int(tx['timeStamp'])
            readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Timestamp: {readable_time}")
            print('-' * 60)
    else:
        print("No token transfer events found.")
