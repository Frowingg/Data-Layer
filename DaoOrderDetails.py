from DbHelper import DbHelper
from pydantic import BaseModel

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
            result = self.db.exe_query(query)
            for row in result:
                orderDetails.append(OrderDetailModel(orderNumber = row[0], 
                                               productCode=  row[1], 
                                               quantityOrdered = row[2],
                                               priceEach = row[3], 
                                               orderLineNumber = row[4], 
                                               ))
            return orderDetails
        except Exception as e:
            print(e)

    def add_orderDetails(self, orderDetail):
        try:
            self.db.exe_query(f"INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES ('{orderDetail.orderNumber}', '{orderDetail.productCode}', '{orderDetail.quantityOrdered}', '{orderDetail.priceEach}', '{orderDetail.orderLineNumber}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)