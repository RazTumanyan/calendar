from calendar import Calendar


def choices():
    print("\nCalendar Menu:")
    print("1. Add Task")
    print("2. Display Month")
    print("3. Display Week")
    print("4. Display Day")
    print("5. Export Data")
    print("6. Load Data")
    print("Type 'e' For Exit")
    inp = input("Choose an option: ")
    return inp


def main():
    while True:
        year = input("Enter the year for the calendar: ")
        try:
            calendar = Calendar(int(year))
            while True:
                choice = choices()

                match choice:
                    case "1":
                        condition = True
                        while condition:
                            while True:
                                start_date = input("Enter the start date (YYYY-MM-DD) / for exit type 'e': ")
                                if start_date == "e":
                                    condition = False
                                    break
                                try:
                                    start_year, start_month, start_day = map(int, start_date.split('-'))
                                except Exception as e:
                                    print(e)
                                    continue
                                try:
                                    calendar.validate_date(start_year, start_month, start_day)
                                    break
                                except Exception as e:
                                    print(e)
                                    continue
                            while True:
                                if start_date == "e":
                                    break
                                end_date = input("Enter the end date (YYYY-MM-DD) / for exit type 'e': ")
                                if end_date == "e":
                                    condition = False
                                    break
                                try:
                                    end_year, end_month, end_day = map(int, end_date.split('-'))
                                except Exception as e:
                                    print(e)
                                    continue
                                try:
                                    calendar.validate_date(end_year, end_month, end_day)
                                    break
                                except Exception as e:
                                    print(e)
                                    continue
                            if start_date != "e" and end_date != "e":
                                if (start_year, start_month, start_day) > (end_year, end_month, end_day):
                                    print("Start date cannot be after end date")
                                    continue
                                else:
                                    description = input("Enter the task description: ")
                                    calendar.add_task(start_date, end_date, description)
                                    print("Task added successfully.")
                                    break

                    case "2":
                        while True:
                            month = input("Enter the month to display / for exit type 'e': ")
                            if month == "e":
                                break
                            try:
                                calendar.display_month(int(month))
                                break
                            except Exception as e:
                                print(e)
                                continue

                    case "3":
                        while True:
                            start_date = input("Enter the start date of the week (YYYY-MM-DD) / for exit type 'e': ")
                            if start_date == "e":
                                break
                            try:
                                calendar.display_week(start_date)
                                break
                            except Exception as e:
                                print(e)
                                continue

                    case "4":
                        while True:
                            date = input("Enter the date to display (YYYY-MM-DD) / for exit type 'e': ")
                            if date == "e":
                                break
                            try:
                                calendar.display_day(date)
                                break
                            except Exception as e:
                                print(e)
                                continue

                    case "5":
                        filename = input("Enter the filename to export data / for exit type 'e': ")
                        if filename == "e":
                            continue
                        calendar.export_data(filename)
                        print("Data exported successfully.")

                    case "6":
                        while True:
                            filename = input("Enter the filename to load data / for exit type 'e': ")
                            if filename == "e":
                                break
                            try:
                                calendar.load_data(filename)
                                print("Data loaded successfully.")
                                break
                            except FileNotFoundError:
                                print("File not found, try again.")
                                continue

                    case "e":
                        print("Exiting the program.")
                        break

                    case _:
                        print("Invalid option. Please try again.")
            break
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    main()
