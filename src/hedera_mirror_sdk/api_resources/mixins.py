import json
from urllib.parse import urlencode

def create_params(**kwargs):
    '''
    Used to create url parameters for API call
    '''
    url = kwargs.get("url")
    params = kwargs.get("params")
    if params:
        query_string = urlencode(eval(params))
    return f'{url}?{query_string}'


class PathBuilder:

    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.domain = kwargs.get('domain')
        self.version = kwargs.get('version')
        self.profile_id = kwargs.get("profile_id")
        self.domain_id = kwargs.get("domain_id")
        self.domain_action = kwargs.get("domain_action")
        self.params = kwargs.get('params')
        

    def build(self):
        paths = {
            "domains":{
                "account": {
                    "path": f'{self.version}/accounts',
                    "name": None
                },
                "transaction": {
                    "path": f'{self.version}/transactions',
                    "name": None
                },
                "topic": {
                    "path": f'{self.version}/topics',
                    "name": None
                },
                "token": {
                    "path": f'{self.version}/tokens',
                    "name": None
                },
                "schedule_transaction": {
                    "path": f'{self.version}/schedule_transactions',
                    "name": None
                },
                "smart_contract": {
                    "path": f'{self.version}/smart_contracts',
                    "name": None
                },
                "block": {
                    "path": f'{self.version}/blocks',
                    "name": None
                },
                "state_proof_alpha": {
                    "path": f'{self.version}/state_proof_alpha',
                    "name": None
                },
                "network": {
                    "path": f'{self.version}/network',
                    "name": None
                },
            }

        }
        domain_info = paths['domains'][self.domain]
        sections = [domain_info['path']]
        if self.profile_id:
            sections.append(self.profile_id)
        if domain_info["name"]:
            sections.append(domain_info["name"])
            if self.domain_id:
                sections.append(self.domain_id)
                if self.domain_action:
                    sections.append(self.domain_action)
        
        path = f'/{"/".join(sections)}'
        url = f'{self.base_url}{path}'
        
        #manage params and filtering
        params = {}
        operators = ["e", "lt", "lte", "gt", "gte"]
        for param in self.params.keys():
            if param in operators:
                params['account.id'] = f'{param}:{self.params[param]}'
            else:
                params[param] = self.params[param]
        if params:
            url = create_params(params=json.dumps(params), url=url)

        return [path, url]