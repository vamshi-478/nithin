# Pulse Guard AI - Simple Blood Pressure Prediction

# Input from user
age = int(input("Enter Age: "))
heart_rate = int(input("Enter Heart Rate: "))
bmi = float(input("Enter BMI: "))
stress = int(input("Enter Stress Level (1-10): "))

# Simple formula to estimate BP
bp = 80 + (0.5 * age) + (0.2 * heart_rate) + (0.3 * bmi) + (2 * stress)

# Output result
print("Predicted Blood Pressure:", round(bp,2), "mmHg")

# Health warning
if bp < 90:
    print("BP Status: Low Blood Pressure")
elif bp <= 120:
    print("BP Status: Normal")
elif bp <= 140:
    print("BP Status: Pre-High BP")
else:
    print("BP Status: High Blood Pressure")