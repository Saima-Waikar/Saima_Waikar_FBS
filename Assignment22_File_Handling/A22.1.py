import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

def add_record():
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    e = Emp(eid, ename, basic)

    with open("emp.dat", "ab") as f:
        pickle.dump(e, f)

    print("Record added successfully")


def display_all():
    try:
        with open("emp.dat", "rb") as f:
            while True:
                try:
                    e = pickle.load(f)
                    print(e.eid, e.ename, e.basic)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found")


def search_record():
    eid = int(input("Enter Employee ID to search: "))
    found = False

    try:
        with open("emp.dat", "rb") as f:
            while True:
                try:
                    e = pickle.load(f)
                    if e.eid == eid:
                        print(e.eid, e.ename, e.basic)
                        found = True
                        break
                except EOFError:
                    break
    except FileNotFoundError:
        pass

    if not found:
        print("Record not found")


def delete_record():
    eid = int(input("Enter Employee ID to delete: "))
    records = []
    found = False

    try:
        with open("emp.dat", "rb") as f:
            while True:
                try:
                    e = pickle.load(f)
                    if e.eid == eid:
                        found = True
                    else:
                        records.append(e)
                except EOFError:
                    break
    except FileNotFoundError:
        pass

    with open("emp.dat", "wb") as f:
        for e in records:
            pickle.dump(e, f)

    if found:
        print("Record deleted successfully")
    else:
        print("Record not found")


def edit_record():
    eid = int(input("Enter Employee ID to edit: "))
    records = []
    found = False

    try:
        with open("emp.dat", "rb") as f:
            while True:
                try:
                    e = pickle.load(f)

                    if e.eid == eid:
                        e.ename = input("Enter new name: ")
                        e.basic = float(input("Enter new basic salary: "))
                        found = True

                    records.append(e)

                except EOFError:
                    break
    except FileNotFoundError:
        pass

    with open("emp.dat", "wb") as f:
        for e in records:
            pickle.dump(e, f)

    if found:
        print("Record updated successfully")
    else:
        print("Record not found")


while True:
    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_record()
    elif ch == 2:
        search_record()
    elif ch == 3:
        delete_record()
    elif ch == 4:
        edit_record()
    elif ch == 5:
        display_all()
    elif ch == 6:
        break
    else:
        print("Invalid choice")