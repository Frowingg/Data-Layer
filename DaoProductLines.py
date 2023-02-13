from DbHelper import DbHelper
from pydantic import BaseModel
from datetime import date
from ResponseModel import *


class ProductLineModel(BaseModel):
    productLine: str | None = None
    textDescription: str | None = None
    htmlDescription: date | None = None
    image: str | None = None

class DaoProductLines:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_productlines(self):
        try:
            productlines = []
            query = "SELECT * FROM productlines;"
            rows = self.db.exe_query(query)
            for row in rows:
                productlines.append(ProductLineModel(productLine = row[0], 
                                               textDescription=  row[1], 
                                               htmlDescription = row[2],
                                               image = row[3], 
                                               ))
            return response (
                message = 'OK',
                result = productlines
            )
        except Exception as error:
            return response (
                message = 'KO',
                result = error
            )


    def add_productline(self, productline):
        try:
            self.db.exe_query(f"INSERT INTO productlines (productLine, textDescription, htmlDescription, image) VALUES ('{productline.productLine}', '{productline.textDescription}', '{productline.htmlDescription}', '{productline.image}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)