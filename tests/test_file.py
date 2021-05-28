import os
import sys
import unittest


sys.path.append(os.path.join("../", "src"))
from file import file_read_json
from file import search_key_json
from file import search_key_yaml

class FileTest(unittest.TestCase):

    def test_file_read(self):
        assert (file_read_json("../config/stats.json"))=={'Amit': 'Test'}

    def test_search_json(self):
        assert (search_key_json("buy","../config/docker_path.json"))=='http://localhost:81/'

    def test_search_yaml(self):
        assert (search_key_yaml("default_response","../config.yaml")["status_code"])==403
