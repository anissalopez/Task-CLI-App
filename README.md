## Task CLI Application

Task App is a command-line interface program that allows users to create and manage their tasks. The application uses an object relational data model that combines a relational database and object relational models to persist user data. The application features various functions that allow users to add people to a database and create, update or delete their tasks. 


## Features 
1. List of the names of all the people in the tasks database
2. List of all of the tasks in the tasks database and an option to view the details (person id and due_date) associated with each task
4. Add/delete a person to/from the database
3. Add, update or delete tasks for a person
4. Search the database by task id 
5. Search the database by person id 


Below is a high level summary of the functions that handle the applications features. 
The functions are located in lib -> helpers.py

- view_people(): returns a list the names of the people located  in the Person table
- view_tasks(): returns a list of all tasks located in the ToDo table
- view_task_detail(): returns the tasks due_date and name 
- delete_task(): deletes a task from the ToDo table 
- view_by_number(): returns the tasks for a person the user selected from the CLI menu
- add_task(): creates a task object and maps the data to ToDo table
- manage_task(): allows a user to update or delete an existing task
- find_by_person_id(): returns a user with matching id
- find_by_task_id(): returns a task with matching id
- add_person(): adds person to Person table 
- delete_person(): deletes person model from Person database
- exit_program(): exits the application when users are done managing their tasks 


## Data Models 
The program features a Person and a Task class. 

<img width="800" alt="ORM model (1)" src="https://github.com/anissalopez/python-p3-v2-final-project-task-manager/assets/127756464/9e07d77c-dfc9-45b2-906a-e4fd4ab4a531">



## Application Requirements
Python 3.8.13 
SQLite 

## Getting Started 
- To get started run python pipenv install to install any needed depencies 
- Then run pipenv shell to enter into a virtual environment
- To set up the SQLite database with some seed data run python lib/seed.py 
- To use the app run python lib/cli.py and follow the prompts to perform the desired actions 


https://github.com/anissalopez/python-p3-v2-final-project-task-manager/assets/127756464/ea69510b-18c9-41d8-b613-2f6de841cc90





