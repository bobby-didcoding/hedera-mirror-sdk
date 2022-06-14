# Hedera Mirror Node Python SDK

Welcome to this Python SDK repository for the Hedera mirror node API.

This is a simple library to facilitate the usage of the Hedera mirror node API.

```
>>> from hedera_mirror_sdk.rest import Client
>>> client = Client(version="v1", env="testnet")
>>> accounts = client.account.get()
>>> accounts["status"]
200
>>> accounts["json"]
{'accounts': [{'account': '0.0....}
```

## Supported Python Versions
This library supports the following Python implementations:

Python 3.6
Python 3.7
Python 3.8
Python 3.9
Python 3.10

## Installation
You can clone the project down from github
```
git clone git@github.com:bobby-didcoding/hedera-mirror-sdk.git
```

hedera_mirror_sdk is available on PyPI: 
```
python -m pip install hedera_mirror_sdk
```

## More about Hedera
Hedera Mirror Nodes store the history of transactions that occurred on mainnet, testnet, and previewnet. Each transaction generates a record that is stored in a record file. The transaction contents can be accessed by the mirror node Rest APIs

Read more <a href="https://docs.hedera.com/guides/docs/mirror-node-api/rest-api" target="_blank">here</a>