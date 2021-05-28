import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from docker import Docker

class DockerTest(unittest.TestCase):

    D1=Docker()
    D2=Docker()

    def test_type(self):
        assert type(DockerTest.D1)==type(DockerTest.D2)

    def test_backend_exists(self):
        assert DockerTest.D1.backend_exists("buy",[{"name":"buy"}])==True

    def test_backend_not_exists(self):
        assert DockerTest.D1.backend_exists("sell",[{"name":"buy"}])==False

    def test_select_backend(self):
        assert DockerTest.D1.select_backend("sell")=="backend Doesn't Exits"

    def test_run_service(self):
        assert DockerTest.D1.run_service("sell")=="Service Execution has Errors"

    def test_stop_service(self):
        assert DockerTest.D1.stop_service("sell")=="Service Execution has Errors"
