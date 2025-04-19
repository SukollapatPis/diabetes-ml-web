# app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

# Load the trained model
model = pickle.load(open('diabetes-model.pkl', 'rb'))

# Create the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

@app.route('/diabetes', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['Glucose'], data['BMI'], data['Age']]
    prediction = model.predict([features])
    confidence = model.predict_proba([features])

    result = {
        'result': int(prediction[0]),
        'confidence': float(np.max(confidence[0]))
    }
    return jsonify(result)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
