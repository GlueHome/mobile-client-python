import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class RestClient(object):
    def __init__(self, base_url: str = None, auth: str = None):
        self.client = requests.Session()
        self.client.mount('https://', HTTPAdapter(max_retries=Retry(total=5, backoff_factor=0.5)))
        self.headers = {'Authorization': auth} if auth else {}
        self.base_url = base_url

    def request(self, method: str, url: str, body: dict = None, params: dict = None) -> str:
        url = url if url.startswith('http') else f'{self.base_url}/{url.lstrip("/")}'
        resp = self.client.request(method=method, url=url, json=body, headers=self.headers, params=params)
        resp.raise_for_status()
        return resp.text

    def get(self, url, params=None):
        return self.request('GET', url, params=params)

    def post(self, url, body=None):
        return self.request('POST', url, body)

    def patch(self, url, body):
        return self.request('POST', url, body)
