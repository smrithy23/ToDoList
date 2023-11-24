
class todoList:
    def __init__(self):
        #dictionary to keep track of tasks
        self.tasks = {} 
   
    #to add a task
    def add_task(self,task,priority):
        numtasks = len(self.tasks)
        self.tasks[numtasks+1] = {'Task':task, 'Priority': priority, 'Completed':False }
        print("Task added sucessfully")

    #displays the current list
    def display_list(self):
        print("\nTo-do list")
        print("----------")
        for k,v in self.tasks.items():
            print("Task No:", k)

            for key in v:
                print(key + ':', v[key])

            print("\n")
    
    #mark as completed
    def mark_task(self,taskid):
        if taskid in self.tasks:
            self.tasks[taskid]['Completed'] = True
            print("Task has been masked as completed.")
        else:
            print("Invalid task number")

    #remove task
    def del_task(self,taskid):
        if taskid in self.tasks:
            self.tasks.pop(taskid)
            print("Task was successfully deleted.")
        else:
            print("Invalid task")

    #Edit task
    def edit_task(self,taskid,taskName):
        if taskid in self.tasks:
            self.tasks[taskid]['Task'] = taskName
        else:
            print("Invalid task number")


    #Sort tasks by priority
    #Save task
    #Load task

    #To string 
    def __str__(self):
        return self.tasks