import database

class todoList:
    def __init__(self):
        #dictionary to keep track of tasks
        self.tasks = {} 
   
    #to add a task
    def add_task(self,task,priority):
        numtasks = len(self.tasks) + 1

        for k,v in self.tasks.items():
            key = k
            if key == numtasks:
                numtasks = numtasks + 1

        completed = False
        self.tasks[numtasks] = {'Task':task, 'Priority': priority, 'Completed':False }
        print("Task added sucessfully")
        database.add_task(numtasks,task,completed,priority)

    def add_task2(self,id,task,priority,completed):
        self.tasks[id] = {'Task':task, 'Priority': priority, 'Completed':completed }
        print("Task added sucessfully")
        database.add_task(id,task,completed,priority)

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
            database.mark_task(taskid,completed)
        else:
            print("Invalid task number")

    #remove task
    def del_task(self,taskid):
        if taskid in self.tasks:
            #database.del_task(taskid) #doesn't work
            self.tasks.pop(taskid)
            print("Task was successfully deleted.")
        else:
            print("Invalid task")

    #Edit task
    def edit_task(self,taskid,taskName):
        if taskid in self.tasks:
            self.tasks[taskid]['Task'] = taskName
            database.edit_task(taskid,taskName)
        else:
            print("Invalid task number")


    #Sort tasks by priority
    def sortList(self):
        numoftasks = len(self.tasks.keys())
        if(numoftasks == 0):
            print("Task list is empty, cannot be sorted")
        else:
            tasklist = []
            for i in range(numoftasks):
                temp = []
                taskname = self.tasks[i+1]['Task']
                pr = self.tasks[i+1]['Priority']
                temp.append(taskname)
                temp.append(pr)
                tasklist.append(temp)
            
            self.highlow(tasklist)
            
    #prints for high to low, but high is 1, low is 3  
    def highlow(self,tasklist):
        size = len(tasklist)
        for i in range(size - 1):
            for j in range(0, size - i - 1):
                if tasklist[j][1] > tasklist[j + 1][1]:
                    tasklist[j], tasklist[j + 1] = tasklist[j + 1], tasklist[j]
        for c in range(size):
            print(tasklist[c])

    #Save task
    def saveList(self,filename):
        try:
            f = open(filename,"w")

            for k,v in self.tasks.items():
                taskid = str(k)
                f.write("TaskID:" + taskid + "\n")
                
                for key in v:
                    k = key
                    vk = str(v[key])
                    f.write(key + ":" + vk)
                    f.write("\n")
            f.close()        
        except FileNotFoundError:
            print("File not found")

    #Load task
    def loadList(self,filename):
        try:
            f = open(filename,"r")
            lines = f.readlines() #reading all lines in file
            list = []
            for line in lines:
                line = line.strip('\n')
                list.append(line)
            f.close()
        
            for i in range(len(list)):
                if 'TaskID:' in list[i]:
                    (tkid,id) = list[i].split(':')
                    a = i + 1

                    if 'Task:' in list[a]:
                        (tk,tkname) = list[a].split(':')
                        b = a + 1

                        if 'Priority:' in list[b]:
                            (pr,prNo) = list[b].split(':')
                            c = b + 1

                            if 'Completed:' in list[c]:
                                Toftest = True
                                ToF = ''
                                (co,ToF) = list[c].split(':')

                                if ToF == 'True':
                                    Toftest = True
                                else:
                                    Toftest = False

                                self.add_task2(int(id),tkname,prNo,Toftest)
        except FileNotFoundError:
            print("File Not Found")

    #Exit - this should remove all data from the table
    def exitList(self):
        database.exit()

    #To string 
    def __str__(self):
        return self.tasks