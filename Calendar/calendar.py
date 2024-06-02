def date_str(year, month, day):
    return f"{year:04d}-{month:02d}-{day:02d}"


class Calendar:
    def __init__(self, year):
        if type(year) == type(""):
            raise ValueError("The Argument Should Be an Integer")
        elif year < 1:
            raise ValueError("The Year Can't Be Less Than 1")
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

    def add_task(self, start_date, end_date, description):
        start_year, start_month, start_day = map(int, start_date.split('-'))
        end_year, end_month, end_day = map(int, end_date.split('-'))
        if (start_year, start_month, start_day) > (end_year, end_month, end_day):
            raise ValueError("Start date cannot be after end date")
        current_year, current_month, current_day = start_year, start_month, start_day
        while (current_year, current_month, current_day) <= (end_year, end_month, end_day):
            self.validate_date(current_year, current_month, current_day)
            date_key = date_str(current_year, current_month, current_day)
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
        if month > 12 or month < 1:
            raise ValueError("Invalid Date")
        elif type(month) == type(""):
            raise ValueError("Invalid Datatype")
        else:
            print(f"Tasks for {self.month_names[month - 1]} {self.year}")
            for day in range(1, self.month_days[month - 1] + 1):
                date_key = date_str(self.year, month, day)
                if date_key in self.tasks:
                    print(f"{day}: {', '.join(self.tasks[date_key])}")

    def display_week(self, start_date):
        start_year, start_month, start_day = map(int, start_date.split('-'))
        self.validate_date(start_year, start_month, start_day)
        print(f"Tasks for the week starting {start_date}")
        for _ in range(7):
            date_key = date_str(start_year, start_month, start_day)
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
        date_key = date_str(year, month, day)
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
