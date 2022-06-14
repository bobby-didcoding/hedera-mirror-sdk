class Domain(object):
    """
    Abstract class used in each domain/endpoint

    Makes an HTTP request to this domain.
        :param dict params: Query parameters.
        :param object data: The request body.
        :param dict headers: The HTTP headers.
        :param tuple auth: Basic auth tuple of (api_key, secret)
    """
    def __init__(self, hedera_mirror_sdk):
        self.hedera_mirror_sdk = hedera_mirror_sdk


    def get(self, params=None, data=None, headers=None, auth=None, profile_id=None, domain_id=None, domain_action=None):
        return self.hedera_mirror_sdk.request(
            'get',
            self.base_url,
            self.domain,
            self.version,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            profile_id=profile_id,
            domain_id=domain_id,
            domain_action=domain_action
        )


