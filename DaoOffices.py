from DbHelper import DbHelper
from pydantic import BaseModel
from ResponseModel import *

class OfficeModel(BaseModel):
    officeCode: str | None = None
    city: str | None = None
    phone: str | None = None
    addressLine1: str | None = None
    addressLine2: str | None = None
    state: str | None = None
    country: str | None = None
    postalCode: str | None = None
    territory: str | None = None

class DaoOffices:
    def __init__(self):
        self.db = DbHelper()
    
    def get_all_offices(self):
        try:
            offices = []
            query = "SELECT * FROM offices;"
            rows = self.db.exe_query(query)
            for row in rows:
                offices.append(OfficeModel(officeCode = row[0], 
                                               city=  row[1], 
                                               phone = row[2],
                                               addressLine1 = row[3], 
                                               addressLine2 = row[4], 
                                               state =  row[5], 
                                               country = row[6],
                                               postalCode = row[7],
                                               territory = row[8]
                                               ))
            return response (
                message = 'OK',
                result = offices
            )
        except Exception as error:
            return response (
                message = 'KO',
                result = error
            )


    def add_office(self, office):
        try:
            self.db.exe_query(f"INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory) VALUES ('{office.officeCode}', '{office.city}', '{office.phone}', '{office.addressLine1}', '{office.addressLine2}', '{office.state}', '{office.country}', '{office.postalCode}', '{office.territory}');commit")
        except Exception as e:
            print(e)