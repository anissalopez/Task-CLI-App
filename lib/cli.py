from helpers import (
    view_people,
    exit_program,
    view_by_number,
    add_task,
    manage_task,
    view_tasks,
    view_task_details,
    find_by_person_id,
    find_by_task_id,
    add_person,
    delete_person
)

from cli_menu import(
    main_menu,
    people_menu,
    person_menu,
    task_menu
)

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "1":    
            while True:
                view_people()
                people_menu()
                person_number = input("> ")
                if person_number == 'b':
                    break
                elif person_number == 'e':
                    exit_program()
                elif person_number == 'a':
                    add_person()
                else: 
                     if int(choice) > 0:
                        view_by_number(person_number)
                        while True:
                            person_menu()
                            sub_choice = input("> ")
                            if sub_choice == '1':
                                add_task(person_number)
                            elif sub_choice == '2':
                                view_by_number(person_number)
                                task_number = input("\nType the number of the task you wish to manage: ")
                                manage_task(task_number, person_number)
                            elif sub_choice == '3':
                                delete_person(person_number)
                                break
                            elif sub_choice == '4':
                                break
                            elif sub_choice == '5':
                                exit_program()
                            else:
                                print("Invalid choice")
                    
        elif choice == "2":
            while True:
                view_tasks()
                task_menu()
                sub_choice = input("> ")
                if sub_choice == "b":
                    break
                elif sub_choice == "e":
                    exit_program()
                else: 
                    try:
                        view_task_details(sub_choice)
                    except IndexError:
                        print("Invalid task number")
                        continue
                    while True:
                        print("\nType 'b' to go back to the previous menu")
                        print("Type 'e' to exit")
                        print("\n")
                        task_action = input("> ") 
                        if task_action == "b":
                            break
                        elif task_action == "e":
                            exit_program()
                        else:
                            print("\nInvalid Choice")
        elif choice == "3":
            while True:
            
                person_id = input("\nPlease enter person id: ")
               
                try:
                    find_by_person_id(person_id)
                    break
                except Exception as exc:
                    print("\nError", exc)
        elif choice == "4":
            while True: 
                task_id = input("\nPlease enter task id: ")
                try:
                    find_by_task_id(task_id)
                    break
                except Exception as exc:
                    print("\nError", exc)
        elif choice == "5":
            exit_program()
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()


