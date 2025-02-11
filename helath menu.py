def heart_rate():
    age = int(input("Enter your age: "))
    max_heart_rate = 220 - age
    print(f"Your estimated maximum heart rate: {max_heart_rate} bpm")

def bmi_calculator():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight / (height ** 2)
    print(f"Your BMI: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

def water_intake():
    weight = float(input("Enter your weight (kg): "))
    water_needed = weight * 0.033  # Kilo başına 33 ml su
    print(f"You should drink at least {water_needed:.2f} liters of water per day.")

def health_menu():
    while True:
        print("\n💙 HEALTH MENU 💙")
        print("1 - Calculate Heart Rate")
        print("2 - Calculate BMI")
        print("3 - Water Intake Reminder")
        print("4 - Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            heart_rate()
        elif choice == "2":
            bmi_calculator()
        elif choice == "3":
            water_intake()
        elif choice == "4":
            print("Exiting... Stay Healthy! 💪")
            break
        else:
            print("Invalid choice. Please select again.")

# Run the menu
health_menu()
