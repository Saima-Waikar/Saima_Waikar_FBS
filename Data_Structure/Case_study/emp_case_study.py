def addEmp():
    id = int(input('Enter ID:'))
    nm = input('Enter Name:')
    dept = input('Enter Department:')
    sal = float(input('Enter Salary:'))
    if(id not in emp_details):
        emp_details[id] = [id,nm,dept,sal]
        return 'Employee adeed successfully.'
    else:
        return 'Employee ID already available.'

def updEmp():
    id = int(input('Enter ID:'))
    er = emp_details.get(id)         #er=emp_record
    if(er):
        nm = input(f'Enter new Name({er[1]}):') or er[1]
        dept = input(f'Enter new Department({er[2]}):') or er[2]
        sal = float(input(f'Enter new Name({er[3]}):') or 0) or er[3]
        emp_details[id] = [id,nm,dept,sal]
        return 'Employee updated successfully'
    else:
        return 'Id not found'

def delEmp():
    id = int(input('Enter ID:'))
    if(id in emp_details):
        del emp_details[id]
        return 'Employee deleted successfully'
    else:
        return 'Id not found'

def searchEmp():
    id = int(input('Enter ID:'))
    er = emp_details.get(id)
    if(er):
        return er
    else:
        return 'Id not found'

def showEmp():
    print(emp_details)

def empManage():
    ch = 0
    while(ch!='6'):
        print('''###EMPLOYEE MANAGEMENT###
        Please select option from below:
        1.Add emp
        2.Update emp
        3.Delete emp
        4.Search emp
        5.Show all
        6.logout''')
        ch = input('Enter Choice:')
        if(ch=='1'):
            res = addEmp()
            print(res)
        elif(ch=='2'):
            res = updEmp()
            print(res)
        elif(ch=='3'):
            res = delEmp()
            print(res)
        elif(ch=='4'):
            res = searchEmp()
            print(res)
        elif(ch=='5'):
            showEmp()
        elif(ch=='6'):
            print('Logged out...')
        else:
            print('Invalid choice....')

def login():
    print("###LOGIN PAGE3###")
    uid = 'admin'
    passw = '1234'
    username = input('Enter Username:')
    password = input('Enter Password:')
    if(uid == username and passw == password):
        empManage()
    else:
        print('Invalid credentials...')

emp_details = {}
ch = 0
while(ch!='2'):
    print('''Please select option from below:
    1.Login
    2.Exit''')
    ch = input("Enter choice:")
    if(ch=='1'):
        login()
    elif(ch=='2'):
        print("Thank you for choosing us!")
    else:
        print("Invalid Choice....")