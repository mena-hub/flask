from pymongo import MongoClient
import json

class MongoAPI:
    def __init__(self, data):
    #   self.client = MongoClient("mongodb://localhost:27017/") # MongoDB
        self.client = MongoClient("mongodb://mongo:27017/")     # docker-compose

        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
    
    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Ingresado', 'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': "Actualizado" if response.modified_count > 0 else "Cambios no realizados"}
        return output

    def delete(self, data):
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': "Eliminado" if response.deleted_count > 0 else "Documento no encontrado"}
        return output

# if __name__ == '__main__':
#   data = {"database": "streaming", "collection": "movie"}
#   mongo_object = MongoAPI(data)
#   print(json.dumps(mongo_object.read(), indent=4))