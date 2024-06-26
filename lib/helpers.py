# lib/helpers.py
from models.task import Task
from models.person import Person
from models.__init__ import CONN, CURSOR

def view_people():
    people = Person.get_all()
    print("\nDisplaying people...")
    print("-"*60)
    i = 1
    for person in people:
        print(f"{i}. {person.name}")
        i += 1

def view_tasks():
    tasks = Task.get_all()
    print("\nDisplaying Tasks...")
    print("-"*60)
    i = 1
    for task in tasks:
        print(f"{i}. {task}")
        i += 1

def view_task_details(task_number):
    sql = """

        Select * from tasks where id is ?
        """
    # task = Task.find_by_id((int(task_number)-1))
    # tasks = Task.get_all()
    # task = tasks[int(task_number)-1]
    try:
        row = CURSOR.execute(sql, (task_number,)).fetchone()
        task = Task.instance_from_db(row)
        print(f"\nTask: {task.task}, Due Date: {task.due_date}, Person Id: {task.person_id}")
    except Exception as exc:
        print("error retrieving task", exc)

def view_by_number(choice):
    sql = """
        Select * from People where id is ?
      """

    try:
        row = CURSOR.execute(sql, (choice,)).fetchone()
        person = Person.instance_from_db(row)
        tasks = person.tasks()
        i = 1
        print(f"\n{person.name}'s Tasks:")
        print("-"*60)
        for task in tasks:
            print(f"{i}. Task: {task.task}, Due Date: {task.due_date}") 
            i += 1
    except Exception as exc:
        print("error retrieving task", exc)
    # try:
    #     # person = Person.find_by_id((int(choice)-1))


    #     people = Person.get_all()
    #     person = people[int(choice)-1]
        
    #     tasks = person.tasks()
    #     i = 1
    #     print(f"\n{person.name}'s Tasks:")
    #     print("-"*60)
    #     for task in tasks:
    #         print(f"{i}. Task: {task.task}, Due Date: {task.due_date}") 
    #         i += 1
    # except Exception as exc:
    #     print("\nError retrieving task", exc)    

def add_task(choice):

    people = Person.get_all()
    person = people[int(choice)-1]
    # person = Person.find_by_id((int(choice)-1))
    task = input("\nPlease enter task name: ")
    due_date = input("\nPlease enter task due_date in the following format 'mm-dd-yyyy': ")
    try:
        Task.create(task, due_date, person.id)
        print("\nTask succesfully added")
    except Exception as exc:
        print("\nError creating new task", exc)
                 
def manage_task(task_number, person_number):

    people = Person.get_all()
    person = people[int(person_number)-1]
    tasks = person.tasks()

    if tasks and int(task_number) in range(1,(len(tasks))):
        task_action = input("\nType 'u' to update task or 'd' to delete: ")
        task = tasks[int(task_number)-1]

        if task_action == "u":
    
            print(f"\nTask: {task.task}, Due Date: {task.due_date}")
            updated_task = input("\nPlease enter an updated task or hit enter to leave as is: ")
            updated_duedate = input("\nPlease enter an updated due-date in the following format 'mm-dd-yyyy' or hit enter to leave as is: " )
                
            try:
                if updated_task == "" and len(updated_duedate):
                    task.due_date = updated_duedate
                elif updated_duedate == "" and len(updated_task):
                    task.task = updated_task
                elif len(updated_task) and len(updated_duedate):
                    task.task = updated_task
                    task.due_date = updated_duedate
                task.update()
                print("\nTask updated succesfully")
            except Exception as exc:
                    print("\nError creating new task ", exc)
                        
        elif task_action == "d":   
            try:
                task.delete()
                print("\nTask deleted succesfully")
            except Exception as exc:
                print("\nError deleting task ", exc)
        else:
            print("\nInvalid input")
    else:
        print("\nInvalid task number")
      
            

def find_by_person_id(personid):
    person = Person.find_by_id(personid)
    
    tasks = person.tasks()
    if tasks:
        print(f"\n{person.name}'s Tasks: ")
        print("-"*60)
        i = 1
        for task in tasks:
            print(f"{i}. Task: {task.task}, Due Date: {task.due_date}")
            i += 1
    
          
def find_by_task_id(task_id):
    task = Task.find_by_id(task_id)
    print(f"\nTask: {task.task}, Due Date: {task.due_date}")  

def add_person():
    person_name = input("\nPlease enter person name: ")
    try:
        Person.create(person_name)
        print("\nPerson created succesfully")
    except Exception as exc:
        print("\nError creating person ", exc )


def delete_person(person_number):
    people = Person.get_all()
    person = people[int(person_number)-1]

    try: 
        tasks = person.tasks()
        for task in tasks:
            task.delete()
        person.delete()
        print("\nPerson deleted succesfully")
    except Exception as exc:
        print("\nError deleting person, ", exc)
      
def exit_program():
    print("\nGoodbye!")
    exit()
