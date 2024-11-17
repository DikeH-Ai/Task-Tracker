#!/usr/bin/env python
import sys, datetime, os, json

def main():
    # accept user input
    # check if argument was passed/ passes correctly
    if len(sys.argv) < 2:
        print("""
            Error: Incomplete argument
                Usage: py program *arguments
                example:
                    task-cli add "Buy groceries"
            """)

        sys.exit()
    # exclude the program name
    user_input = sys.argv[1:]
    # create a dict of functions for each possible command
    dict_func = {
        "add": add,
        "update": update,
        "delete": delete,
        "mark-todo": todo,
        "mark-in-progress": in_progress,
        "mark-done": done,
        "list": list_all,
        "list-done": list_done,
        "list-not-done": list_todo,
        "list-in-progress": list_in_progress,
        "--help": helper,
    }
    if user_input[0] not in dict_func:
        print("Error: Invalid operation")
        sys.exit()

    # set json data file
    json_file = "task_tracker_data.json"

    # open json file
    with open(json_file, "a+") as json_file:
        # call function based on operation
        dict_func[user_input[0]](user_input[1:], json_file)

"""
    Define each operation function
"""
# add task
def add(args_list, json_file):

    if not args_list:
        print("""
            Error: Incomplete argument
                Usage: py program *arguments
                example:
                    task-cli add "Buy groceries"
            """)
        sys.exit()
    try:
        # if the file is empty
        if os.stat(json_file.name).st_size == 0:
            id = 0
            # construct json data
            dict_data = {
                args_list[0]: {
                    "id": id, 
                    "description": args_list[0], 
                    "status": "todo", 
                    "createdAt": datetime.datetime.now().isoformat(), 
                    "updatedAt": None
                } 
                for _ in range(len(args_list)) if isinstance(args_list[0], str)
            }
            
            # convert to json object
            content = json.dump(dict_data, json_file, indent=4)
        else:
        # file already has data
            #  move file pointer to the start
            json_file.seek(0)
            
            # transform file data to python object
            py_object = json.load(json_file)

            # get id        
            id = list(py_object.values())[-1]["id"] + 1
            # construct python data
            dict_data = {
                args_list[0]: {
                    "id": id, 
                    "description": args_list[0], 
                    "status": "todo", 
                    "createdAt": datetime.datetime.now().isoformat(), 
                    "updatedAt": None
                } 
                for _ in range(len(args_list)) if isinstance(args_list[0], str)
            }

            # output
            print(f"Task added successfully (ID: {id})")
            # update dict to json
            py_object.update(dict_data)
            #  move file pointer to the start and overwrite the previous content
            json_file.seek(0)
            json_file.truncate()

            # write json to file
            content = json.dump(py_object, json_file, indent=4)
    except Exception as e:
        print(f"Error(add): {str(e)}")   

# update
def update(args_list, json_file): # delete and recreate a task
    try:
        if len(args_list) < 2:
            print("Invalid number of arguments")
            sys.exit()

        task_id, task = int(args_list[0]), args_list[1]
        # move pointer to the start
        json_file.seek(0)

        # convert json_file date to python object
        py_object = json.load(json_file)

        # update key
        for key, value in py_object.items():
            if value["id"] == task_id:
                value["description"] = task
                py_object[task] = py_object.pop(key)
                py_object[task]["updatedAt"] = datetime.datetime.now().isoformat()
                break
            else:
                print("Task not found")
                sys.exit()

        # move pointer to the top and truncate 
        json_file.seek(0)
        json_file.truncate()
        # write json to file
        content = json.dump(py_object, json_file, indent=4)
    except Exception as e:
        print(f"Error(update): {str(e)}")

# delete
def delete(args_list, json_file):
    try:
        if len(args_list) < 1:
            print("Invalid Argument")
            sys.exit()
        
        task_id = int(args_list[0])
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["id"] == task_id:
                py_object.pop(key)
                break
    
        
        # move pointer to the top and truncate 
        json_file.seek(0)
        json_file.truncate()
        # write json to file
        content = json.dump(py_object, json_file, indent=4)     
    except Exception as e:
        print(f"Error(update): {str(e)}")
    
