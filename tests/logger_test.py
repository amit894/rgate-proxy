import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from logger import Logger


class LoggerTest(unittest.TestCase):

    L1=Logger()
    L2=Logger()

    def test_type(self):
        assert type(LoggerTest.L1)==type(LoggerTest.L2)
