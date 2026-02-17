import getpass
import hashlib

mylist = ['Fix Computer', 'Buy Markers']
username = 'lancer'

passwordHash = hashlib.sha256('1234'.encode()).hexdigest()


def main():
    menu()

def menu():
    while True:
        print("\n---- To Do List ----")
        print("\n1. Enter a new task. ")
        print("2. View task list. ")
        print("3. Remove a task")
        print("4. Exit Application\n")
        menuoptions()
    
def menuoptions():
    try:            # Input Validation 21 - 25 return is important to end statement
        userinput = int(input("Enter an option (1-4):"))
    except ValueError:
        print("Invalid. Try (1-4)")
        return
    if userinput == 1:
        addtask = str(input("Add a task:"))
        mylist.append(addtask)
    elif userinput == 2:
        print("\nTasks\n--------------")
        if len(mylist) == 0:
            print("No tasks yet!")
        else:
            for i, task in enumerate(mylist, 1):
                print(f"{i}. {task}")
    elif userinput == 3:
        task = str(input("Enter task to be removed:"))
        if task in mylist:
            mylist.remove(task)
    elif userinput == 4:
        exit()
    else:
        print("Input Invalid")


def Login():
    uname = str(input("Username: ").lower())
    if uname == username:
        passw = getpass.getpass("Password: ")
        passw_hashed = hashlib.sha256(passw.encode()).hexdigest()
        if passw_hashed == passwordHash:
            print("Access Is Granted.")
            main()
        else: 
            print("Invalid Credentials\n")
    else:
        print("Invalid Credentials")

Login()


