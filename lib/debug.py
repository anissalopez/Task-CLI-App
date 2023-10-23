#!/usr/bin/env python3
# lib/debug.py


from models.__init__ import CONN, CURSOR
from lib.models.task import ToDo
from models.person import Person
import ipdb

Person.drop_table()
Person.create_table()

ToDo.drop_table()
ToDo.create_table()


newPerson = Person.create("Anissa")
Paul = Person.create("Paul")
Nikki = Person.create("Nikki")
Darby = Person.create("Darby")

Paul.delete()


laundry = ToDo.create("laundry", "10-24-2023", 1)
taxes = ToDo.create("taxes", "01-12-2023", 1)
taxes = ToDo("taxes", "01-12-2023", 1)
