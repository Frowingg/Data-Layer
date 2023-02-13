from DbHelper import DbHelper
from pydantic import BaseModel
from datetime import date
from ResponseModel import *

class OrderModel(BaseModel):
    orderNumber: int | None = None
    orderDate: date | None = None
    requiredDate: date | None = None
    shippedDate: date | None = None
    status: str | None = None
    comments: str | None = None
    customerNumber: int | None = None

class DaoOrders:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_orders(self):
        try:
            orders = []
            query = "SELECT * FROM orders;"
            rows = self.db.exe_query(query)
            for row in rows:
                orders.append(OrderModel(orderNumber = row[0], 
                                        orderDate=  row[1], 
                                        requiredDate = row[2],
                                        shippedDate = row[3], 
                                        status = row[4], 
                                        comments = row[5],
                                        customerNumber = row[6]
                                        ))
            return response (
                message = 'OK',
                result = orders
            )
        except Exception as error:
            return response (
                message = 'KO',
                result = error
            )


    def add_order(self, order):
        try:
            self.db.exe_query(f"INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber) VALUES ('{order.orderNumber}','{order.orderDate}','{order.requiredDate}','{order.shippedDate}','{order.status}','{order.comments}','{order.customerNumber}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)