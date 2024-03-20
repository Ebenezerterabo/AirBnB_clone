#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ This class represents the console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quits the program """
        return True

    def help_quit(self):
        """ heelp"""
        print("Exit the program")

    def help_EOF(self):
        """ EOF """
        print("Exit the program ")

    def emptyline(self):
        """ Do nothing """
        pass

    def do_create(self, arg):
        """ creates an instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            NewBaseModel = eval(arg.split()[0])()
            NewBaseModel.save()
            print(NewBaseModel.id)
        except Exception:
            print("** class doesn't exist **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
