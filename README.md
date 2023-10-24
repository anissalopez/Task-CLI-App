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
To set up the SQLite database run python lib/seed.py. This will populate the database with seed data for the application. 
Run python lib/cli.py to use the application. Upon running the application you will be presented with a menu. 
Follow the prompts to perform the desired actions.



##Demo

Add a Task: Users can add new tasks to their task list.
Manage a Task: Users can view and update details of a specific task.
Delete a Task: Users can delete a task from their task list.
View Task List: Users can view a list of all their tasks.
Exit the Application: Users can exit the application when they are done managing their tasks.
Requirements
Python 3.7 or above
SQLite or PostgreSQL database
Installation
Clone the repository: git clone https://github.com/your-repo.git
Install the required dependencies: pip install -r requirements.txt
Set up the database:
For SQLite: Run python db_setup.py to create the SQLite database.
For PostgreSQL: Update the database connection details in config.py, then run python db_setup.py to create the PostgreSQL tables.
Run the application: python main.py
Usage
Upon running the application, you will be presented with a menu.
Choose an option by entering the corresponding number or letter.
Follow the prompts to perform the desired action.
Use the 'b' or 'e' options to go back to the previous menu or exit the application, respectively.
Support
If you encounter any issues or have any questions or suggestions, please feel free to open an issue in this repository or contact the developer.

License
This project is licensed under the [MIT License](LICENSE).

Feel free to customize the README file to fit your specific application and add any additional sections or information as needed.

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---


https://github.com/anissalopez/python-p3-v2-final-project-task-manager/assets/127756464/ea69510b-18c9-41d8-b613-2f6de841cc90