# mark-todo
def todo(args_list, json_file):
    try:
        if len(args_list) < 1:
            print("Invalid Argument")
            sys.exit()
        
        task_id = int(args_list[0])
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["id"] == task_id:
                value["status"] = "todo"
                py_object[key]["updatedAt"] = datetime.datetime.now().isoformat()
                break

        # move pointer to the top and truncate 
        json_file.seek(0)
        json_file.truncate()
        # write json to file
        content = json.dump(py_object, json_file, indent=4)     
    except Exception as e:
        print(f"Error(todo): {str(e)}")

# mark-in-progress
def in_progress(args_list, json_file):
    try:
        if len(args_list) < 1:
            print("Invalid Argument")
            sys.exit()
        
        task_id = int(args_list[0])
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["id"] == task_id:
                value["status"] = "in-progress"
                py_object[key]["updatedAt"] = datetime.datetime.now().isoformat()
                break

        # move pointer to the top and truncate 
        json_file.seek(0)
        json_file.truncate()
        # write json to file
        content = json.dump(py_object, json_file, indent=4)     
    except Exception as e:
        print(f"Error(todo): {str(e)}")  

# mark-done
def done(args_list, json_file):
    try:
        if len(args_list) < 1:
            print("Invalid Argument")
            sys.exit()
        
        task_id = int(args_list[0])
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["id"] == task_id:
                value["status"] = "done"
                py_object[key]["updatedAt"] = datetime.datetime.now().isoformat()
                break

        # move pointer to the top and truncate 
        json_file.seek(0)
        json_file.truncate()
        # write json to file
        content = json.dump(py_object, json_file, indent=4)     
    except Exception as e:
        print(f"Error(todo): {str(e)}")  

# list
def list_all(args_list, json_file):
    try:
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            print(f"Task: {key}: Task ID: {value["id"]} - Task Status: {value["status"]} - Last Update: {value["updatedAt"]}")
    
    except Exception as e:
        print(f"Error(todo): {str(e)}")  
    

# list-done
def  list_done(args_list, json_file):
    try:
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["status"] == "done":
                print(f"Task: {key}: Task ID: {value["id"]} - Task Status: {value["status"]} - Last Update: {value["updatedAt"]}")
    
    except Exception as e:
        print(f"Error(todo): {str(e)}")  


# list-todo
def  list_todo(args_list, json_file):
    try:
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["status"] == "todo":
                print(f"Task: {key}: Task ID: {value["id"]} - Task Status: {value["status"]} - Last Update: {value["updatedAt"]}")
    
    except Exception as e:
        print(f"Error(todo): {str(e)}")  


# list-in-progress
def  list_in_progress(args_list, json_file):
    try:
        # move pointer to the top
        json_file.seek(0)

        # load json file data to python object
        py_object = json.load(json_file)

        # get task id and delete coresponding data
        for key,value in py_object.items():
            if value["status"] == "in-progress":
                print(f"Task: {key}: Task ID: {value["id"]} - Task Status: {value["status"]} - Last Update: {value["updatedAt"]}")
    
    except Exception as e:
        print(f"Error(todo): {str(e)}")  

# helper function
def helper(*args):
    print("""
./task-tracker --help # list of all available commands

# To add a task
./task-tracker add "Buy groceries"

# To update a task
./task-tracker update 1 "Buy groceries and cook dinner"

# To delete a task
./task-tracker delete 1

# To mark a task as in progress/done/todo
./task-tracker mark-in-progress 1
./task-tracker mark-done 1
./task-tracker mark-todo 1

# To list all tasks
./task-tracker list
./task-tracker list done
./task-tracker list todo
./task-tracker list in-progress
""")
if __name__ == "__main__":
    main()