import todofunctions

#Displays menu to user
def display_options():
    print("\nChoose an option:")
    print("1. Add a task") #DONE
    print("2. Mark task as completed") #DONE
    print("3. Remove the task") #DONE
    print("4. Change the description of an pre-exsisting task")#DONE
    print("5. Sort list by priority") 
    print("6. Save task list")
    print("7. Load pre-existing list")
    print("8. Exit")#DONE
    choice = int(input('\nPlease enter your choice (1-8):'))
    return choice

def main():
    list_obj = todofunctions.todoList()
    print("Welcome")
    choice = display_options()
    flag = True

    while (flag != False):
        if(choice == 1):
            taskName = input('Enter the name of the task:')
            print("Priority options:")
            print("1: High")
            print("2: Medium")
            print("3: Low")
            priority = int(input('Enter priority number:'))
            while (priority < 1 or priority > 3):
                print("Please enter valid input (1,2,3)")
                priority = int(input('Enter priority number:'))

            list_obj.add_task(taskName,priority)
            list_obj.display_list()
            choice = display_options()

        elif (choice == 2):
            list_obj.display_list()
            taskid = int(input("Enter the task number you would like to mark as completed:"))
            list_obj.mark_task(taskid)
            list_obj.display_list() # debug
            choice = display_options()
        
        elif (choice == 3):
            list_obj.display_list()
            taskid = int(input("Enter the task number you would like to delete:"))
            list_obj.del_task(taskid)
            list_obj.display_list()
            choice = display_options()
        
        elif (choice == 4):
            list_obj.display_list()
            taskid = int(input("Enter the task number you would like to change the description:"))
            taskName = input("What would you like to change the description to? ")
            list_obj.edit_task(taskid,taskName)
            list_obj.display_list()
            choice = display_options()

        elif (choice == 5):
            print("Sorting list by priority...") #needs to be implemented
            choice = display_options()

        elif (choice == 6):
            print("Saving task to a txt file...") 
            filename = input("Enter the name of the file (without .txt):")
            filename = filename + ".txt"
            list_obj.saveList(filename)
            choice = display_options()

        elif (choice == 7):
            filename = input("Enter the name of the file (without .txt):")
            filename = filename + ".txt"
            print("Loading task to txt file..")
            list_obj.loadList(filename)
            choice = display_options()

        #To quit
        elif (choice == 8):
            print("Goodbye")
            list_obj.exitList()
            flag = False
        else:
            print("Invalid Input. Please try again.")
            choice = display_options()


main()