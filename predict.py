import requests
import io
from fastapi import HTTPException
from config import settings


async def get_prediction(images_bytes: bytes):
    try:
        print('Иштеди')
        url = settings.ROBOFLOW_URL
        files = {
            'file':('image.jpg', io.BytesIO(images_bytes), 'image/jpg')
        }
        response = requests.post(url, files=files)
        print(response.text)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail='Server Error')
        return {'confidence':response.json()['predictions'][0]['confidence'] * 100,
                'time':response.json()['time'] }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))