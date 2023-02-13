from DbHelper import DbHelper
from pydantic import BaseModel

class EmployeeModel(BaseModel):
    employeeNumber: int | None = None
    lastName: str | None = None
    firstName: str | None = None
    extension: str | None = None
    email: str | None = None
    officeCode: str | None = None
    reportsTo: int | None = None
    jobTitle: str | None = None

class DaoEmployees:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_employees(self):
        try:
            employees = []
            query = "SELECT * FROM employees;"
            result = self.db.exe_query(query)
            for row in result:
                employees.append(EmployeeModel(employeeNumber = row[0], 
                                               lastName = row[1], 
                                               firstName=  row[2], 
                                               extension = row[3],
                                               email = row[4], 
                                               officeCode = row[5], 
                                               reportsTo =  row[6], 
                                               jobTitle = row[7]
                                               ))
            return employees
        except Exception as e:
            print(e)

    def add_employee(self, employee):
        try:
            self.db.exe_query(f"INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES ('{employee.employeeNumber}','{employee.lastName}','{employee.firstName}','{employee.extension}','{employee.email}','{employee.officeCode}','{employee.reportsTo}','{employee.jobTitle}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)