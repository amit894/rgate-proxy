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
        response=RequestsTest.R1.default_response()
        assert "403 FORBIDDEN"==response.status

    def test_get_response(self):
        response=RequestsTest.R1.get_method("api/buy/index.html")
        assert "503 SERVICE UNAVAILABLE"==response.status

    def test_post_response(self):
        response=RequestsTest.R1.post_method("/api/buy/index.html")
        assert "403 FORBIDDEN"==response.status
