# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username='aacuser', password='YOUR_PASSWORD_HERE'): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """Insert a document into the animals collection."""
        try:
            if data is not None:
                result = self.collection.insert_one(data)
                return result.acknowledged
            return False
        except Exception:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        """Return documents matching the supplied query."""
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception:
            return []
        
    # Update method to implement the U in CRUD.
    def update(self, query, new_data):
        """Update documents matching the supplied query."""
        try:
            if query is not None and new_data is not None:
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                return result.modified_count
            return 0
        except Exception:
            return 0
        
    # Delete method to implement the D in CRUD.
    def delete(self, query):
        """Delete documents matching the supplied query."""
        try:
            if query is not None:
                result = self.collection.delete_many(query)
                return result.deleted_count
            return 0
        except Exception:
            return 0