# Patient Health Data Analyzer

num = int(input("Enter number of patients: "))

high_bp = 0
normal_bp = 0

for i in range(num):
    print("\nPatient", i+1)

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    heart_rate = int(input("Enter heart rate: "))
    bp = int(input("Enter blood pressure: "))

    print("\nHealth Report for", name)

    # Blood pressure analysis
    if bp < 90:
        print("BP Status: Low")
    elif bp <= 120:
        print("BP Status: Normal")
        normal_bp += 1
    elif bp <= 140:
        print("BP Status: Pre-High")
    else:
        print("BP Status: High")
        high_bp += 1

    # Heart rate analysis
    if heart_rate < 60:
        print("Heart Rate: Low")
    elif heart_rate <= 100:
        print("Heart Rate: Normal")
    else:
        print("Heart Rate: High")

# Summary
print("\n---- Hospital Data Summary ----")
print("Total Patients:", num)
print("Patients with Normal BP:", normal_bp)
print("Patients with High BP:", high_bp)