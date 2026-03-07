# Stress level calculator (1 to 10 scale)

heart_rate = int(input("Enter heart rate: "))
sleep_hours = float(input("Enter sleep hours: "))
work_hours = float(input("Enter work hours per day: "))

# Calculate stress score
score = (heart_rate/10) + (8 - sleep_hours) + (work_hours/2)

# Convert to 1–10 scale
stress_level = int(score)

# Limit value between 1 and 10
if stress_level < 1:
    stress_level = 1
elif stress_level > 10:
    stress_level = 10

print("Stress Level (1-10):", stress_level)

if stress_level <= 3:
    print("Low Stress ")
elif stress_level <= 7:
    print("Moderate Stress")
else:
    print("High Stress ")
