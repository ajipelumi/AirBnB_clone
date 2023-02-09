#!/usr/bin/python3
""" The Entry Point of the Command Interpreter. """
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Command Line Interpreter. """

    # Define custom prompt
    prompt = "(hbnb) "

    # Create dictionary to store class names
    class_names = {
            "BaseModel": BaseModel,
    }

    def emptyline(self):
        """
        Method is called when an empty line is entered
        in response to the prompt.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        syntax: quit
        """
        sys.exit(0)

    def do_EOF(self, arg):
        """
        End-of-file (EOF) command.
        Press Ctrl-D to signal EOF/
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel.
        syntax: create <class name>
        """
        # If class name is missing
        if not arg:
            print("** class name missing **")

        # If class name does not exist
        elif arg not in self.class_names:
            print("** class doesn't exist **")

        # If class name is present
        else:
            cls = self.class_names[arg]  # Get the class
            obj = cls()  # Create instance
            obj.save()  # Save instance to JSON file
            print(obj.id)  # Print the instance id

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        syntax: show <class name> <id>
        """
        # Split into arguments
        args = arg.split()

        # If class name is missing
        if len(args) == 0:
            print("** class name missing **")

        # If class name does not exist
        elif args[0] not in self.class_names:
            print("** class doesn't exist **")

        # If id is missing
        elif len(args) == 1:
            print("** instance id missing **")

        else:
            key = f'{args[0]}.{args[1]}'  # Store key to access value
            obj = storage.all()  # Load all objects into memory
            value = ""

            # Iterate through objects
            for obj_id in obj.keys():

                # If key is found
                if obj_id == key:
                    value = obj[key]  # Get value
                    print(value)  # Print value

            if not value:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
