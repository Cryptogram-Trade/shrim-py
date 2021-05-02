from unittest import TestCase
from . import ShrimpyDevClient, ShrimpyUserClient


class TestShrimpyDevClient(TestCase):

    def setUp(self):
        self.client = ShrimpyDevClient("mykey", "mysecret")

    def test_response_is_json(self):
        response = self.client.get("bittrex/ticker")
        self.assertIsInstance(response, list)
        self.assertIn('priceUsd', response[0].keys())

    def test_headers_are_included(self):
        self.assertEqual(self.client.auth_provider.api_key, "mykey")
        self.assertEqual(self.client.auth_provider.secret_key, "mysecret")
        self.assertTrue(10**12 < self.client.auth_provider.last_nonce < 10**13)

    def test_client_connects_to_dev_api(self):
        self.assertEqual(self.client.url, "https://dev-api.shrimpy.io/v1/")
        self.assertEqual(self.client.auth_provider.version, "dev")


class TestShrimpyUserClient(TestCase):

    def setUp(self):
        self.client = ShrimpyUserClient("mykey", "mysecret")

    def test_client_for_user_api(self):
        self.assertEqual(self.client.url, "https://api.shrimpy.io/v1/")
        self.assertEqual(self.client.auth_provider.version, "user")