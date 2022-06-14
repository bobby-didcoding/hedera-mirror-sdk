import os
from hedera_mirror_sdk.error import APIError
from hedera_mirror_sdk.api_resources.mixins import create_params, PathBuilder
from hedera_mirror_sdk.api_resources.api_requester import APIRequestor
import base64
import hmac
import hashlib
from datetime import datetime
from uuid import uuid4
import json
import requests



class Client(object):
    """ 
    A client for accessing the hedera_mirror_sdk API. 
    """
    
    def __init__(
        self, 
            version=None,
            env=None,
            environ=None
        ):
        """
        Initializes the hedera_mirror_sdk Client
        :param str version: hedera_mirror_sdk version
        :param str env: The environment in which API calls will be made
        :returns: hedera_mirror_sdk Client
        :rtype: hedera_mirror_sdk.rest.Client
        """
        environ = environ or os.environ
        self.hedera_mirror_sdk_version = version or environ.get('HEDERA_MIRROR_SDK_VERSION')
        self.env = env or environ.get('HEDERA_MIRROR_SDK_ENV')

        base_url = {
            "mainnet": 'https://mainnet-public.mirrornode.hedera.com/api',
            "testnet": 'https://testnet.mirrornode.hedera.com/api',
            "previewnet": "https://previewnet.mirrornode.hedera.com/api/v1/transactions/api"
        }
        try:
            self.base_url = base_url[self.env.strip().lower()]
        except AttributeError:
            raise APIError("Use 'mainnet', 'testnet' or 'previewnet' as env")
        
        # Domains
        self._account = None
        self._transaction = None
        self._topic = None
        self._token = None
        self._schedule_transaction = None
        self._smart_contract = None
        self._block = None
        self._state_proof_alpha = None
        self._network = None


    def request(self, method, base_url, domain, version, profile_id=None, domain_id=None, domain_action=None, params=None, data=None, headers=None, auth=None):

        headers = headers or {}
        params = params or {}
        method = method.upper()

        path, url = PathBuilder(
            base_url=base_url,
            domain=domain,
            version=version,
            profile_id=profile_id,
            domain_id=domain_id,
            domain_action=domain_action,
            params=params).build()

        print(f'Endpoint (url): \n{url}\n\n')
        api = APIRequestor(url = url)

        if method == "POST":
            response = api.post()
        elif method == "PUT":
            response = api.put()
        elif method == "GET":
            response = api.get()
        elif method == "DELETE":
            response = api.delete()

        if method == "DELETE":
            print(
                f'Response:\nStatus:\n{response.status_code}\nMessage:\nObject deleted'
            )
            json_response = {}
        else:
            print(
                f'Response:\nStatus:\n{response.status_code}\nJson Response:\n{response.json()}'
            )
            json_response = response.json()
        return {
            "status": response.status_code,
            "json": json_response
        }
        
    @property
    def account(self):
        """
        Access the hedera_mirror_sdk Account API
        """
        if self._account is None:
            from hedera_mirror_sdk.rest.account import Account
            self._account = Account(self, self.base_url, 'account',self.hedera_mirror_sdk_version)
        return self._account

    @property
    def transaction(self):
        """
        Access the hedera_mirror_sdk Transaction API
        """
        if self._transaction is None:
            from hedera_mirror_sdk.rest.transaction import Transaction
            self._transaction = Transaction(self, self.base_url, 'transaction',self.hedera_mirror_sdk_version)
        return self._transaction

    @property
    def topic(self):
        """
        Access the hedera_mirror_sdk Topic API
        """
        if self._topic is None:
            from hedera_mirror_sdk.rest.topic import Topic
            self._topic = Topic(self, self.base_url, 'topic',self.hedera_mirror_sdk_version)
        return self._topic

    @property
    def token(self):
        """
        Access the hedera_mirror_sdk Token API
        """
        if self._token is None:
            from hedera_mirror_sdk.rest.token import Token
            self._token = Token(self, self.base_url, 'token',self.hedera_mirror_sdk_version)
        return self._token

    @property
    def schedule_transaction(self):
        """
        Access the hedera_mirror_sdk Schedule Transaction API
        """
        if self._schedule_transaction is None:
            from hedera_mirror_sdk.rest.schedule_transaction import ScheduleTransaction
            self._schedule_transaction = ScheduleTransaction(self, self.base_url, 'schedule_transaction',self.hedera_mirror_sdk_version)
        return self._schedule_transaction

    @property
    def smart_contract(self):
        """
        Access the hedera_mirror_sdk Schedule Transaction API
        """
        if self._smart_contract is None:
            from hedera_mirror_sdk.rest.smart_contract import SmartContract
            self._smart_contract = SmartContract(self, self.base_url, 'smart_contract',self.hedera_mirror_sdk_version)
        return self._smart_contract

    @property
    def block(self):
        """
        Access the hedera_mirror_sdk Schedule Transaction API
        """
        if self._block is None:
            from hedera_mirror_sdk.rest.block import Block
            self._block = Block(self, self.base_url, 'block',self.hedera_mirror_sdk_version)
        return self._block

    @property
    def state_proof_alpha(self):
        """
        Access the hedera_mirror_sdk Schedule Transaction API
        """
        if self._state_proof_alpha is None:
            from hedera_mirror_sdk.rest.state_proof_alpha import StateProofAlpha
            self._state_proof_alpha = StateProofAlpha(self, self.base_url, 'state_proof_alpha',self.hedera_mirror_sdk_version)
        return self._state_proof_alpha

    @property
    def network(self):
        """
        Access the hedera_mirror_sdk Schedule Transaction API
        """
        if self._network is None:
            from hedera_mirror_sdk.rest.network import Network
            self._network = Network(self, self.base_url, 'network',self.hedera_mirror_sdk_version)
        return self._network