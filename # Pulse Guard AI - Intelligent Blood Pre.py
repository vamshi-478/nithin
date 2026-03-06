# Pulse Guard AI - Intelligent Blood Pressure Prediction System

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Sample Dataset
data = {
    'Age':[25,30,35,40,45,50,55,60,65,70],
    'HeartRate':[72,75,78,80,82,85,88,90,92,95],
    'BMI':[22,24,26,27,28,30,31,32,33,34],
    'Stress':[2,3,4,5,6,6,7,8,8,9],
    'SystolicBP':[110,115,120,125,130,135,140,145,150,155]
}

df = pd.DataFrame(data)

# Features and Target
X = df[['Age','HeartRate','BMI','Stress']]
y = df['SystolicBP']

# Train Test Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Model
model = RandomForestRegressor()
model.fit(X_train,y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
error = mean_absolute_error(y_test,predictions)
print("Mean Absolute Error:",error)

# User Input for Prediction
print("\nEnter Patient Data")

age = int(input("Age: "))
heart_rate = int(input("Heart Rate: "))
bmi = float(input("BMI: "))
stress = int(input("Stress Level (1-10): "))

input_data = np.array([[age,heart_rate,bmi,stress]])

bp_prediction = model.predict(input_data)

print("\nPredicted Blood Pressure:",bp_prediction[0])