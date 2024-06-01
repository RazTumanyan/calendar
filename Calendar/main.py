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
                while True:
                    start_date = input("Enter the start date (YYYY-MM-DD): ")
                    start_year, start_month, start_day = map(int, start_date.split('-'))
                    try:
                        calendar.validate_date(start_year, start_month, start_day)
                        break
                    except ValueError as e:
                        print(e)
                        continue
                while True:
                    end_date = input("Enter the end date (YYYY-MM-DD): ")
                    end_year, end_month, end_day = map(int, end_date.split('-'))
                    try:
                        calendar.validate_date(end_year, end_month, end_day)
                        break
                    except ValueError as e:
                        print(e)
                        continue
                if (start_year, start_month, start_day) > (end_year, end_month, end_day):
                    print("Start date cannot be after end date")
                    continue
                else:
                    description = input("Enter the task description: ")
                    calendar.add_task(start_date, end_date, description)
                    print("Task added successfully.")
                    break

        elif choice == 2:
            while True:
                month = int(input("Enter the month to display: "))
                try:
                    calendar.display_month(month)
                    break
                except ValueError as e:
                    print(e)
                    continue

        elif choice == 3:
            while True:
                start_date = input("Enter the start date of the week (YYYY-MM-DD): ")
                try:
                    calendar.display_week(start_date)
                    break
                except ValueError as e:
                    print(e)
                    continue

        elif choice == 4:
            while True:
                date = input("Enter the date to display (YYYY-MM-DD): ")
                try:
                    calendar.display_day(date)
                    break
                except ValueError as e:
                    print(e)
                    continue

        elif choice == 5:
            filename = input("Enter the filename to export data: ")
            calendar.export_data(filename)
            print("Data exported successfully.")

        elif choice == 6:
            while True:
                filename = input("Enter the filename to load data: ")
                try:
                    calendar.load_data(filename)
                    print("Data loaded successfully.")
                    break
                except FileNotFoundError:
                    print("File not found, try again.")
                    continue

        elif choice == 7:
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
