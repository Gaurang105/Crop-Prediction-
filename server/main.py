import asyncio
from fastapi import FastAPI, Request, Response
import model


app = FastAPI()

@app.get('/api/cropr')
async def crop_recommendation(request: Request):
    try:
        data = await request.json()
    except Exception:
        return Response(content={'m': 'invalid json payload'}, status_code=400)

    result = await asyncio.get_running_loop().run_in_executor(None, model.predict, 80, 90, 20, 21, 81, 210, 'acidic')

    print(await request.body())
    return {'prediction': str(result)}

