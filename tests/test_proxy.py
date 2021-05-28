import unittest
import os
import sys
import pytest
import requests

class ProxyrTest(unittest.TestCase):

    def test_app(self):
        response = requests.get("http://localhost:8080/api/buy/index.html")
        assert response.status_code==200

    def test_backend_down(self):
        response = requests.get("http://localhost:8080/api/sellers/index.html")
        assert response.status_code==503

    def test_default(self):
        response = requests.get("http://localhost:8080/")
        assert response.status_code==403
