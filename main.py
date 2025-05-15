import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class User:

    def __init__(self, name, se_name, user_id, status):
        self.name = name
        self.se_name = se_name
        self.user_id = user_id
        self.status = status

    def __str__(self):
        return f"name: {self.name}\nse_name: {self.se_name}\nid: {self.user_id}\nstatus: {self.status}\n………………"


def create():
    name = input("Enter name: ")
    se_name = input("Enter last name: ")
    user_id = input("Enter ID: ")
    status = input("Enter status: ")
    if status == "":
        status = "inactive"
    return User(name, se_name, user_id, status)


newuser = []

while True:
    print(
        "1.Add new member \n 2. Display all members\n 3. serch for a nember \n 4. Exit"
    )
    choice = input("Enter your choice:   ")
    if choice == "1":
        clear()
        new = create()
        newuser.append(new)

        time.sleep(2)
        clear()

    elif choice == "3":
        print(
            "Search by:\n 1.MembershipID\n2.first name \n3. membreship status")
        chooce = input("enter your choice:  ")
        time.sleep(4)
        clear()

        if chooce == "2":
            search = input("enter a name :  ")
            found = False
            for x in newuser:
                if x.name.lower() == search.lower():
                    found = True
                    print(x)
                    time.sleep(5)
                    clear()
                    break
            if not found:
                print("not found")

        elif chooce == "1":
            search = input("enter a ID :  ")
            found = False
            for x in newuser:
                if x.user_id == search:
                    found = True
                    print(x)
                    time.sleep(5)
                    clear()

            if not found:
                print("not found")
        elif chooce == "3":
            search = input("enter a status: ")
            found = False
            for x in newuser:
                if x.status.lower() == search.lower():
                    found = True
                    print(x)
                    time.sleep(5)
                    clear()

            if not found:
                print("not found")
    elif choice == "2":
        for x in newuser:
            print(x)
            time.sleep(5)
            clear()

    elif choice == "4":
        break
    else:
        print("Invalid choice. please try again.")
