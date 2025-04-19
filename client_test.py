
# client_test.py
import requests
import json

def predict_diabetes(glucose, bmi, age):
    url = 'http://127.0.0.1:5000/diabetes'
    payload = {
        'Glucose': glucose,
        'BMI': bmi,
        'Age': age
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

if __name__ == '__main__':
    glucose = int(input("Glucose? "))
    bmi = float(input("BMI? "))
    age = int(input("Age? "))
    result = predict_diabetes(glucose, bmi, age)
    print("Diabetic" if result['result'] == 1 else "Not Diabetic")
    print(f"Confidence: {result['confidence']:.2f}")