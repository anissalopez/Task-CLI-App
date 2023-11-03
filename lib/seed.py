from models.person import Person
from models.task import Task 


def seed():

    Person.drop_table()
    Task.drop_table()
    Person.create_table()
    Task.create_table()

    anissa = Person.create("Anissa")
    darby = Person.create("Darby")
    nikki = Person.create("Nikki")

    laundry = Task.create("laundry", "10-30-2023", anissa.id)
    phase3_project = Task.create("phase 3 project", "10-30-2023", anissa.id)
    dishes = Task.create("dishes", "10-20-2023", anissa.id)

    laundry = Task.create("laundry", "10-30-2023", darby.id)
    phase3_project = Task.create("phase 3 project", "10-30-2023", darby.id)
    dishes = Task.create("dishes", "10-20-2023", darby.id)

    laundry = Task.create("laundry", "10-30-2023", nikki.id)
    phase3_project = Task.create("phase 3 project", "10-30-2023", nikki.id)
    dishes = Task.create("dishes", "10-20-2023", nikki.id)

seed()
print("seeded database")








