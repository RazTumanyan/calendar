from calendar import Calendar


def choices():
    print("\nCalendar Menu:")
    print("1. Add Task")
    print("2. Display Month")
    print("3. Display Week")
    print("4. Display Day")
    print("5. Export Data")
    print("6. Load Data")
    print("7. Exit")
    inp = input("Choose an option: ")
    return int(inp)


def main():
    year = int(input("Enter the year for the calendar: "))
    calendar = Calendar(year)

    while True:
        choice = choices()

        if choice == 1:
            while True:
                confirm1 = input("Are you sure ? (yes/no): ")
                if confirm1.lower() == "yes":
                    while True:
                        start_date = input("Enter the start date (YYYY-MM-DD): ")
                        start_year, start_month, start_day = map(int, start_date.split('-'))
                        if start_year != year or start_month < 1 or start_month > 12 or start_day < 1 or start_day > \
                                calendar.month_days[start_month - 1]:
                            print("Invalid Date")
                            continue
                        break
                    while True:
                        end_date = input("Enter the end date (YYYY-MM-DD): ")
                        end_year, end_month, end_day = map(int, end_date.split('-'))
                        if end_year != year or end_month < 1 or end_month > 12 or end_day < 1 or end_day > \
                                calendar.month_days[end_month - 1]:
                            print("Invalid Date")
                            continue
                        break
                    description = input("Enter the task description: ")
                    try:
                        calendar.add_task(start_date, end_date, description)
                        print("Task added successfully.")
                    except ValueError as e:
                        print(e)
                    break
                elif confirm1.lower() == "no":
                    break
                else:
                    continue

        elif choice == 2:
            while True:
                confirm2 = input("Are you sure ? (yes/no): ")
                if confirm2.lower() == "yes":
                    month = int(input("Enter the month to display: "))
                    try:
                        calendar.display_month(month)
                    except ValueError as e:
                        print(e)
                    break
                elif confirm2.lower() == "no":
                    break
                else:
                    continue

        elif choice == 3:
            while True:
                confirm3 = input("Are you sure ? (yes/no): ")
                if confirm3.lower() == "yes":
                    start_date = input("Enter the start date of the week (YYYY-MM-DD): ")
                    try:
                        calendar.display_week(start_date)
                    except ValueError as e:
                        print(e)
                    break
                elif confirm3.lower() == "no":
                    break
                else:
                    continue

        elif choice == 4:
            while True:
                confirm4 = input("Are you sure ? (yes/no): ")
                if confirm4.lower() == "yes":
                    date = input("Enter the date to display (YYYY-MM-DD): ")
                    try:
                        calendar.display_day(date)
                    except ValueError as e:
                        print(e)
                    break
                elif confirm4.lower() == "no":
                    break
                else:
                    continue

        elif choice == 5:
            while True:
                confirm5 = input("Are you sure ? (yes/no): ")
                if confirm5.lower() == "yes":
                    filename = input("Enter the filename to export data: ")
                    calendar.export_data(filename)
                    print("Data exported successfully.")
                    break
                elif confirm5.lower() == "no":
                    break
                else:
                    continue

        elif choice == 6:
            while True:
                confirm6 = input("Are you sure ? (yes/no): ")
                if confirm6.lower() == "yes":
                    while True:
                        filename = input("Enter the filename to load data: ")
                        try:
                            calendar.load_data(filename)
                            print("Data loaded successfully.")
                            break
                        except FileNotFoundError:
                            print("File not found, try again.")
                            continue
                    break
                elif confirm6.lower() == "no":
                    break
                else:
                    continue

        elif choice == 7:
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
