import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from stats import Stats


class StatsTest(unittest.TestCase):

    S1=Stats()
    S2=Stats()
    D={}

    def test_type(self):
        assert type(StatsTest.S1)==type(StatsTest.S2)

    def test_proxy(self):
        assert type(Stats.get_proxy_stats())==type(StatsTest.D)
