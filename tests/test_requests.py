import os
import sys
import unittest

sys.path.append(os.path.join("../", "src"))
from rgate_requests import RGate_Requests


class RequestsTest(unittest.TestCase):

    R1=RGate_Requests()
    R2=RGate_Requests()

    def test_type(self):
        assert type(RequestsTest.R1)==type(RequestsTest.R2)

    def test_default_response(self):
        response=RequestsTest.R1.get_method("/")
        assert response.status=="403 FORBIDDEN"

    def test_get_response(self):
        response=RequestsTest.R1.get_method("api/buy/index.html")
        assert response.status=="200 OK"

    def test_get_response_503(self):
        response=RequestsTest.R1.get_method("api/sellers/index.html")
        assert response.status=="503 SERVICE UNAVAILABLE"

    def test_post_response(self):
        response=RequestsTest.R1.post_method("/api/buy/index.html")
        assert response.status=="403 FORBIDDEN"
