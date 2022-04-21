from math import remainder
from tkinter import N


class time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def add(self):
        print("time 1:\n")
        self.hour1 = int(input("enter hour:"))
        self.minute1 = int(input("enter minute:"))
        self.second1 = int(input("enter second:"))

        print("time 2:\n")
        self.hour2 = int(input("enter hour:"))
        self.minute2 = int(input("enter minute:"))
        self.second2 = int(input("enter second:"))

        if(self.minute1 > 60):
            self.minute1 -= 60
            self.hour1 += 1

        elif (self.minute2 > 60):
            self.minute2 -= 60
            self.hour2 += 1

        elif(self.second1 > 60):
            self.second1 -= 60
            self.minute1 += 1

        elif (self.second2 > 60):
            self.second2 -= 60
            self.minute2 += 1

        self.hour = (self.hour1+self.hour2)
        self.minute = (self.minute1+self.minute2)
        self.second = (self.second1+self.second2)
        print("sum two times is: ", self.hour,
              ":", self.minute, ":", self.second)

    def sub(self):
        if(self.minute1 > 60):
            self.minute1 -= 60
            self.hour1 += 1

        elif (self.minute2 > 60):
            self.minute2 -= 60
            self.hour2 += 1

        elif(self.second1 > 60):
            self.second1 -= 60
            self.minute1 += 1

        elif (self.second2 > 60):
            self.second2 -= 60
            self.minute2 += 1

        self.hour = abs(self.hour1-self.hour2)
        self.minute = abs(self.minute1-self.minute2)
        self.second = abs(self.second1-self.second2)
        print("sub two times is: ", self.hour,
              ":", self.minute, ":", self.second)

    def Second(self):

        print("\nenter time for convert to second: \n")
        self.hour1 = int(input("enter hour:"))
        self.minute1 = int(input("enter minute:"))
        self.second1 = int(input("enter second:"))

        self.convert = (self.hour1*120)+(self.minute1*60)+self.second1
        print("convert time to second is: ", self.convert, "s")

    def timee(self):
        self.hour = 0
        self.minute = 0
        self.second1 = int(input("\nenter second for convert to time: "))
        while(self.second1 > 60):
            self.second1 -= 60
            self.minute += 1

            if(self.minute > 60):
                self.minute -= 60
                self.hour += 1
            else:
                continue
        print(self.hour, ":", self.minute, ":", self.second1)


the_result = time(1, 1, 1)
the_result.add()
the_result.sub()
the_result.Second()
the_result.timee()
