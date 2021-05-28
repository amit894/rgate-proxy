import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from deployer import Deployer
from config import Config
from docker import Docker

class DeployTest(unittest.TestCase):

    D1=Deployer(Config(),Docker())
    D2=Deployer(Config(),Docker())


    def test_type(self):
        assert type(DeployTest.D1)==type(DeployTest.D2)

    def test_deploy_rgate(self):
        DeployTest.D1.read_config()
        assert None==(DeployTest.D1.deploy_rgate())

    def test_get_compose_config(self):
        assert "../config/docker-compose.yml"==DeployTest.D1.get_compose_config()

    def test_stop_rgate(self):
        assert None==(DeployTest.D1.stop_rgate())

    def test_config_map(self):
        DeployTest.D1.read_config()
        DeployTest.D1.create_backend_map()
