import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('congestion_model.pkl')

def predict_congestion(location, time):
    # Input data preprocessing
    features = np.array([location['lat'], location['lon'], time]).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]
