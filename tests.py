from app import app
from api import errorFields, rateLimitedFields, usedFields
from typing import Final
from unittest import main as entrypoint, TestCase
from time import sleep as timeout

# Test Case Constant Variables (w/ Types)
IpAddress = str
RestContext = str

INVALID_SPECIFIC_IP_ADDRESS: Final[IpAddress] = "142askdopewqipo" # This is just a random.
VALID_SPECIFIC_IP_ADDRESS: Final[IpAddress] = "142.250.204.110" # Just a google test ping IP.
HTTP_OKAY: Final[int] = 200

class IPTests(TestCase):
    def setUp(self):
        self.instance = app.test_client()

    def test_get_own_ip(self):
        timeout(1)
        resp_own_ip = self.instance.get("/")
        self.assertTrue(HTTP_OKAY, resp_own_ip.status_code)

    def test_assert_specific_ip(self):
        timeout(2)
        resp_req_specific_ip = self.instance.get("/", data={"ip_address": VALID_SPECIFIC_IP_ADDRESS})
        self.assertTrue(HTTP_OKAY, resp_req_specific_ip.status_code)

    def test_get_okay_invalid_ip(self):
        timeout(3)
        resp_invalid_ip  = self.instance.get("/", data={"ip_address": INVALID_SPECIFIC_IP_ADDRESS})
        self.assertTrue(HTTP_OKAY, resp_invalid_ip.status_code)

if __name__ == "__main__":
    entrypoint()

