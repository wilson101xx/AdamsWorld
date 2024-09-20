import os
from openai import OpenAI
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()

embedding_service_id = "embedding"
gpt_model = os.getenv("OPENAI_4O")
gpt_key = os.getenv("OPENAI_KEY")
gpt_embedding = os.getenv("OPENAI_EMBEDDING_MODEL")
organisation_id = os.getenv("organisation_id")

client = OpenAI(
    api_key=gpt_key,
    organization=organisation_id,

)

def embedding(data):
    response = client.embeddings.create(
        model="text-embedding-3-small", input=data, encoding_format="float"
    )
    final = response.data[0].embedding
    return final


def python_mongo():

    uri = "mongodb+srv://wilsonadam15:Wilson101!@cluster0.bantn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    

    with open("./documents/cv.txt", "r") as f:
        cv = f.read()

    db = client["vector_database"]  # Replace with your database name
    collection = db["vector_collection"]  # Replace with your collection name

    embedded_data = embedding(cv)
    document = {
    "name": "AdamCV",  # metadata field
    "description": "This is Adams",  # more metadata
    "vector": embedded_data
    }

    result = collection.insert_one(document)
    print(f"Document inserted with id: {result.inserted_id}")



if __name__ == "__main__":
    # print(embedding("Testing 123"))
    python_mongo()