
# Employee Management System

This Employee Management System is a Python-based application that allows you to manage employee records in an SQL database. It provides functionalities to add, remove, promote, and display employee details. The system connects to a MySQL database and performs various operations using SQL queries.

## Features

- **Add Employee**: Add a new employee to the database.
- **Remove Employee**: Remove an existing employee from the database.
- **Promote Employee**: Increase the salary of an existing employee.
- **Display Employee**: Display details of a specific employee.
- **Display All Employees**: Display details of all employees.

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/employee-management-system.git
    cd employee-management-system
    ```

2. **Install the Required Python Packages**

    ```sh
    pip install mysql-connector-python tabulate
    ```

3. **Configure the Database Connection**

    Update the database connection details in the script:

    ```python
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YourPassword",
        database="sql_hr"
    )
    ```

4. **Create the Database and Table**

    Ensure you have a MySQL database named `sql_hr` and a table named `employees` with the following structure:

    ```sql
    CREATE DATABASE sql_hr;
    USE sql_hr;

    CREATE TABLE employees (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        post VARCHAR(100),
        salary DECIMAL(10, 2)
    );
    ```

## Usage

Run the script to start the Employee Management System:

```sh
python employee_management_system.py
```

### Main Menu

```
Welcome to Employee Management Record
Press 
1 to Add Employee
2 to Remove Employee
3 to Promote Employee
4 to Display Employee
5 to Display All Employees
6 to Exit
```

## Script Overview

### Main Script

```python
import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPassword",
    database="sql_hr"
)

def check_employee(employee_id, conn):
    sql = 'SELECT * FROM employees WHERE id=%s'
    c = conn.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    c.close()
    return r == 1

def add_employee(conn):
    Id = input("Enter Employee Id: ")
    if check_employee(Id, conn):
        print("Employee already exists\nTry Again\n")
        return
    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")
        data = (Id, Name, Post, Salary)
        sql = 'INSERT INTO employees (id, name, post, salary) VALUES (%s, %s, %s, %s)'
        c = conn.cursor()
        c.execute(sql, data)
        conn.commit()
        c.close()
        print("Employee Added Successfully")

def remove_employee(conn):
    Id = input("Enter Employee Id: ")
    if not check_employee(Id, conn):
        print("Employee does not exist\nTry Again\n")
        return
    else:
        sql = 'DELETE FROM employees WHERE id=%s'
        data = (Id,)
        c = conn.cursor()
        c.execute(sql, data)
        conn.commit()
        c.close()
        print("Employee Removed")

def promote_employee(conn):
    Id = input("Enter Employee Id: ")
    if not check_employee(Id, conn):
        print("Employee does not exist\nTry Again\n")
        return
    else:
        Amount = int(input("Enter increase in Salary: "))
        sql = 'SELECT salary FROM employees WHERE id=%s'
        data = (Id,)
        c = conn.cursor()
        c.execute(sql, data)
        r = c.fetchone()
        new_salary = r[0] + Amount
        sql = 'UPDATE employees SET salary=%s WHERE id=%s'
        d = (new_salary, Id)
        c.execute(sql, d)
        conn.commit()
        c.close()
        print("Employee Promoted")

def display_employee_details(conn):
    Id = input("Enter Employee Id: ")
    sql = 'SELECT * FROM employees WHERE id=%s'
    c = conn.cursor()
    c.execute(sql, (Id,))
    employee_details = c.fetchone()
    if employee_details:
        print("Employee Id: ", employee_details[0])
        print("Employee Name: ", employee_details[1])
        print("Employee Post: ", employee_details[2])
        print("Employee Salary: ", employee_details[3])
        print("-----------------------------------")
    else:
        print("Employee not found.")
    c.close()

def display_all_employees(conn):
    cursor = conn.cursor()
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    data = [row for row in rows]
    columns = [i[0] for i in cursor.description]
    print(tabulate(data, headers=columns))
    cursor.close()

def menu(conn):
    while True:
        print("Welcome to Employee Management Record")
        print("Press ")
        print("1 to Add Employee")
        print("2 to Remove Employee ")
        print("3 to Promote Employee")
        print("4 to Display Employee")
        print("5 to Display All Employees")
        print("6 to Exit")
        
        ch = int(input("Enter your Choice: "))
        if ch == 1:
            add_employee(conn)
        elif ch == 2:
            remove_employee(conn)
        elif ch == 3:
            promote_employee(conn)
        elif ch == 4:
            display_employee_details(conn)
        elif ch == 5:
            display_all_employees(conn)
        elif ch == 6:
            conn.close()
            exit(0)
        else:
            print("Invalid Choice")

menu(conn)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## Contact

If you have any questions or suggestions, feel free to reach out at [yuvraj.works1@gmail.com](mailto:yuvraj.works1@gmail.com).
