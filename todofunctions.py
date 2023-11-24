import database
class todoList:
    def __init__(self):
        #dictionary to keep track of tasks
        self.tasks = {} 
   
    #to add a task
    def add_task(self,task,priority):
        numtasks = len(self.tasks) + 1
        completed = False
        self.tasks[numtasks] = {'Task':task, 'Priority': priority, 'Completed':False }
        print("Task added sucessfully")
        database.add_task(self,numtasks,task,completed,priority)

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
            completed = self.tasks[taskid]['Completed']
            database.mark_task(self,taskid,completed)
        else:
            print("Invalid task number")

    #remove task
    def del_task(self,taskid):
        if taskid in self.tasks:
            self.tasks.pop(taskid)
            print("Task was successfully deleted.")
            database.del_task(self,taskid)
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
    #Exit - this should remove all data from the table
    def exitList(self):
        database.exit(self)

    #To string 
    def __str__(self):
        return self.tasks