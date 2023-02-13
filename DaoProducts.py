from DbHelper import DbHelper
from pydantic import BaseModel
from ResponseModel import *


class ProductModel(BaseModel):
    productCode: str | None = None
    productName: str | None = None
    productLine: str | None = None
    productScale: str | None = None
    productVendor: str | None = None
    productDescription: str| None = None
    quantityInStock: int | None = None
    buyPrice: float | None = None
    MSRP: float| None = None

class DaoProducts:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_products(self):
        try:
            products = []
            query = "SELECT * FROM products;"
            rows = self.db.exe_query(query)
            for row in rows:
                products.append(ProductModel(productCode = row[0], 
                                               productName=  row[1], 
                                               productLine = row[2],
                                               productScale = row[3], 
                                               productVendor = row[4], 
                                               productDescription =  row[5], 
                                               quantityInStock = row[6],
                                               buyPrice = row[7],
                                               MSRP = row[8]
                                               ))
            return response (
                message = 'OK',
                result = products
            )
        except Exception as error:
            return response (
                message = 'KO',
                result = error
            )

    def add_product(self, product):
        try:
            self.db.exe_query(f"INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock , buyPrice, MSRP) VALUES ('{product.productCode}', '{product.productName}', '{product.productLine}', '{product.productScale}', '{product.productVendor}', '{product.productDescription}', '{product.quantityInStock }', '{product.buyPrice}', '{product.MSRP}');commit")
        except Exception as e:
            print('errore durante la connessione')
            print(e)