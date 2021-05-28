import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from config import Config

class ConfigTest(unittest.TestCase):

    C1=Config()
    C2=Config()

    def test_type(self):
        assert type(ConfigTest.C1)==type(ConfigTest.C2)
