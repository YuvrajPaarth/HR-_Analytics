import mysql.connector
from tabulate import tabulate

# Replace these values with your actual database connection details
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yuvi@12345",
    database = "sql_hr"
)

cursor = conn.cursor()
select_query = "SELECT * FROM sql_hr.employees"
cursor.execute(select_query)
rows = cursor.fetchall()
#Making in table
data = [row for row in rows]
columns = [i[0] for i in cursor.description]

print(tabulate(data, headers=columns))
menu()

# Close the cursor and connection when done
cursor.close()
conn.close()


#Check Employee Function
def check_employee(employee_id):
    sql = 'SELECT * FROM sql_hr.employees WHERE id=%s'
    c = conn.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql,data)
    r = c.rowcount
    if r == 1:
        return True
    else:
        menu()
        return False
#Add Employee Function
def Add_Employ():
    Id = input("Enter Employee Id: ")
    if (check_employee(Id) == True):
        print("Employee already exists\nTry Again\n")
        menu()
     
    else:
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        data = (Id, Name, Post, Salary)
 
        # Inserting Employee details in the Employee 
        # Table
        sql = 'insert into empd values(%s,%s,%s,%s)'
        c = conn.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in the table
        conn.commit()
        print("Employee Added Successfully ")
        menu()

# Function to Remove Employee with given Id
def Remove_Employ():
    Id = input("Enter Employee Id : ")
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
     
    else:
        # Query to Delete Employee from Table
        sql = 'delete from empd where id=%s'
        data = (Id,)
        c = conn.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # commit() method to make changes in 
        # the table
        conn.commit()
        print("Employee Removed")
        menu()

# Function to Promote Employee
def Promote_Employee():
    Id = int(input("Enter Employ's Id"))
 
    # Checking if Employee with given Id
    # Exist or Not
    if(check_employee(Id) == False):
        print("Employee does not  exists\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary"))
 
        # Query to Fetch Salary of Employee with 
        # given Id
        sql = 'select salary from empd where id=%s'
        data = (Id,)
        c = conn.cursor()
 
        # Executing the SQL Query
        c.execute(sql, data)
 
        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount
 
        # Query to Update Salary of Employee with
        # given Id
        sql = 'update empd set salary=%s where id=%s'
        d = (t, Id)
 
        # Executing the SQL Query
        c.execute(sql, d)
 
        # commit() method to make changes in the table
        conn.commit()
        print("Employee Promoted")
        menu()

def Display_Employee_Details(Id):
    # Query to select a specific employee from the Employee Table
    sql = 'select * from empd where EmployeeId = %s'
    c = conn.cursor()

    # Executing the SQL Query with the provided employee ID
    c.execute(sql, (Id,))

    # Fetching the details of the employee
    employee_details = c.fetchone()

    # If employee exists, display their details
    if employee_details:
        print("Employee Id : ", employee_details[0])
        print("Employee Name : ", employee_details[1])
        print("Employee Post : ", employee_details[2])
        print("Employee Salary : ", employee_details[3])
        print("-----------------------------------")
    else:
        print("Employee not found.")
        menu()

# menu function to display the menu
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
     
    # Taking choice from user
    ch = int(input("Enter your Choice "))
    if ch == 1:
        Add_Employ()
         
    elif ch == 2:
        Remove_Employ()
         
    elif ch == 3:
        Promote_Employee()
         
    elif ch == 4:
        Display_Employee_Details()
         
    elif ch == 5:
        exit(0)
         
    else:
        print("Invalid Choice")
        menu()