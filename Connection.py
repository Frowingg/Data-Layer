import mysql.connector
import json
from pathlib import Path 

class Connection:
    __connection = None
    __config = json.loads(Path(r"config.json").read_text())

    def __init__(self) -> None:
        try:
            if (self.__connection == None):
                self.__connection = mysql.connector.connect(**self.__config)
        except Exception as error:
            print(error)

    @property
    def connection(self):
        return self.__connection
        
    def exe_query(self, query):
        try:
            # cursore = self.__connessione.cursor(dictionary=True)  
            cursor = self.__connection.cursor()           
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as error:
            print(error)
        finally:
            if (self.__connection != None):
                self.__connection.close()

# MyConnection = Connection()
# print(MyConnection)