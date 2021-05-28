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
        assert True==DockerTest.D1.backend_exists("buy",[{"name":"buy"}])

    def test_backend_not_exists(self):
        assert False==DockerTest.D1.backend_exists("sell",[{"name":"buy"}])

    def test_select_backend(self):
        assert "backend Doesn't Exits"==DockerTest.D1.select_backend("sell")

    def test_run_service(self):
        assert "Service Execution has Errors"==DockerTest.D1.run_service("sell")

    def test_stop_service(self):
        assert "Service Execution has Errors"==DockerTest.D1.stop_service("sell")
