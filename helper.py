import todofunctions

# This file allows me to interact with the user and assisted me in debugging
# Author: Smrithy Mudavangattil Sajan

# Displays menu to user
def display_options():
    print("\nChoose an option:")
    print("1. Add a task") #DONE
    print("2. Mark task as completed") #DONE
    print("3. Remove the task") #DONE
    print("4. Change the description of an pre-exsisting task")#DONE
    print("5. Sort list by priority") #DONE
    print("6. Save task list")#DONE
    print("7. Load pre-existing list")#DONE
    print("8. Exit")#DONE
    choice = int(input('\nPlease enter your choice (1-8):'))
    return choice


def main():
    list_obj = todofunctions.todoList()
    print("Welcome")
    choice = display_options()
    flag = True

    #Flag is False when user selects option 8
    while (flag != False):

        #Adding tasks
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

        #Marking the task as completed
        elif (choice == 2):
            list_obj.display_list()
            taskid = int(input("Enter the task number you would like to mark as completed:"))
            list_obj.mark_task(taskid)
            list_obj.display_list() 
            choice = display_options()
        
        #Deleting a task
        elif (choice == 3):
            if (list_obj.sizeList() == 0):
                print("List is empty cannot perform this function")
            else:
                list_obj.display_list()
                taskid = int(input("Enter the task number you would like to delete:"))
                list_obj.del_task(taskid)
                list_obj.display_list()

            choice = display_options()
        
        #Editing an existing task
        elif (choice == 4):
            list_obj.display_list()
            taskid = int(input("Enter the task number you would like to change the description:"))
            taskName = input("What would you like to change the description to? ")
            list_obj.edit_task(taskid,taskName)
            list_obj.display_list()
            choice = display_options()

        #Temporily sorting a task from high to low
        elif (choice == 5):
            print("Sorting list by priority high to low...")
            list_obj.sortList()
            choice = display_options()

        #Saving to a file
        elif (choice == 6):
            print("Saving task to a txt file...") 
            filename = input("Enter the name of the file (without .txt):")
            filename = filename + ".txt"
            list_obj.saveList(filename)
            choice = display_options()

        #Loading from an existing file
        elif (choice == 7):
            filename = input("Enter the name of the file (without .txt):")
            filename = filename + ".txt"
            print("Loading task to txt file..")
            list_obj.loadList(filename)
            choice = display_options()

        #To quit or leave the program, this will also delete all the rows from the table
        elif (choice == 8):
            print("Goodbye")
            list_obj.exitList()
            flag = False

        #if the user enters anything other than 1-8
        else:
            print("Invalid Input. Please try again.")
            choice = display_options()


main()