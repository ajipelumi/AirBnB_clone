#!/usr/bin/python3
""" Console Test Module. """
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import unittest
import sys


class TestHBNBCommand(unittest.TestCase):
    """ Tests the behaviour of Console. """

    def setUp(self):
        """ Sets up objects and variables. """
        self.console = HBNBCommand()
        self.regex_id = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'

    def test_help(self):
        """ Test the help command """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertTrue(output.startswith("Documented commands"))

    def test_quit(self):
        """ Test the quit command """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF(self):
        """ Test the EOF command """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(f.getvalue(), "\n")

    def test_emptyline(self):
        """ Test the emptyline command. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_missing_class(self):
        """ Test the create command with a missing class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_create_nonexistent_class(self):
        """ Test the create command with a nonexistent class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create DontExist")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_create_valid_class(self):
        """ Test the create command with a valid class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertRegex(f.getvalue(), self.regex_id)

    def test_show_missing_class(self):
        """ Test the show command with a missing class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_show_nonexistent_class(self):
        """ Test the show command with a nonexistent class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show DontExist")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_show_missing_instance(self):
        """ Test the show command with a missing instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_show_nonexistent_instance(self):
        """ Test the show command with a nonexistent instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel DontExist")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_show_valid_class_and_instance(self):
        """ Test the show command with a valid class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {output}")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_destroy_missing_class(self):
        """ Test the destroy command with a missing class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_destroy_nonexistent_class(self):
        """ Test the destroy command with a nonexistent class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy DontExist")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_destroy_missing_instance(self):
        """ Test the destroy command with a missing instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_destroy_nonexistent_instance(self):
        """ Test the destroy command with a nonexistent instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel DontExist")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_valid_class_and_instance(self):
        """ Test the destroy command with a valid class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {output}")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_all_nonexistent_class(self):
        """ Test the all command with a nonexistent class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all DontExist")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_all_valid_class(self):
        """ Test the create command with a valid class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue())
            
    def test_update_missing_class(self):
        """ Test the update command with a missing class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

    def test_update_nonexistent_class(self):
        """ Test the update command with a nonexistent class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update DontExist")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_update_missing_instance(self):
        """ Test the update command with a missing instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

    def test_update_nonexistent_instance(self):
        """ Test the update command with a nonexistent instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel DontExist")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_update_missing_attribute(self):
        """ Test the update command with a missing class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {output}")
            self.assertEqual("** attribute name missing **\n", f.getvalue())

    def test_update_missing_value(self):
        """ Test the update command with a missing class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {output} name")
            self.assertEqual("** value missing **\n", f.getvalue())

    def test_update_valid_class_and_instance(self):
        """ Test the update command with a valid class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {output} name Pelumi")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Pelumi", f.getvalue())

            
if __name__ == '__main__':
    unittest.main()
