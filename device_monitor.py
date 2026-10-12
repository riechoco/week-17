def get_initial_readings():
    return [28, 31, 35, 37, 29]
def add_reading(readings):
    try:
        reading = input("\nEnter new reading: ")

        if not reading.strip():
            raise ValueError

        value = int(reading)

        readings.append(value)
        print("\nReading added successfully.")
    except ValueError:
        print("\nInvalid input. Enter a whole number only.")
def classify_reading(reading, warning_limit, critical_limit):
    if reading <= warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"
def compute_total(readings):
    return sum(readings)
def compute_average(readings):
    if len(readings) == 0:
        return 0
    return compute_total(readings) / len(readings)
def find_minimum(readings):
    if len(readings) == 0:
        return None
    return min(readings)
def find_maximum(readings):
    if len(readings) == 0:
        return None
    return max(readings)
def count_category(readings, warning_limit, critical_limit, category):
    count = 0

    for reading in readings:
        if classify_reading(reading, warning_limit,
                            critical_limit) == category:
            count += 1

    return count
def determine_overall_status(warning_count, critical_count):
    if critical_count > 0:
        return "ATTENTION REQUIRED"
    elif warning_count > 0:
        return "MONITORING REQUIRED"
    else:
        return "NORMAL"
def display_summary(readings):
    if not readings:
        print("\nNo readings available.")
        return
    warning_limit = 30
    critical_limit = 35
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)
    normal_count = count_category(
        readings, warning_limit, critical_limit, "NORMAL"
    )
    warning_count = count_category(
        readings, warning_limit, critical_limit, "WARNING"
    )
    critical_count = count_category(
        readings, warning_limit, critical_limit, "CRITICAL"
    )
    number = len(readings)
    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print(f"\nNORMAL   : {normal_count} "
          f"({normal_count / number * 100:.2f}%)")
    print(f"WARNING  : {warning_count} "
          f"({warning_count / number * 100:.2f}%)")
    print(f"CRITICAL : {critical_count} "
          f"({critical_count / number * 100:.2f}%)")
    status = determine_overall_status(
        warning_count, critical_count
    )
    print(f"\nOverall Status: {status}")
def main():
    readings = get_initial_readings()
    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")
        try:
            choice = input("\nEnter choice: ")

            if not choice.strip():
                raise ValueError

            choice = int(choice)
        except ValueError:
            print("\nInvalid input. Enter a whole number only.")
            continue
        if choice == 1:
            print("\nCURRENT READINGS")
            print("----------------")
            for i, reading in enumerate(readings, start=1):
                print(f"Reading {i}: {reading} °C")
        elif choice == 2:
            add_reading(readings)
        elif choice == 3:
            print("\nREADING CLASSIFICATION")
            print("----------------------")
            for i, reading in enumerate(readings, start=1):
                category = classify_reading(reading, 30, 35)
                print(f"Reading {i}: {reading} °C - {category}")
        elif choice == 4:
            display_summary(readings)
        elif choice == 5:
            print("\nThank you for using the Device Monitoring System.")
            break

        else:
            print("\nInvalid choice. Please select 1 to 5.")
main()
