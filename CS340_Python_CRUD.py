from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db, col):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # insert data
            return True  # return true
        else:
            print("data parameter is empty")
            return False # return false

# Method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data)
        else:
            print("data parameter is empty")
            return False

# Method to implement the U in CRUD
    def update(self, oldData, newData):

        if oldData is not None: # check if data exists in database and ensure updated data is given
            return self.database.animals.update(oldData, {"$set": newData})
        else:
            print("data parameter is empty")
            return False
            
# Method to implement the D in CRUD
    def delete(self, data):
        if data is not None: # check if data exists in database
            return self.database.animals.delete_one(data)
        else:
            print("data parameter is empty")
            return False
