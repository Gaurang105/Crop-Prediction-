import numpy as np
import joblib
import pandas as pd

scaler = joblib.load('./model_files/scaler.joblib')
cla = joblib.load('./model_files/cla.joblib')
nature_encoder = joblib.load('./model_files/nature_encoder.joblib')
label_encoder = joblib.load('./model_files/label_encoder.joblib')

def preprocess(N, P, K, temp, humidity, rainfall, nature):
    arr = np.array([[N, P, K, temp, humidity, rainfall]], dtype=np.float32)
    scaled = scaler.transform(arr)

    nature_encoded = nature_encoder.transform([[nature]])

    df = pd.DataFrame(scaled, columns=['N', 'P', 'K', 'temperature', 'humidity', 'rainfall'])
    z = df.assign(acidic=nature_encoded.toarray()[:, 0], alkaline=nature_encoded.toarray()[:, 1], neutral=nature_encoded.toarray()[:, 2])

    return z

def predict(N, P, K, temp, humidity, rainfall, nature):
    preprocessed = preprocess(N, P, K, temp, humidity, rainfall, nature)
    y_pred = cla.predict(preprocessed)
    return label_encoder.categories_[0][y_pred.astype(np.uint8)]

    