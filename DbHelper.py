import mysql.connector
import json
from pathlib import Path 

class DbHelper:
    __connessione = None
    __config = json.loads(Path(r"config.json").read_text())
    
    def __init__(self) -> None:
        try:
            # if(self.__connessione == None):
                self.__connessione = mysql.connector.connect(**self.__config)
        except Exception as e:
            print('errore durante la connessione')
            print(e)

    def exe_query(self, query):
        try:
            cursore = self.__connessione.cursor()           
            cursore.execute(query)
            result = cursore.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            # if (self.__connessione != None):
                self.__connessione.close()