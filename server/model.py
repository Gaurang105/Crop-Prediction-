import numpy as np
import joblib
import pandas as pd

scaler = joblib.load('./model_files/scaler.joblib')
cla = joblib.load('./model_files/cla.joblib')
nature_encoder = joblib.load('./model_files/nature_encoder.joblib')
label_encoder = joblib.load('./model_files/label_encoder.joblib')

states = pd.read_csv('./data_files/states.csv')
ph = states.pop('ph')
nature = pd.cut(ph, bins=[0, 6.5, 7.5, np.inf], labels=['acidic', 'neutral', 'alkaline'])
names = states.pop('Name')
states['nature'] = nature

dc = {}
for name, row in zip(names, states.to_numpy()):
    dc[name] = row

def get_state_data(name):
    return dc[name]

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

def top_5(N, P, K, temp, humidity, rainfall, nature):
    preprocessed = preprocess(N, P, K, temp, humidity, rainfall, nature)
    probas = cla.predict_proba(preprocessed)

    top5 = []

    for _ in range(5):
        k = np.argmax(probas, axis=-1)[0]
        top5.append(k)
        probas[:, k] = -np.inf
    
    top5_labels = []

    for idx in top5:
        top5_labels.append(label_encoder.categories_[0][idx])

    return top5_labels
    