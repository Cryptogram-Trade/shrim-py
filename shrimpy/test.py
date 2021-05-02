from unittest import TestCase
from . import ShrimpyClient


class TestClient(TestCase):

    def setUp(self):
        self.client = ShrimpyClient("mykey", "mysecret")

    def test_constructed_client(self):
        self.assertEqual(self.client.url, "https://api.shrimpy.io/v1/")

    def test_response_is_json(self):
        response = self.client.get("bittrex/ticker")
        self.assertIsInstance(response, list)
        self.assertIn('priceUsd', response[0].keys())

    def test_headers_are_included(self):
        self.assertEqual(self.client.auth_provider.api_key, "mykey")
        self.assertEqual(self.client.auth_provider.secret_key, "mysecret")
        self.assertTrue(10**12 < self.client.auth_provider.last_nonce < 10**13)

