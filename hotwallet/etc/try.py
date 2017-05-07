import requests
import json


def main():
    url = "http://localhost:6970"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "getbalance",
        # "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print response

if __name__ == "__main__":
    main()
