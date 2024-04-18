## Task CLI Application

Task App is a command-line interface program that allows users to create and manage their tasks. The application uses an object relational data model that combines a relational database and object relational models to persist user data. The application features various functions that allow users to create, update or delete their tasks. 


[![Watch the video](https://img.youtube.com/vi/DyVw-CaBOj4/maxresdefault.jpg)](https://youtu.be/DyVw-CaBOj4)



## Features 
1. View list of all people 
2. View list of all tasks 
3. View task details
4. Add/delete a person to/from the database
5. Add, update or delete tasks for a person
6. Search the database by task id 
7. Search the database by person id 


Below is a high level summary of the functions that accomplish these features:

- view_people(): returns list of all people 
- view_tasks(): returns list of all tasks
- view_task_detail(): returns the tasks due_date and name 
- delete_task(): deletes a task instance and it's details from the tasks table
- view_by_number(): returns the tasks for the person the user selects
- add_task(): creates a task object and persists the objects details to the tasks table
- manage_task(): updates or deletes a user's task and persists the updates to the tasks table
- find_by_person_id(): returns a user with matching id
- find_by_task_id(): returns a task with matching id
- add_person(): creates a person instance and persists that instance's details to the people table
- delete_person(): deletes person instance and removes instance's details from the people table
- exit_program(): exits the application when users are done managing their tasks 


## Data Models 
The program utilizes two object relational models -- Task and Person. These classes create a tasks and a people table, respectively, and maps data from the respective classes to and from those tables. 

The structure is a compositional one to many relationship in which a person can have many tasks but a task is only associated with one person and a task cannot be created without a person. 

![Diagram](<People and Tasks diagram (1).png>)


## Application Requirements
Python 3.8.13 
SQLite 

## Getting Started 
- To get started run python pipenv install required dependencies
- Then run pipenv shell to enter into a virtual environment
- To set up the SQLite database with some seed data run python lib/seed.py 
- To use the app run python lib/cli.py and follow the prompts to perform the desired actions 


https://github.com/anissalopez/python-p3-v2-final-project-task-manager/assets/127756464/ea69510b-18c9-41d8-b613-2f6de841cc90





