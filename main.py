from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from typing import List
from DaoCustomers import *
from DaoEmployees import *
from DaoOffices import *
from DaoOrderDetails import *
from DaoOrders import *
from DaoPayments import *
from DaoProductLines import *
from DaoProducts import *

app = FastAPI()

dao_customer = DaoCustomers()
dao_employee = DaoEmployees()
dao_office = DaoOffices()
dao_orderDetail = DaoOrderDetails()
dao_order = DaoOrders()
dao_payment = DaoPayments()
dao_productline = DaoProductLines()
dao_product = DaoProducts()

@app.get('/')
async def base():
    return 'Hello World!'

# COSTUMERS

@app.get("/get_customers/")
async def get_all_customers():
    return dao_customer.get_all_customers()

@app.post('/add_customer/')
async def add_customer(customer:CustomerModel):
    return dao_customer.add_customer(customer)

# EMPLOYEES

@app.get("/get_employees/", response_model=List[EmployeeModel])
async def get_all_employees():
    return dao_employee.get_all_employees()

@app.post('/add_employee/')
async def add_employee(employee:EmployeeModel):
    dao_employee.add_employee(employee)
    # if employee:
    return JSONResponse(content={"message": f"Nuovo impiegato inserito nel db: '{employee.employeeNumber}','{employee.lastName}','{employee.firstName}','{employee.extension}','{employee.email}','{employee.officeCode}','{employee.reportsTo}','{employee.jobTitle}'"})
    # else:


# OFFICES

@app.get("/get_offices/", response_model=List[OfficeModel])
async def get_all_offices():
    return dao_office.get_all_offices()

@app.post('/add_office/')
async def add_office(office:OfficeModel):
        dao_office.add_office(office)
        return JSONResponse(content={"message": f"Nuovo ufficio inserito nel db: '{office.officeCode}', '{office.city}', '{office.phone}', '{office.addressLine1}', '{office.addressLine2}', '{office.state}', '{office.country}', '{office.postalCode}', '{office.territory}"})
        # print(f"Connessione al db fallita a causa {e}")
# ORDER_DETAILS

@app.get("/get_orderDetails/", response_model=List[OrderDetailModel])
async def get_all_orderDetails():
    return dao_orderDetail.get_all_orderDetails()

@app.post('/add_orderDetails/')
async def add_orderDetails(orderDetail:OrderDetailModel):
    dao_orderDetail.add_orderDetails(orderDetail)
    return JSONResponse(content={"message": f"Nuovo dettaglio dell'ordine inserito nel db: '{orderDetail.orderNumber}', '{orderDetail.productCode}', '{orderDetail.quantityOrdered}', '{orderDetail.priceEach}', '{orderDetail.orderLineNumber}'"})


# ORDERS

@app.get("/get_orders/", response_model=List[OrderModel])
async def get_all_orders():
    return dao_order.get_all_orders()

@app.post('/add_orders/')
async def add_order(order:OrderModel):
    dao_order.add_order(order)
    return JSONResponse(content={"message": f"Nuovo ordine inserito nel db: '{order.orderNumber}','{order.orderDate}','{order.requiredDate}','{order.shippedDate}','{order.status}','{order.comments}','{order.customerNumber}'"})

# PAYMENTS

@app.get("/get_payments/", response_model=List[PaymentModel])
async def get_all_payments():
    return dao_payment.get_all_payments()

@app.post('/add_payment/')
async def add_payment(payment:PaymentModel):
    dao_payment.add_payment(payment)
    return JSONResponse(content={"message": f"Nuovo ordine inserito nel db: '{payment.customerNumber}', '{payment.checkNumber}', '{payment.paymentDate}', '{payment.amount}'"})

# PRODUCT_LINES

@app.get("/get_productlines", response_model=List[ProductLineModel])
async def get_all_productlines():
    return dao_productline.get_all_productlines()

@app.post('/add_productline/')
async def add_productline(productline:ProductLineModel):
    dao_productline.add_productline(productline)
    return JSONResponse(content={"message": f"Nuovo ordine inserito nel db: '{productline.productLine}', '{productline.textDescription}', '{productline.htmlDescription}', '{productline.image}'"})


# PRODUCTS

@app.get("/get_products/", response_model=List[ProductModel])
async def get_all_products():
    return dao_product.get_all_products()

@app.post('/add_product/')
async def add_product(product:ProductModel):
    dao_product.add_product(product)
    return JSONResponse(content={"message": f"Nuovo ordine inserito nel db: '{product.productCode}', '{product.productName}', '{product.productLine}', '{product.productScale}', '{product.productVendor}', '{product.productDescription}', '{product.quantityInStock }', '{product.buyPrice}', '{product.MSRP}'"})