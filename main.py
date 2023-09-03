from file_functions import *
from console_functions import *
from util import FILE_NAME
 
def main():    
    print("Welcome to DyproCode2023(c)v.1.1.0 Time Manager!")
    print("-------------------------------------------- ")
    print("add    - To add new activity")
    print("start  - To start timing an activity")
    print("stop   - To stop timing an activity")
    print("time   - To add time to an existing activity")
    print("list   - To see a list of activities")
    print("search - To search for an activity")
    print("delete - To delete an activity")
    print("goal   - To create a new goal for an activity")
    print("notes  - To print patch notes")
    print("q      - To quit program or command")
    
    user_activities = read_file(FILE_NAME)
    
    display_goals(user_activities)
    
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input == "q":
            update_file(FILE_NAME, user_activities)
            break
        elif user_input == "add":
            add_activity(user_activities)
            update_file(FILE_NAME, user_activities)
        elif user_input == "start":
            start_activity(user_activities)
            update_file(FILE_NAME, user_activities)
        elif user_input == "stop":
            stop_activity(user_activities)
            update_file(FILE_NAME, user_activities)
        elif user_input == "time":
            add_time(user_activities)
            update_file(FILE_NAME, user_activities)
        elif user_input == "search":
            search_for_activity(user_activities)
        elif user_input == "list":
            print_activities(user_activities)
        elif user_input == "delete":
            delete_activity(user_activities)
            update_file(FILE_NAME, user_activities)  
        elif user_input == "goal":
            create_new_goal(user_activities)
            update_file(FILE_NAME, user_activities)
        elif user_input == "notes":
            print_patch_notes()
        else:
            print("Enter a valid command!")


if __name__ == "__main__":
    main()