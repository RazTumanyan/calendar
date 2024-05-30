class Calendar:
    def __init__(self, year):
        self.year = year
        self.tasks = {}
        self.month_days = [31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

    def is_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0:
            return True
        else:
            return False

    def validate_date(self, year, month, day):
        if year != self.year or month < 1 or month > 12 or day < 1 or day > self.month_days[month - 1]:
            raise ValueError("Invalid date")

    def date_str(self, year, month, day):
        return f"{year:04d}-{month:02d}-{day:02d}"

    def add_task(self, start_date, end_date, description):
        start_year, start_month, start_day = map(int, start_date.split('-'))
        end_year, end_month, end_day = map(int, end_date.split('-'))
        if (start_year, start_month, start_day) > (end_year, end_month, end_day):
            raise ValueError("Start date cannot be after end date")
        current_year, current_month, current_day = start_year, start_month, start_day
        while (current_year, current_month, current_day) <= (end_year, end_month, end_day):
            self.validate_date(current_year, current_month, current_day)
            date_key = self.date_str(current_year, current_month, current_day)
            if date_key not in self.tasks:
                self.tasks[date_key] = []
            self.tasks[date_key].append(description)
            current_day += 1
            if current_day > self.month_days[current_month - 1]:
                current_day = 1
                current_month += 1
                if current_month > 12:
                    current_month = 1
                    current_year += 1

    def display_month(self, month):
        print(f"Tasks for {self.month_names[month - 1]} {self.year}")
        for day in range(1, self.month_days[month - 1] + 1):
            date_key = self.date_str(self.year, month, day)
            if date_key in self.tasks:
                print(f"{day}: {', '.join(self.tasks[date_key])}")

    def display_week(self, start_date):
        start_year, start_month, start_day = map(int, start_date.split('-'))
        print(f"Tasks for the week starting {start_date}")
        for _ in range(7):
            date_key = self.date_str(start_year, start_month, start_day)
            if date_key in self.tasks:
                print(f"{date_key}: {', '.join(self.tasks[date_key])}")
            start_day += 1
            if start_day > self.month_days[start_month - 1]:
                start_day = 1
                start_month += 1
                if start_month > 12:
                    start_month = 1
                    start_year += 1

    def display_day(self, date):
        year, month, day = map(int, date.split('-'))
        self.validate_date(year, month, day)
        date_key = self.date_str(year, month, day)
        if date_key in self.tasks:
            print(f"Tasks for {date_key}: {', '.join(self.tasks[date_key])}")
        else:
            print(f"No tasks for {date_key}")

    def export_data(self, filename):
        with open(filename, 'w') as file:
            file.write(f"year:{self.year}\n")
            for date, tasks in self.tasks.items():
                tasks_str = '|'.join(tasks)
                file.write(f"{date}:{tasks_str}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.year = int(lines[0].strip().split(':')[1])
            self.tasks = {}
            for line in lines[1:]:
                date, tasks_str = line.strip().split(':')
                tasks = tasks_str.split('|')
                self.tasks[date] = tasks
            self.month_days = [31, 29 if self.is_leap_year() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main():
    year = int(input("Enter the year for the calendar: "))
    calendar = Calendar(year)

    while True:
        print("\nCalendar Menu:")
        print("1. Add Task")
        print("2. Display Month")
        print("3. Display Week")
        print("4. Display Day")
        print("5. Export Data")
        print("6. Load Data")
        print("7. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")
            description = input("Enter the task description: ")
            try:
                calendar.add_task(start_date, end_date, description)
                print("Task added successfully.")
            except ValueError as e:
                print(e)

        elif choice == 2:
            month = int(input("Enter the month to display: "))
            try:
                calendar.display_month(month)
            except ValueError as e:
                print(e)

        elif choice == 3:
            start_date = input("Enter the start date of the week (YYYY-MM-DD): ")
            try:
                calendar.display_week(start_date)
            except ValueError as e:
                print(e)

        elif choice == 4:
            date = input("Enter the date to display (YYYY-MM-DD): ")
            try:
                calendar.display_day(date)
            except ValueError as e:
                print(e)

        elif choice == 5:
            filename = input("Enter the filename to export data: ")
            calendar.export_data(filename)
            print("Data exported successfully.")

        elif choice == 6:
            filename = input("Enter the filename to load data: ")
            try:
                calendar.load_data(filename)
                print("Data loaded successfully.")
            except FileNotFoundError:
                print("File not found.")

        elif choice == 7:
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
