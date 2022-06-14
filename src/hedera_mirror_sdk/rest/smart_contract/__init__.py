# coding=utf-8

from hedera_mirror_sdk.api_resources.abstract.domain import Domain

class SmartContract(Domain):

    def __init__(self, hedera_mirror_sdk, base_url, domain, version ,**kwargs):
        """
        Initialize the SmartContract Domain
        """
        super(SmartContract, self).__init__(hedera_mirror_sdk)
        self.base_url = base_url
        self.domain = domain
        self.version = version


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<hedera_mirror_sdk.SmartContract>'
