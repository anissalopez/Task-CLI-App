# lib/helpers.py
from models.task import Task
from models.person import Person

def view_people():
    people = Person.get_all()
    print("\nDisplaying people...")
    for i in range(len(people)):
        print(f"\n{i+1}. {people[i].name}")


def view_tasks():
    tasks = Task.get_all()
    print("\nDisplaying Tasks...")
    for i in range(len(tasks)):
        print(f"\n{i+1}. {tasks[i].task}")

    

def view_task_details(task_number):
    tasks = Task.get_all()
    task = tasks[int(task_number)-1]
    print(f"\nTask: {task.task}, Due Date: {task.due_date}, Person Id: {task.person_id}")

def delete_task(task_number):
    confirmation = input("Please enter 'd' to confirm: ")
    tasks = Task.get_all()
    if confirmation == 'd':
        task = tasks[int(task_number)-1]
        try:
            task.delete()
            print("\ntask deleted succesfully")
        except Exception as exc:
            print("\nError deleting task", exc)
            print("-" * 60)
 
  
def view_by_number(choice):
    try:
        people = Person.get_all()
        person = people[int(choice)-1]
        
        tasks = person.tasks()

        print("-" * 60)
        print(f"\n{person.name}'s Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. Task: {tasks[i].task}, Due Date: {tasks[i].due_date}")
        print("\n")
        print("-" * 60)   
    except Exception as exc:
        print("Error retrieving task", exc)
    
     
        

def add_task(choice):
    people = Person.get_all()
    person = people[int(choice)-1]
    task = input("Please enter task name: ")
    due_date = input("Please enter task due_date in the following format 'mm-dd-yyyy': ")
    try:
        new_task = Task.create(task, due_date, person.id)
        print("\nTask succesfully added")
        print("-" * 60)
    except Exception as exc:
        print("\nError creating new task", exc)
        print("-" * 60)
 
                     
def manage_task(task_number, person_number):
    people = Person.get_all()
    person = people[int(person_number)-1]
    tasks = person.tasks()

    if tasks and int(task_number) in range(1,(len(tasks)+1)):
        task_action = input("Type 'u' to update task or 'd' to delete: ")
        task = tasks[int(task_number)-1]

        if task_action == "u":
            
            print("")
            print(f"Task: {task.task}, Due Date: {task.due_date}")
            updated_task = input("Please enter an updated task or hit enter to leave as is: ")
            updated_duedate = input("Please enter an updated due-date in the following format 'mm-dd-yyyy' or hit enter to leave as is: " )
            
            try:
                if updated_task == "" and len(updated_duedate):
                    task.due_date = updated_duedate
                elif updated_duedate == "" and len(updated_task):
                    task.task = updated_task
                elif len(updated_task) and len(updated_duedate):
                    task.task = updated_task
                    task.due_date = updated_duedate
                task.update()
                print("")
                print("Task updated succesfully")
                print("-" * 60)
            except Exception as exc:
                    print("")
                    print("Error creating new task ", exc)
                    print("-" * 60)   
                      
        elif task_action == "d":   
            try:
                task.delete()
                print("")
                print("Task deleted succesfully")
                print("-" * 60)
            except Exception as exc:
                print("")
                print("Error deleting task ", exc)
                print("-" * 60)
        else:
                print("")
                print("Invalid input")
                print("-" * 60)
    else:

        print("")
        print("Invalid task number")
        print("-" * 60)
            

def find_by_person_id(personid):
    person = Person.find_by_id(personid)
    
    tasks = person.tasks()
    if tasks:
        print("-" * 60)
        print("")
        print(f"{person.name}'s Tasks: ")
        for i in range(len(tasks)):
            print(f"{i+1}. Task: {tasks[i].task}, Due Date: {tasks[i].due_date}")
        print("")
        print("-" * 60)
    
          
def find_by_task_id(task_id):
    task = Task.find_by_id(task_id)
    print("")
    print(f"Task: {task.task}, Due Date: {task.due_date}")  
    print("")  
    print("-" * 60)
    

def add_person():
    person_name = input("Please enter person name: ")
    try:
        Person.create(person_name)
        print("")
        print("Person created succesfully")
        print("")
        print("-" * 60)
    except Exception as exc:
        print("")
        print("Error creating person ", exc )
        print("")
        print("-" * 60)


def delete_person(person_number):
    people = Person.get_all()
    person = people[int(person_number)-1]


    try: 
        person.delete()
        print("")
        print("Person deleted succesfully")
        print("")
        print("-" * 60)
    except Exception as exc:
        print("")
        print("Error deleting person, ", exc)
        print("")
        print("-" * 60)

        
def exit_program():
    print("Goodbye!")
    exit()
