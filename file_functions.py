import json
from activity import Activity

def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            activities = json.load(f)["activities"]
            activities_objects = []
            for i in activities:
                activities_objects.append(Activity.to_activity(i))
    except FileNotFoundError:
        activities_objects = []
    
    return activities_objects

def update_file(file_path, activities):
    with open(file_path, 'w') as f:
        activities_dict = []
        for x in activities:
            activities_dict.append(x.to_dict())
        activities = {"activities": activities_dict}
        json.dump(activities, f)