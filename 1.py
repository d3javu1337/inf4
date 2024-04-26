class Fraction():

    @staticmethod
    def __numeratorValidator(num):
        if(type(num)==int):
            return True
        else:
            raise Exception("Введён неправильный числитель")
        
    @staticmethod
    def __denominatorValidator(den):
        if(type(den)==int and den >=0):
            return True
        else:
            raise Exception("Введён неправильный знаменатель")
        

    def __init__(self, num, den):
        if(self.__numeratorValidator(num)):
            self.__numerator = num
        if(self.__denominatorValidator(den)):
            self.__denominator = den

    def reduction(self):
        # sign = 1 if self.__numerator > 0 else -1
        den = self.__denominator
        num = abs(self.__numerator)
        while(num!=den):
            if(num-den>0):
                num-=den
            else:
                den-=num
        self.__denominator //= den
        self.__numerator //= num

    def Print(self):
        print(f"{self.__numerator} / {self.__denominator}")

    @staticmethod
    def __otherValidator(value):
        if(type(value) == Fraction):
            return True
        else:
            raise Exception("Это не дробь")

    def __add__(self, other):
        if(self.__otherValidator(other)):
            uden = self.__denominator * other.__denominator
            num = self.__numerator*other.__denominator + other.__numerator*self.__denominator
            f = Fraction(num, uden)
            f.reduction()
            return f

    def __sub__(self, other):
        if(self.__otherValidator(other)):
            uden = self.__denominator * other.__denominator
            num = self.__numerator*other.__denominator - other.__numerator*self.__denominator
            f = Fraction(num, uden)
            f.reduction()
            return f


    def __mul__(self, other):
        if(self.__otherValidator(other)):
            num = self.__numerator * other.__numerator
            den = self.__denominator * other.__denominator

    def __lt__(self, other):
        if(self.__otherValidator(other)):
            num1 = self.__numerator * other.__denominator
            num2 = other.__numerator * self.__denominator
            return num1 < num2

    def __gt__(self, other):
        if(self.__otherValidator(other)):
            num1 = self.__numerator * other.__denominator
            num2 = other.__numerator * self.__denominator
            return num1 > num2


    def __le__(self, other):
        if(self.__otherValidator(other)):
            num1 = self.__numerator * other.__denominator
            num2 = other.__numerator * self.__denominator
            return num1 <= num2

    def __ge__(self, other):
        if(self.__otherValidator(other)):
            num1 = self.__numerator * other.__denominator
            num2 = other.__numerator * self.__denominator
            return num1 >= num2

    def __eq__(self, other):
        if(self.__otherValidator(other)):
            num1 = self.__numerator * other.__denominator
            num2 = other.__numerator * self.__denominator
            return num1 == num2

    def __ne__(self, other):
        if(self.__otherValidator(other)):
            num1 = self.__numerator * other.__denominator
            num2 = other.__numerator * self.__denominator
            return num1 != num2

    



if __name__ == "__main__":
    f = Fraction(-41,82)
    f1 = Fraction(52,52)
    # f.reduction()
    f2 = f-f1
    f2.Print()