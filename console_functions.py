from activity import Activity

def add_activity(activities):
    activity_name = input("Enter the name of the activity: ").lower()
    if activity_name == "q":
        return None

    activity_type = input("What type of activity is it?: ").lower()
    if activity_type == "q":
        return None
    
    new_activity = Activity(activity_name, type = activity_type)

    activities_sorted = sorted(activities, key=lambda x:x.name)

    if Activity.search(activities_sorted, activity_name, len(activities_sorted)) is not None:
        print("Activity already exists.")
        return None
    
    activities.append(new_activity)
    choice = input("Would you like to add time to this activity?(y/n): ").lower()
    if choice == "q":
        return None

    if choice == "y":
        add_time(activities, activity_name)
    elif choice == "n":
        print("no time added")
    else:
        print("invalid choice, no time added")


def add_time(activities, name = ""):
    if name == "":
        name = input("What activity would you like to add time to?: ").lower()
        if name == "q":
            return None
    time = input(f"How much time would you like too add to {name}?: ").lower()
    if time == "q":
        return None

    for x in activities:
        if x.name == name:
            try:
                x.add_time(time)
                print(f"{time}h added")
            except ValueError:
                print("invalid time, time not updated")


def print_activities(activities):
    if len(activities) == 0:
        print("No activities to list")
    
    user_input = input("How would you like to view activities?(all|type|time): ").lower()

    if user_input == "q":
        return None
    elif user_input == "all":
        for i in activities:
            print(i)
    elif user_input == "type":
        activities_done_at_time  = Activity.sort_by_type(activities)
        if len(activities_done_at_time) == 0:
            print("No activities of this type done in  this time frame")
            return None 
        for i in activities_done_at_time:
            print(i)
        print()

    elif user_input == "time":
        activities_done_at_time = Activity.sort_by_time(activities)

        if activities_done_at_time == None:
            return None

        if len(activities_done_at_time) == 0:
            print("No activities done in time frame")
            return None 
        for i in activities_done_at_time:
            print(i)
        print()
    else:
        print("Invalid command")


def delete_activity(activities):
    name = input("What activity would you like to delete?: ").lower()

    if name == "q":
        return None

    for x in activities:
        if x.name == name:
            user_choice = input(f"Are you sure you want to delete {name}?(y/n): ").lower()
            if user_choice == "y":
                print(f"{name} has been deleted")
                activities.remove(x)
                return None
            elif user_choice == "n":
                print("No change made")
                return None
            else:
                print("Invalid Choice, no changes made")
                return None
            
def search_for_activity(activities):
    name = input("What activity would you like to search for?: ").lower()
    
    if name == "q":
        return None

    activities_sorted = sorted(activities, key=lambda x:x.name)

    act = Activity.search(activities_sorted, name, len(activities_sorted))
    
    print(act) 

    user_choice = input(f"Would you like to add time to {name}?(y/n): ").lower()
    
    if user_choice == "q":
        return None

    if user_choice == "y":
        add_time(activities, name)
    elif user_choice == "n":
        print("no time added")
    else:
        print("invalid choice, no time added")


def create_new_goal(activities):
    name = input("What activity would you like to set a goal for?: ").lower()

    if name == "q":
        return None

    activity = Activity.search(activities, name, len(activities))

    if activity is None:
        return None
    
    activity.set_goal()


def display_goals(activities):
    user_activities_with_goals = list()
    for i in activities:
        if i.goal is not None:
            user_activities_with_goals.append(i)

    if not len(user_activities_with_goals) == 0:
        print()
        print("Here are your current goals and their progress: ")
        print("-------------------------------------------- ")
        for i in user_activities_with_goals:
            i.check_goal()
            i.print_goal()
            i.print_goal_progress() 
            print()
        print()
    else:
        print()

def start_activity(activities):
    name = input("What activity would you like to start: ").lower()

    if not Activity.activity_in_list(activities, name):
        print("This activity does not exist")
        return None
    
    if name == "q":
        return None

    activity = Activity.search(activities, name, len(activities))
    activity.start()

def stop_activity(activities):
    name = input("What activity would you like to stop: ").lower()

    if name == "q":
        return None

    activity = Activity.search(activities, name, len(activities))

    if activity is None:
        return None

    activity.stop()

def print_patch_notes():
    print("""PATCH NOTES:
------------------------------------
v.1.0.0
Initial Release. 
Updates: 
add, delete and update activities 
start and stop timer for an activity
------------------------------------
v.1.1.0
View selection update.
Updates:
allows user to view by activity type 
or by date
------------------------------------
""")
print()