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

    def do_destroy(self, arg):
        """
        Deletes an instance
        syntax: destroy <class name> <id>
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
            flag = 0  # Tracks item deletion
            key_to_delete = ""

            # Iterate through objects
            for obj_id in obj.keys():

                # If key is found
                if obj_id == key:
                    key_to_delete = key  # Store the key

            # Check for key_to_delete
            if key_to_delete:
                del obj[key_to_delete]
                flag = 1  # Indicates that item has been deleted

            # The instance does not exist as key is not found
            if flag == 0:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        syntax: all <class name> or all
        """
        # If class name does not exist
        if arg and arg not in self.class_names:
            print("** class doesn't exist **")

        else:
            all_instance = []  # List to store instance
            all_objs = storage.all()  # Get the instances

            # If no class name
            if not arg:

                # Iterate through objects
                for key in all_objs.keys():

                    # Append each instance to list (cast as string)
                    all_instance.append(str(all_objs[key]))

                print(all_instance)  # Print list

            # Valid class name is entered
            if arg and arg in self.class_names:

                # Iterate through objects
                for key in all_objs.keys():

                    obj = all_objs[key]  # Get instance

                    # Check if instance class name is argument passed
                    if obj.__class__.__name__ == arg:

                        # Append each instance to list (cast as string)
                        all_instance.append(str(obj))

                print(all_instance)  # Print list

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file).
        syntax: update <class name> <id> <attribute name> "<attribute value>"
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
            key = f'{args[0]}.{args[1]}'  # Store key to access obj_to_update
            obj = storage.all()  # Load all objects into memory
            obj_to_update = ""

            # Iterate through objects
            for obj_id in obj.keys():

                # If key is found
                if obj_id == key:
                    obj_to_update = obj[key]  # Get obj_to_update

            # If instance of class name to be updated is not found
            if not obj_to_update:
                print("** no instance found **")

            # If attribute name is missing
            elif len(args) == 2:
                print("** attribute name missing **")

            # If attribute value is missing
            elif len(args) == 3:
                print("** value missing **")

            # All arguments passed
            else:

                # Cast attribute value to type
                try:

                    # Check if value is an int
                    attr_value = int(args[3])

                except ValueError:

                    try:

                        # Check if value is a float
                        attr_value = float(args[3])

                    except ValueError:

                        # Value can only be a string
                        attr_value = args[3].strip("'\"")

                # Add or Update item in object
                setattr(obj_to_update, args[2], attr_value)

                # Save change to JSON file
                obj_to_update.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
