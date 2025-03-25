from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
CORS(app)

# Sample dataset for training AI model (Power, Temperature, Maintenance Status)
data = pd.DataFrame({
    "power": [150, 500, 1200, 1800, 250, 600, 1100, 2000, 300, 700],
    "temperature": [4, 30, 22, 45, 5, 32, 20, 50, 6, 35],
    "status": [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]  # 0 = OK, 1 = Maintenance Required
})

# Train AI model
X = data[["power", "temperature"]]
y = data["status"]
model = RandomForestClassifier()
model.fit(X, y)

# Function to predict maintenance status
def predict_maintenance(power, temperature):
    prediction = model.predict([[power, temperature]])[0]
    return "⚠️ Maintenance Needed" if prediction == 1 else "✅ OK"

# API to send appliance data with AI predictions
@app.route('/get_appliances', methods=['GET'])
def get_appliances():
    appliances = [
        {"id": 1, "appliance": "Refrigerator", "power": 150, "temperature": 4},
        {"id": 2, "appliance": "Washing Machine", "power": 500, "temperature": 30},
        {"id": 3, "appliance": "Air Conditioner", "power": 1200, "temperature": 22},
        {"id": 4, "appliance": "Heater", "power": 1800, "temperature": 45},
    ]
    
    # Add AI predictions to appliances
    for appliance in appliances:
        appliance["status"] = predict_maintenance(appliance["power"], appliance["temperature"])

    return jsonify(appliances)

if __name__ == '__main__':
    app.run(debug=True)
