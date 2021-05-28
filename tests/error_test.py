import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from error import Error


class ErrorTest(unittest.TestCase):

    E1=Error()
    E2=Error()

    def test_type(self):
        assert type(ErrorTest.E1)==type(ErrorTest.E2)
