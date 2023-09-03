from util import *

class Activity():    
    todolist_day = list()
    todolist_week = list()

    def __init__(self, name, type = None, days = None, total_time = 0, goal = None, start_time = None):
        self.name = name
        self.days = days
        if self.days is None: 
            self.days = {today: 0}
        self.total_time = total_time
        self.type = type
        self.goal = goal
        self.start_time = start_time

        
    def add_time(self,time):
        time = convert_min_to_dec(time)
        self.days[today] = self.days.get(str(date.today()), 0) + time
        self.total_time += time

        if self.goal is not None: 
            self.goal["time_spent"] += time


    def __str__(self):
        total_days = str()
        if type(self.days) == dict:
            for day, time in self.days.items():
                total_days += f"\n\t{day} : {convert_dec_to_min(time)}h " 

        return f"\n{self.name.capitalize()} has been done for {convert_dec_to_min(self.total_time)}h{total_days}"


    def to_dict(self):
        new_dict = {"name": self.name, "type": self.type, "days": self.days, "total_time": self.total_time, "goal": self.goal, "start_time": self.start_time}
        return new_dict


    @staticmethod
    def to_activity(json_dict):
        return Activity(name=json_dict["name"], type=json_dict["type"], days=json_dict["days"], total_time=json_dict["total_time"], goal=json_dict["goal"], start_time=json_dict["start_time"])


    @staticmethod
    def search(activities_sorted, activity_name, current_size):
        try:
            if activities_sorted[current_size//2].name == activity_name:
                return activities_sorted[current_size//2]
            elif activities_sorted[current_size//2 - 1].name == activity_name:
                return activities_sorted[current_size//2 - 1]
            elif activities_sorted[current_size//2 + 1].name == activity_name:
                return activities_sorted[current_size//2 + 1]
            else:
                if activities_sorted[current_size//2].name < activity_name:
                    activities_sorted = activities_sorted[current_size//2:]
                else:
                    activities_sorted = activities_sorted[:current_size//2 + 1]
            
                current_size = current_size // 2
            
                return Activity.search(activities_sorted, activity_name, current_size)
        except IndexError:
            print(f"{activity_name} not in list.")
            return None
        

    def set_goal(self):
        if self.goal is None:
            time_frame = input("What time frame would you like to use for this goal? (day/week/month/year)").lower()
            if time_frame not in TIME_FRAMES.keys():
                print("Not a valid time frame, no goal set")
                return None

            time_goal = input(f"How many hours per {time_frame} would you like to spend?: ")
            time_goal = convert_min_to_dec(time_goal)

            self.goal = {"time_frame": time_frame, "time_goal": time_goal, "date_started": str(date.today()), "time_spent": 0} 
        else:
            print("This is your current goal:")
            self.print_goal()   
            user_choice = input("would you like to update(y/n): ").lower()
            
            if user_choice == "n":
                return None   
            else:
                while True:
                    user_choice = input("Change time frame: time_frame\nChange time goal: time_goal\nDelete Goal: delete\nQuit: q\n->").lower()
                    
                    if user_choice == "q":
                        print("Your updated goal is: ")
                        self.print_goal()
                        break
                    elif user_choice == "time_goal":
                        time_goal = input("Enter new time goal: ")
                        self.goal["time_goal"] = convert_min_to_dec(time_goal)
                        continue
                    elif user_choice == "time_frame":
                        time_frame = input("Enter new time frame: ")

                        if time_frame in TIME_FRAMES.keys():
                            self.goal["time_frame"] == time_frame
                        else:
                            print("Invalid time frame, no changes made")
                        continue
                    elif user_choice == "delete":
                        user_choice = input("Are you sure you would like to delete this goal? (y/n):").lower()
                        if user_choice == "y":
                            self.goal = None
                            print("goal has been deleted")
                            break
                        elif user_choice == "n":
                            print("goal not delete")
                            continue
                        else:
                            print("invalid command, no changes made")
                            continue
                    else: 
                        print("invalid command, please enter valid command")
                        continue

    def check_goal(self):
        date_started = date.fromisoformat(self.goal["date_started"])
        if (date.today() - date_started).days  >= TIME_FRAMES[self.goal["time_frame"]]:
            self.goal["time_spent"] = 0
            self.goal["date_started"] = str(today)


    def print_goal_progress(self):
        print(f"You are {(self.goal['time_spent']/self.goal['time_goal'] * 100)}% towards finishing your {self.name} goal!")


    def print_goal(self):
        print(f"The goal for {self.name} is: {round(self.goal['time_goal'])}h per {self.goal['time_frame']}")


    def start(self):
        self.start_time = str(datetime.now())
        print(f"you have started a new start time for {self.name} at {self.start_time}")


    def stop(self):
        if self.start_time is None:
            print("You haven't started recording time for this activity")
            return None

        user_choice = input("Would you like to stop doing this activity(y/n)?: ")
        if user_choice == "q":
            return None
        elif user_choice == "y":
            total_time = datetime.now() - datetime.fromisoformat(self.start_time)
            hours = total_time.days * 24 + (total_time.seconds / 3600)

            user_choice = input(f"You have {self.name} for {convert_dec_to_min(hours)}. Would you like to add this to your total?(y/n): ")
            if user_choice == "q":
                return None
            elif user_choice == "y":
                self.add_time(convert_dec_to_min(hours))
                self.start_time = None
                print(f"{convert_dec_to_min(hours)}h have been added to {self.name}")
            else:
                print("No time added.")
                return None
        else:
            print("Activity still in progress.")


    @staticmethod
    def sort_by_time(activities):
        user_input = input("How far back would you like to view?(all|year|month|week|day): ").lower()
        options = {"all": None, "year": current_year, "month": current_month, "week": current_week, "day": today}

        if user_input not in options:
            print("Invalid option")
            return None

        activities_in_time_frame = list()

        if user_input == "all":
            return activities
        
        for act in activities:
            done_in_time_frame = list(filter(lambda x: x in options[user_input], act.days))
            if len(done_in_time_frame) == 0:
                continue
            activities_in_time_frame.append(Activity(act.name, act.type, done_in_time_frame, act.total_time, act.goal, act.start_time))

                    
        return activities_in_time_frame

    
    @staticmethod
    def sort_by_type(activities):
        user_input = input("What type of activities would you like to view?: ").lower()

        activities_with_type = list(filter(lambda x: x.type == user_input, activities))

        if len(activities_with_type) == 0:
            print("No activities with this type found")
            return None

        return Activity.sort_by_time(activities_with_type)
        
    @classmethod
    def create_todolist(activities, cls):
        user_input = input("When should this to do list be completed?(week|day): ").lower()
        
        if user_input == "day":
            pass
        


