class DateADT:
    leap_years = [ele for ele in range(0,3000,4)]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, *args):
        self.year = 0
        self.month = 0
        self.day = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        if len(args) == 3:
            self.year, self.month, self.day = map(int, args)
        elif len(args) == 6:
            self.year, self.month, self.day, self.hours, self.minutes, self.seconds = map(int, args)
        elif len(args) == 1:
            args1 = args[0].split(" ")
            self.year, self.month, self.day = map(int, args1[0].split("-"))
            self.hours, self.minutes, self.seconds = map(int, args1[1].split(":"))

        self.correctDateTime()

    def correctDateTime(self):
        if self.month > 11:
            raise ValueError
        if (self.day == 29 and self.month == 1 and self.year not in DateADT.leap_years) or self.day > 31:
            raise ValueError 
        if self.hours < 0 or self.hours > 23:
            raise ValueError
        if self.minutes < 0 or self.minutes > 59:
            raise ValueError
        if self.seconds < 0 or self.seconds > 60:
            raise ValueError

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def setYear(self,year):
        self.year = year
        self.correctDateTime()

    def setMonth(self,month):
        self.month = month
        self.correctDateTime()

    def setDay(self,day):
        self.day = day
        self.correctDateTime()

    def setHours(self,hours):
        self.hours = hours
        self.correctDateTime()

    def setMinutes(self,minutes):
        self.minutes = minutes
        self.correctDateTime()

    def setSeconds(self,seconds):
        self.seconds = seconds
        self.correctDateTime()

    def before(self, other):
        return self.getTime() < other.getTime()

    def after(self, other):
        return self.getTime() > other.getTime()

    def max_days_in_month(self, year, month):
        if year in DateADT.leap_years:
            return self.days_leap_year[month]
        return self.days[month]
    
    def getTime(self):
        total_days = 0
        for y in range(1970, self.year):
            if y in DateADT.leap_years:
                total_days += 366
            else:
                total_days += 365
        for m in range(self.month):
            total_days += self.max_days_in_month(self.year, m)
        total_days += self.day - 1

        total_ms = total_days * 24 * 60 * 60 * 1000
        total_ms += self.hours * 60 * 60 * 1000
        total_ms += self.minutes * 60 * 1000
        total_ms += self.seconds * 1000

        return total_ms

    def setTime(self, ms):
        total_seconds = ms // 1000
        remaining_ms = ms % 1000

        total_days = total_seconds // (24 * 60 * 60)
        remaining_seconds = total_seconds % (24 * 60 * 60)

        self.hours = remaining_seconds // 3600
        remaining_seconds %= 3600

        self.minutes = remaining_seconds // 60
        self.seconds = remaining_seconds % 60

        self.year = 1970
        while True:
            if self.year in DateADT.leap_years:
                days_in_year = 366
            else:
                days_in_year = 365
            if total_days < days_in_year:
                break
            total_days -= days_in_year
            self.year += 1

        self.month = 0
        while total_days >= self.max_days_in_month(self.year, self.month):
            total_days -= self.max_days_in_month(self.year, self.month)
            self.month += 1

        self.day = total_days + 1

    def toString(self):
        return (
            f"{self.year:04d}-{self.month:02d}-{self.day:02d} "
            f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        )
# if __name__ == "__main__":
#     date1 = DateADT(2023, 2, 28)
#     date2 = DateADT("2024-01-15 13:45:50")
#     print(date1.toString(),date2.toString())
#     # print("Is date1 before date2?", date1.before(date2))