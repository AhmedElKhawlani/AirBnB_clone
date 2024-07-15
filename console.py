#!/usr/bin/python3

"""
Module that defines HBNBCommand class.
"""

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
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
            print("** no instance found **")
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

    def do_count(self, acls):
        if acls:
            try:
                acls = eval(acls)
            except NameError:
                print("** class doesn't exist **")
                return

            storage_dict = storage.all()
            counter = 0
            for key in storage_dict:
                if key[:len(acls.__name__)] == acls.__name__:
                    counter += 1
            print(counter)
        else:
            print(len(storage.all()))

    def default(self, line):
        if line[-6:] == ".all()":
            self.do_all(line[:-6])
        elif line[-8:] == ".count()":
            self.do_count(line[:-8])
        elif "." in line and line.count(".") == 1:
            line = line.split(".")
            command = line[-1]
            i = command.index('(')
            j = command.index(')')
            do = command[:i]
            between = command[i + 1: j]
            arg = line[0]
            if do == 'show':
                self.do_show(arg + " " + between)
            elif do == 'destroy':
                self.do_destroy(arg + " " + between)
            elif do == 'update' and '{' not in between:
                splitted = between.split(',')
                for i in range(len(splitted) - 1):
                    splitted[i] = eval(splitted[i])
                ide, name, val = splitted
                self.do_update(arg + ' ' + ide + ' ' + name + ' ' + val)
            elif do == 'update':
                splitted = between.split(',')
                for i in range(len(splitted)):
                    splitted[i] = eval(splitted[i])
                D = splitted[-1]
                ide = splitted[0]
                for key in D:
                     li = arg + ' ' + ide + ' ' + str(key) + ' ' + str(D[key])
                     self.do_update(li)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
