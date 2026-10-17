readings = [20, 25, 32, 34, 17, 27]
choice = ""

def main_menu():
    global choice
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        current_readings()
    elif choice == "2":
        add_reading(readings)
    elif choice == "3":
        classify_reading(readings, 30, 35)
    elif choice == "4":
        generate_summary()
    elif choice == "5":
        kill_program()
    else:
        print("Invalid choice. Please select from 1 to 5.")
        main_menu()


def kill_program():
    print("Thank you for using the Device Monitoring System.")
    raise SystemExit

def current_readings():
    print("\nCURRENT ROOM TEMPERATURE READINGS")
    print("----------------------------------")

    for i, reading in enumerate(readings, start=1):
        print(f"Reading {i}: {reading} °C")

    choice2 = input('\nEnter "1" to return to the main menu or "2" to exit: ')

    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()

def add_reading(readings):
    new_reading = int(input("Enter new reading (°C): "))
    readings.append(new_reading)
    print(f"Reading added successfully: {new_reading} °C\n")

    choice2 = input('\nEnter "1" to return to the main menu or "2" to exit: ')

    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()


def classify_reading(reading, warning_limit, critical_limit):
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for i, reading in enumerate(readings, start=1):
        if reading < 20:
            level = "LOW"
        elif reading <= 30:
            level = "HIGH"
        else:
            level = "CRITICALLY HIGH"

        print(f"Reading {i}: {reading} °C -> {level}")

    choice2 = input('\nEnter "1" to return to the main menu or "2" to exit: ')

    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()

def generate_summary():
    total = sum(readings)
    avg = total / len(readings)
    highest = max(readings)
    lowest = min(readings)

    normal = 0
    warning = 0
    critical = 0

    for reading in readings:
        if reading < 20:
            critical += 1
        elif reading <= 30:
            normal += 1
        elif reading <= 35:
            warning += 1
        else:
            critical += 1

    total_readings = len(readings)

    normal_percent = (normal / total_readings) * 100
    warning_percent = (warning / total_readings) * 100
    critical_percent = (critical / total_readings) * 100

    # Overall status
    if critical > 0:
        overall_status = "ATTENTION REQUIRED"
    elif warning > 0:
        overall_status = "MONITOR CLOSELY"
    else:
        overall_status = "NORMAL"

    print("\nSUMMARY REPORT:")
    print("----------------")
    print(f"Total readings: {len(readings)}")
    print(f"Average room temperature: {avg:.2f} °C")
    print(f"Highest room temperature: {highest} °C")
    print(f"Lowest room temperature: {lowest} °C")

    print()
    print(f"NORMAL   : {normal} ({normal_percent:.2f}%)")
    print(f"WARNING  : {warning} ({warning_percent:.2f}%)")
    print(f"CRITICAL : {critical} ({critical_percent:.2f}%)")
    print(f"\nOverall Status: {overall_status}")

    choice2 = input('\nEnter "1" to return to the main menu or "2" to exit: ')

    if choice2 == "1":
        main_menu()
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to main menu.\n")
        main_menu()

if __name__ == "__main__":
    while True:
        main_menu()