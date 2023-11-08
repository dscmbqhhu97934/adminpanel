import random
import sqlite3



def connect_to_server(test, value):
    if test:
        return {"status": 200, "Message": "Connected server - "+str(random.randint(10,200))+"ms"}
    else:
        return {"status": 200, "Message": "Connecting servet"}

