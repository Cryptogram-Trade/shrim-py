import hmac
import hashlib
import time
import base64
import threading
import json
from urllib.parse import urlencode

import requests
from requests.auth import AuthBase


class AuthProvider(AuthBase):
    def __init__(self, api_key, secret_key, version):
        self.api_key = api_key
        self.secret_key = secret_key
        self.nonce_lock = threading.Lock()
        self.last_nonce = int(time.time() *  1000)
        self.version = version


    def __call__(self, request):
        nonce = self._get_nonce()
        message = ''.join([request.path_url, request.method, str(nonce), (request.body or '')])
        headers = get_auth_headers(self.version, nonce, message, self.api_key, self.secret_key)
        request.headers.update(headers)

        return request

    def _get_nonce(self):
        new_nonce = int(time.time() *  1000)
        with self.nonce_lock:
            if (new_nonce <= self.last_nonce):
                new_nonce = new_nonce + 1

            self.last_nonce = new_nonce

        return new_nonce
    

def get_auth_headers(version, timestamp, message, api_key, secret_key):
    message = message.encode('ascii')
    hmac_key = base64.b64decode(secret_key)
    signature = hmac.new(hmac_key, message, hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
    header_prefix = "DEV-" if version == "dev" else ""

    return {
        'Content-Type': 'application/json',
        f'{header_prefix}SHRIMPY-API-KEY': api_key,
        f'{header_prefix}SHRIMPY-API-NONCE': timestamp,
        f'{header_prefix}SHRIMPY-API-SIGNATURE': signature_b64
    }


class BaseShrimpyClient():
    """Authenticated access to the Shrimpy Developer API"""
    version = None

    def __init__(self, key, secret, timeout=300):
        url_prefix = "dev-" if self.version == "dev" else ""
        self.url = f'https://{url_prefix}api.shrimpy.io/v1/'
        self.auth_provider = None
        self.timeout = timeout
        if (key and secret):
            self.auth_provider = AuthProvider(key, secret, self.version)
        self.session = requests.Session()


    def call(self, method, endpoint, params=None, data=None):
        url = self.url + endpoint
        if data is not None:
            data = json.dumps(data)

        api_request = self.session.request(
            method,
            url,
            params=params,
            data=data,
            auth=self.auth_provider,
            timeout=self.timeout
        )

        return api_request.json()
    
    def get(self, *args, **kwargs):
        return self.call('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.call('POST', *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.call('DELETE', *args, **kwargs)

    def _create_query_string(self, endpoint, params):
        return endpoint + '?' + urlencode(params)

    def _add_param_or_ignore(self, params, key, value):
        if value is not None:
            params[key] = value


class ShrimpyDevClient(BaseShrimpyClient):
    version = "dev"


class ShrimpyUserClient(BaseShrimpyClient):
    version = "user"