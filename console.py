#!/usr/bin/python3

"""
Module that defines HBNBCommand class.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand : class that set up the command interpreter.
    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        EOF to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
