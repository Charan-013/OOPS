class Clock:
    def __init__(self,time):
        if len(time) == 2:
            self.hours = time[0]
            # print(self.hours)
            self.minutes = time[1]
            # print(self.minutes)
        else:
            self.hours,self.minutes = map(int,time.split(":"))
        if int(self.hours) < 0 or int(self.hours) > 24:
            self.hours = 0
        if int(self.minutes) < 0 or int(self.minutes) > 60:
            self.minutes = 0

    def tic(self):
        self.minutes = self.minutes + 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours = self.hours + 1
            if self.hours == 24:
                self.hours = 0

    def toc(self, minutes):
        new_minutes = self.hours * 60 + self.minutes + minutes
        self.hours = (new_minutes // 60) % 24
        self.minutes = new_minutes % 60

    def isEarlier(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        return False

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

def main():
    method_input = input()
    cases = int(input())
    for i in range(cases):
        if method_input == "constructor(int, int)":
            inp = list(map(int,input().split(",")))
            result = Clock(inp)
            print(result)
        elif method_input == "constructor(String)":
            inp = input()
            result = Clock(inp)
            print(result)
        elif method_input == "tic()":
            inp = list(map(int,input().split(":")))
            c = Clock(inp)
            result = c.tic()
            print(c)
        elif method_input == "toc(int)":
            inp = list(map(str,input().split(",")))
            c = Clock(inp[0])
            result = c.toc(int(inp[1]))
            print(c)
        elif method_input == "isEarlierThan(Clock)":
            inp = list(map(str,input().split(",")))
            c1 = Clock(inp[0])
            c2 = Clock(inp[1])
            result = c1.isEarlier(c2)
            if result == True:
                print("true")
            else:
                print("false")

        elif method_input == "toString()":
            print("null")

if __name__ == "__main__":
    main()