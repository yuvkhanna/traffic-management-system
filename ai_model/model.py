import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model():
    # Load dataset
    data = pd.read_csv('traffic_data_new.csv')

    # Convert 'time' column to datetime
    data['time'] = pd.to_datetime(data['time'])

    # Feature engineering from 'time' column
    data['hour'] = data['time'].dt.hour
    data['day_of_week'] = data['time'].dt.dayofweek
    data['month'] = data['time'].dt.month

    # Drop the original 'time' column
    data = data.drop('time', axis=1)

    # Encode 'weather' column if it's categorical
    label_encoder = LabelEncoder()
    data['weather_encoded'] = label_encoder.fit_transform(data['weather'])

    # Define feature matrix X and target vector y
    X = data[['location_lat', 'location_lon', 'hour', 'day_of_week', 'month', 'weather_encoded']]
    y = data['congestion_level']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

    # Save the model
    joblib.dump(model, 'congestion_model.pkl')

# Optionally, if you want to run model.py directly, add this
if __name__ == "__main__":
    train_model()
