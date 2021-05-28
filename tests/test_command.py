import unittest
import os
import sys

sys.path.append(os.path.join("../", "src"))
from command import Command

class CommandTest(unittest.TestCase):

    C1=Command()
    C2=Command()

    def test_type(self):
        assert type(CommandTest.C1)==type(CommandTest.C2)

    def test_cmd_no_arg(self):
        try:
            CommandTest.C1.run_command()
        except TypeError as err:
            assert err,"run_command() missing 2 required positional arguments: 'cmd' and 'args'"

    def test_cmd_one_arg(self):
        try:
            CommandTest.C1.run_command("test")
        except TypeError as err:
            assert err,"run_command() missing 2 required positional arguments: 'cmd' and 'args'"


    def test_cmd_two_arg(self):
            assert "..0",CommandTest.C1.run_command("tail","-f amit")

    def test_cmd_output_no_arg(self):
        try:
            CommandTest.C1.run_command_output()
        except TypeError as err:
            print("Error")
            assert err,"run_command() missing 2 required positional arguments: 'cmd' and 'args'"

    def test_cmd_output_one_arg(self):
        try:
            CommandTest.C1.run_command_output("test")
        except TypeError as err:
            assert err,"run_command() missing 2 required positional arguments: 'cmd' and 'args'"


    def test_cmd_output_two_arg(self):
            assert "0",CommandTest.C1.run_command_output("test","amit")
