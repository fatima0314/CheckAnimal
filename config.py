from dotenv import load_dotenv
import os

load_dotenv()

class Setting:

    MONGODB_URL = os.getenv('MONGODB_URL')
    ROBOFLOW_URL = os.getenv('ROBOFLOW_URL')
    DB_NAME = os.getenv('DB_NAME')

settings = Setting()