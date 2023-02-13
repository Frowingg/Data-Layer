from DbHelper import DbHelper
from pydantic import BaseModel
from ResponseModel import *
class OrderDetailModel(BaseModel):
    orderNumber: int 
    productCode: str 
    quantityOrdered: int 
    priceEach: float
    orderLineNumber: int

class DaoOrderDetails:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_orderDetails(self):
        try:
            orderDetails = []
            query = "SELECT * FROM orderdetails;"
            rows = self.db.exe_query(query)
            for row in rows:
                orderDetails.append(OrderDetailModel(orderNumber = row[0], 
                                               productCode=  row[1], 
                                               quantityOrdered = row[2],
                                               priceEach = row[3], 
                                               orderLineNumber = row[4], 
                                               ))
            return response (
                message = 'OK',
                result = orderDetails
            )
        except Exception as error:
            return response (
                message = 'KO',
                result = error
            )


    def add_orderDetails(self, orderDetail):
        try:
            self.db.exe_query(f"INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES ('{orderDetail.orderNumber}', '{orderDetail.productCode}', '{orderDetail.quantityOrdered}', '{orderDetail.priceEach}', '{orderDetail.orderLineNumber}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)