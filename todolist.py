import string
tasks_list = []
isRunning = True

def main():
    global isRunning
    while(isRunning):
        global tasks_list
        #display current task
        if not tasks_list:
            print("No current task yet")
        else:
            displayTask()
        #user menu
        print("======================")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Exit")
        print("======================")
        try:
            user_input = int(input("Enter Option: "))
            match user_input:
                case 1:
                    addTask()
                case 2:
                    deleteTask()
                case 3:
                    isRunning = False
        except ValueError:
            print("Must be 1,2,3 only!")
        
# #add Task
def addTask():
    #check if task has value
    global tasks_list
    user_input = input("Task Name: ")
    tasks_list.append(user_input)
        
# #deleteTask
def deleteTask():
    global tasks_list
    try:
        user_input = int(input("Task ID: ")) #input
        for task in range(len(tasks_list)): 
            if task != user_input:
                tasks_list.pop(user_input)
                print("Task Succesfully Removed.")
            else: 
                print("Task ID not Found.")
    except ValueError:
        print("Must be a number!")
            
            
# #displayTask
def displayTask():
    #counter for ID
    global tasks_list
    print()
    print("Task List:")
    for task in range(len(tasks_list)):
        print(f"{task}: {tasks_list[task]}")
        
main()