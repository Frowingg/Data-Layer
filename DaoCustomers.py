from DbHelper import DbHelper
from pydantic import BaseModel
from ResponseModel import *

class CustomerModel(BaseModel):
    customerNumber: int | None = None
    customerName: str | None = None
    contactLastName: str | None = None
    contactFirstName: str | None = None
    phone: str | None = None
    addressLine1: str | None = None
    addressLine2: str | None = None
    city: str | None = None
    state: str | None = None
    postalCode: str| None = None
    country: str | None = None
    salesRepEmployeeNumber: int | None = None
    creditLimit: float| None = None

class DaoCustomers:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_customers(self):
        customers = []
        try:
            query = "SELECT * FROM customers;"
            rows = self.db.exe_query(query)
            for row in rows:
                customers.append(CustomerModel(customerNumber = row[0], 
                                               customerName = row[1], 
                                               contactLastName=  row[2], 
                                               contactFirstName = row[3],
                                               phone = row[4], 
                                               addressLine1 = row[5], 
                                               addressLine2=  row[6], 
                                               city = row[7],
                                               state = row[8], 
                                               postalCode = row[9], 
                                               country=  row[10], 
                                               salesRepEmployeeNumber = row[11],
                                               creditLimit = row[12]
                                              ))
            return response (
                message = 'OK',
                result = customers
            )
        except Exception as error:
            return response (
                message = 'KO',
                result = error
            )



    def add_customer(self, customer):
        try:
            self.db.exe_query(f"INSERT INTO customerss (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) VALUES ('{customer.customerNumber}', '{customer.customerName}','{customer.contactLastName}','{customer.contactFirstName}','{customer.phone}','{customer.addressLine1}','{customer.addressLine2}','{customer.city}','{customer.state}','{customer.postalCode}','{customer.country}','{customer.salesRepEmployeeNumber}','{customer.creditLimit}');commit")
            return response (
                    message = 'OK',
                    result = f"Nuovo cliente inserito nel db: '{customer.customerNumber}', '{customer.customerName}','{customer.contactLastName}','{customer.contactFirstName}','{customer.phone}','{customer.addressLine1}','{customer.addressLine2}','{customer.city}','{customer.state}','{customer.postalCode}','{customer.country}','{customer.salesRepEmployeeNumber}','{customer.creditLimit}'"
            )
        except Exception as error:
            return response (
                    message = 'KO',
                    result = error
            )