from models .__init__ import CONN, CURSOR 
from models.person import Person
from models.toDo import ToDo 


def seed():

    Person.drop_table()
    ToDo.drop_table()
    Person.create_table()
    ToDo.create_table()

    anissa = Person.create("Anissa")
    darby = Person.create("Darby")
    nikki = Person.create("Nikki")

    laundry = ToDo.create("laundry", "10-30-2023", anissa.id)
    phase3_project = ToDo.create("phase 3 project", "10-30-2023", anissa.id)
    dishes = ToDo.create("dishes", "10-20-2023", anissa.id)

    laundry = ToDo.create("laundry", "10-30-2023", darby.id)
    phase3_project = ToDo.create("phase 3 project", "10-30-2023", darby.id)
    dishes = ToDo.create("dishes", "10-20-2023", darby.id)

    laundry = ToDo.create("laundry", "10-30-2023", nikki.id)
    phase3_project = ToDo.create("phase 3 project", "10-30-2023", nikki.id)
    dishes = ToDo.create("dishes", "10-20-2023", nikki.id)

seed()
print("seeded database")








