from math import remainder
from tkinter import N


class function:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def add(self):
        while True:
            print("function 1:\n")
            self.numerator1 = int(input("enter numerator:"))
            self.denominator1 = int(input("enter denominator:"))

            print("function 2:\n")
            self.numerator2 = int(input("enter numerator:"))
            self.denominator2 = int(input("enter denominator:"))

            if (self.denominator1 == 0 or self.denominator2 == 0):
                print("program id terminated")
                break
            elif (self.denominator1 == self.denominator2):
                self.sum = (self.numerator1+self.numerator2)/self.denominator2
                print("sum functions is: ", self.sum)
                break
            else:
                self.hm = self.denominator1 * self.denominator2
                self.nn1 = self.numerator1*self.denominator2
                self.nn2 = self.numerator2*self.denominator1
                self.sum = (self.numerator1+self.numerator2)/self.denominator2
                print("sum functions is: ", self.sum)
                break

    def sub(self):
        if (self.denominator1 == 0 or self.denominator2 == 0):
            print("program id terminated")

        elif (self.denominator1 == self.denominator2):
            self.subb = abs(self.numerator1-self.numerator2)/self.denominator2
            print("sub functions is: ", self.subb)

        else:
            self.hm = self.denominator1 * self.denominator2
            self.nn1 = self.numerator1*self.denominator2
            self.nn2 = self.numerator2*self.denominator1
            self.subb = abs(self.nn1-self.nn2)/self.hm
            print("sub functions is: ", self.subb)

    def mul(self):
        if (self.denominator1 == 0 or self.denominator2 == 0):
            print("program id terminated")

        else:
            self.numerator = self.numerator1 * self.numerator2
            self.denominator = self.denominator1*self.denominator2
            print("mul functions is: ", self.numerator, "/", self.denominator)

    def div(self):
        if (self.denominator1 == 0 or self.denominator2 == 0):
            print("program id terminated")

        else:
            self.numerator = self.numerator1 * self.denominator2
            self.denominator = self.numerator2*self.denominator1
            print("div functions is: ", self.numerator, "/", self.denominator)

    def show(self):
        print("function :\n")
        self.numerator1 = int(input("enter numerator:"))
        self.denominator1 = int(input("enter denominator:"))

        if (self.denominator1 == 0 or self.denominator2 == 0):
            print("program id terminated")

        else:
            self.numerator = self.numerator1 * self.denominator2
            self.denominator = self.numerator2*self.denominator1
            print("div functions is: ", self.numerator, "/", self.denominator)


the_result = function(1/2, 1/2)
the_result.add()
the_result.sub()
the_result.mul()
the_result.div()
