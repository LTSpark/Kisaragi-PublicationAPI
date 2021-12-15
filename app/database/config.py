import os

from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

def connect_database():
    conection_string = os.getenv("MONGODB_URI")
    connect(host=conection_string)

