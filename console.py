#!/usr/bin/python3

"""
Module that defines HBNBCommand class.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand : class that set up the command interpreter.
    """
    prompt = "(hbnb) "

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

    def do_create(self, acls):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Usage : create acls
        """
        if acls == "":
            print("** class name missing **")
        else:
            try:
                acls = eval(acls)
                inst = acls()
                inst.save()
                print(inst.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance,
        based on the class name and id.
        """
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        acls = args[0]

        try:
            acls = eval(acls)
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]

        storage_dict = storage.all()
        key = acls.__name__ + "." + id
        if key in storage_dict:
            print(storage_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        acls = args[0]

        try:
            acls = eval(acls)
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]

        storage_dict = storage.all()
        key = acls.__name__ + "." + id
        if key in storage_dict:
            del storage_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, acls):
        """
        Prints all string representation of all instances,
        based or not on the class name.
        """
        if acls:
            try:
                acls = eval(acls)
            except NameError:
                print("** class doesn't exist **")
                return

            storage_dict = storage.all()
            to_print = []
            for key in storage_dict:
                if key[:len(acls.__name__)] == acls.__name__:
                    to_print.append(str(storage_dict[key]))
        else:
            storage_dict = storage.all()
            to_print = []
            for key in storage_dict:
                to_print.append(str(storage_dict[key]))

        print(to_print)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id,
        by adding or updating attribute
        """
        args = line.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        acls = args[0]

        try:
            acls = eval(acls)
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        id = args[1]
        storage_dict = storage.all()
        key = acls.__name__ + "." + id
        if key not in storage_dict:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr = args[2]

        if len(args) < 4:
            print("** value missing **")
            return
        val = eval(args[3])

        obj = storage_dict[key]
        obj.__dict__[attr] = val
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
