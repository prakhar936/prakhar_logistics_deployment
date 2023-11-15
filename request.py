import requests

url = "http://localhost:5000/predict_api"

r = requests.post(url,json={'Pregnancies':1, 'Glucose':85, 'Insulin':0, 'BMI':26.6, 'DiabetesPedigreeFunction':0.351, 'Age':31})

print(r.json())