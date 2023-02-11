import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import model


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

headers = {
    'Access-Control-Allow-Origin': "*"
}


def validate_input(data):
    keys = ['N', 'P', 'K', 'temp', 'humidity', 'rainfall']

    for k in keys:
        float(data[k])

    if data['nature'] not in ['acidic', 'neutral', 'alkaline']:
        raise ValueError('Invalid value for field nature')


@app.get('/api/cropr')
async def crop_r(N: float, P: float, K: float, temp: float, humidity: float, rainfall: float, nature: str):
    if nature not in ['acidic', 'neutral', 'alkaline']:
        return JSONResponse({
            'm': 'Invalid nature provided, valid values are [acidic, neutral, alkaline]'
        },
            status_code=400,
            headers=headers
        )
    prediction = await asyncio.get_running_loop().run_in_executor(None, model.predict, N, P, K, temp, humidity, rainfall, nature)
    return JSONResponse({'prediction': str(prediction[0])}, headers=headers)


# @app.post('/api/cropr')
# async def crop_recommendation(request: Request):
#     try:
#         data = await request.json()
#         try:
#             validate_input(data)
#         except KeyError as e:
#             key = e.args,
#             return JSONResponse(
#                 content={
#                     'm': f'Key not specified {key}'
#                 },
#                 status_code=400,
#             )
#         except ValueError as e:
#             return JSONResponse(
#                 content={
#                     'm': str(e)
#                 },
#                 status_code=400
#             )
#     except json.decoder.JSONDecodeError:
#         return JSONResponse(content={'m': 'invalid json payload'}, status_code=400, headers=headers)

#     result = await asyncio.get_running_loop().run_in_executor(None, model.predict, *data.values())

#     print(await request.body())
#     return {'prediction': str(result)}
