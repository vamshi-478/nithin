# Health Risk Predictor

print("---- Health Risk Predictor ----")

# User inputs
age = int(input("Enter Age: "))
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))
heart_rate = int(input("Enter Heart Rate: "))
bp = int(input("Enter Blood Pressure: "))

# BMI calculation
bmi = weight / (height * height)

print("\nYour BMI:", round(bmi,2))

# BMI status
if bmi < 18.5:
    print("BMI Status: Underweight")
elif bmi < 25:
    print("BMI Status: Normal")
elif bmi < 30:
    print("BMI Status: Overweight")
else:
    print("BMI Status: Obese")

# Heart rate status
if heart_rate < 60:
    print("Heart Rate: Low")
elif heart_rate <= 100:
    print("Heart Rate: Normal")
else:
    print("Heart Rate: High")

# Blood pressure status
if bp < 90:
    print("Blood Pressure: Low")
elif bp <= 120:
    print("Blood Pressure: Normal")
elif bp <= 140:
    print("Blood Pressure: Pre-High")
else:
    print("Blood Pressure: High")

# Overall health risk
if bmi > 30 or bp > 140 or heart_rate > 100:
    print("\nHealth Risk: HIGH ⚠️")
else:
    print("\nHealth Risk: NORMAL ✅")