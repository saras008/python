import requests

def get_normal_transactions(address, api_key, startblock=0, endblock=99999999, page=1, offset=10, sort='asc'):
    """
    Fetches normal transactions for a given Ethereum address using the Etherscan API.

    Parameters:
        address (str): Ethereum address to query.
        api_key (str): Your Etherscan API key.
        startblock (int): Starting block number (default is 0).
        endblock (int): Ending block number (default is 99999999).
        page (int): Page number for pagination (default is 1).
        offset (int): Number of transactions per page (default is 10).
        sort (str): Sort order: 'asc' or 'desc' (default is 'asc').

    Returns:
        list: A list of transaction dictionaries.
    """
    url = 'https://api.etherscan.io/api'
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'startblock': startblock,
        'endblock': endblock,
        'page': page,
        'offset': offset,
        'sort': sort,
        'apikey': api_key
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == '1':
            transactions = data['result']
            return transactions
        elif data['status'] == '0' and data['message'] == 'No transactions found':
            print('No transactions found for this address.')
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
    address = '0xDe3258C1C45a557F4924d1E4e3d0A4E5341607Ee'
    api_key = '9ZUCWCDSQ5E521UR5PCSBXFNHNAZCICYYB'

    transactions = get_normal_transactions(address, api_key, offset=100, sort='desc')

    if transactions:
        for tx in transactions:
            print(f"Hash: {tx['hash']}")
            print(f"From: {tx['from']}")
            print(f"To: {tx['to']}")
            print(f"Value: {int(tx['value']) / 1e18} ETH")
            print(f"Block Number: {tx['blockNumber']}")
            print(f"Timestamp: {tx['timeStamp']}")
            print('-' * 60)
