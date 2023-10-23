def main_menu():
    return print("""
    
Welcome! Please select from the following: 
                            
1.View list of people with tasks to complete")
2. View list of all tasks")
3. Search tasks by person id")
4. Search task by id")
5. Exit          
        """)

def people_menu():
    return  print("""
                      
Type the number of the person to view their tasks
Type 'a' to add a person")
Type 'b' to go back to the previous menu")
Type 'e' to exit")

                """)

def person_menu():
    return print("""

1. Add a task
2. Manage task")
3. Delete person")
4. Go back to the previous menu")
5. Exit")
""") 

def task_menu():
    return print("""
          
Type the number of the task to view details
Type 'b' to go back to the previous menu
Type 'e' to exit

          """)
               