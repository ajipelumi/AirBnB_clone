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

    def test_show_alternate_syntax_class_and_instance_BaseModel(self):
        """ Test the show command with BaseModel class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.show({output})")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_show_alternate_syntax_class_and_instance_User(self):
        """ Test the show command with User class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.show({output})")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_show_alternate_syntax_class_and_instance_State(self):
        """ Test the show command with State class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"State.show({output})")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_show_alternate_syntax_class_and_instance_City(self):
        """ Test the show command with City class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"City.show({output})")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_show_alternate_syntax_class_and_instance_Amenity(self):
        """ Test the show command with Amenity class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Amenity.show({output})")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_show_alternate_syntax_class_and_instance_Place(self):
        """ Test the show command with Place class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Place.show({output})")
            self.assertNotEqual("** no instance found **\n", f.getvalue())

    def test_show_alternate_syntax_class_and_instance_Review(self):
        """ Test the show command with Review class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Review.show({output})")
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

    def test_destroy_BaseModel_class_and_instance(self):
        """ Test the destroy command with BaseModel class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_User_class_and_instance(self):
        """ Test the destroy command with User class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_City_class_and_instance(self):
        """ Test the destroy command with City class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"City.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_State_class_and_instance(self):
        """ Test the destroy command with State class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"State.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_Place_class_and_instance(self):
        """ Test the destroy command with Place class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Place.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_Amenity_class_and_instance(self):
        """ Test the destroy command with Amenity class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Amenity.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy_Review_class_and_instance(self):
        """ Test the destroy command with Review class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Review.destroy({output})")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review {output}")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_all_nonexistent_class(self):
        """ Test the all command with a nonexistent class. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all DontExist")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_all_valid_BaseModel(self):
        """ Test the all command with a valid class BaseModel. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_all_alternate_valid_BaseModel(self):
        """ Test the all command with a valid class BaseModel. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("BaseModel.all()")
            self.assertIn("BaseModel", f.getvalue())

    def test_all_alternate_valid_Review(self):
        """ Test the all command with a valid class Review. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.console.onecmd("Review.all()")
            self.assertIn("Review", f.getvalue())

    def test_all_alternate_valid_User(self):
        """ Test the all command with a valid class User. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("User.all()")
            self.assertIn("User", f.getvalue())

    def test_all_alternate_valid_State(self):
        """ Test the all command with a valid class State. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.console.onecmd("State.all()")
            self.assertIn("State", f.getvalue())

    def test_all_alternate_valid_City(self):
        """ Test the all command with a valid class City. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.console.onecmd("City.all()")
            self.assertIn("City", f.getvalue())

    def test_all_alternate_valid_Amenity(self):
        """ Test the all command with a valid class Amenity. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.console.onecmd("Amenity.all()")
            self.assertIn("Amenity", f.getvalue())

    def test_all_alternate_valid_Place(self):
        """ Test the all command with a valid class Place. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.console.onecmd("Place.all()")
            self.assertIn("Place", f.getvalue())

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

    def test_update_BaseModel_class_and_instance(self):
        """ Test the update command with BaseModel class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_update_User_class_and_instance(self):
        """ Test the update command with User class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_update_State_class_and_instance(self):
        """ Test the update command with State class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"State.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show State {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_update_City_class_and_instance(self):
        """ Test the update command with City class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"City.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show City {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_update_Place_class_and_instance(self):
        """ Test the update command with Place class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Place.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show Place {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_update_Amenity_class_and_instance(self):
        """ Test the update command with Amenity class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Amenity.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show Amenity {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_update_Review_class_and_instance(self):
        """ Test the update command with Review class and instance. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"Review.update({output} 'name' 'Mike')")
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show Review {output}")
            self.assertIn("name", f.getvalue())
            self.assertIn("Mike", f.getvalue())

    def test_count_BaseModel(self):
        """ Test the count command with a valid class BaseModel. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            self.assertEqual("3\n", f.getvalue())

    def test_count_User(self):
        """ Test the count command with a valid class User. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertEqual("2\n", f.getvalue())

    def test_count_State(self):
        """ Test the count command with a valid class State. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.count()")
            self.assertEqual("2\n", f.getvalue())

    def test_count_Place(self):
        """ Test the count command with a valid class Place. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.count()")
            self.assertEqual("2\n", f.getvalue())

    def test_count_City(self):
        """ Test the count command with a valid class City. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.count()")
            self.assertEqual("2\n", f.getvalue())

    def test_count_Amenity(self):
        """ Test the count command with a valid class Amenity. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity.count()")
            self.assertEqual("2\n", f.getvalue())

    def test_count_Review(self):
        """ Test the count command with a valid class Review. """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review.count()")
            self.assertEqual("2\n", f.getvalue())

            
if __name__ == '__main__':
    unittest.main()
