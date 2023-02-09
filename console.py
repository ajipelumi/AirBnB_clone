#!/usr/bin/python3
""" The Entry Point of the Command Interpreter. """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Command Line Interpreter. """

    # Define custom prompt
    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
