from DbHelper import DbHelper
from pydantic import BaseModel
from datetime import date

class PaymentModel(BaseModel):
    customerNumber: int  
    checkNumber: str
    paymentDate: date 
    amount: float

class DaoPayments:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_payments(self):
        try:
            payments = []
            query = "SELECT * FROM payments;"
            result = self.db.exe_query(query)
            for row in result:
                payments.append(PaymentModel(customerNumber = row[0], 
                                               checkNumber=  row[1], 
                                               paymentDate = row[2],
                                               amount = row[3], 
                                               ))
            return payments
        except Exception as e:
            print(e)

    def add_payment(self, payment):
        try:
            self.db.exe_query(f"INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) VALUES ('{payment.customerNumber}', '{payment.checkNumber}', '{payment.paymentDate}', '{payment.amount}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)