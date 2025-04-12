from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings
from models import PredictionModel



client = AsyncIOMotorClient(
    settings.MONGODB_URL
)
database = client[settings.DB_NAME]

async def init_db():
    await init_beanie(database=database, document_models=[PredictionModel])

try:
    client.server_info()
    print('Connected')

except Exception as e:
    print(f'Error, {e}')