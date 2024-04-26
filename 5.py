class Time():
    
    @staticmethod
    def __hoursValidator(hours):
        if(type(hours) == int and 0<=hours<24):
            return True
        else:
            raise Exception("Введено некорректное значение часов")

    @staticmethod
    def __minsValidator(mins):
        if(type(mins) == int and 0<=mins<60):
            return True
        else:
            raise Exception("ведено некорректное значение минут")

    @staticmethod
    def __secValidator(sec):
        if(type(sec) == int and 0<=sec<60):
            return True
        else:
            raise Exception("ведено некорректное значение секунд")
        
    def __init__(self, hours:int, mins:int, sec:int):
        if(self.__hoursValidator(hours)):
            self.__hours = hours
        if(self.__minsValidator(mins)):
            self.__mins = mins
        if(self.__secValidator(sec)):
            self.__sec = sec

    def changeHours(self, value):
        if(self.__hoursValidator(value)):
            self.__hours += value
            self.__hours = self.__hours%24
    def changeMins(self, value):
        if(self.__minsValidator(value)):
            self.__mins += value
            if(self.__mins>=60):
                self.changeHours(self.__mins//60)
                self.__mins = self.__mins%60
            

    def changeSec(self, value):
        if(self.__secValidator(value)):
            self.__sec += value
            if(self.__sec>=60):
                self.changeMins(self.__sec//60)
                self.__sec = self.__sec%60

    def setHours(self, value):
        if(self.__hoursValidator(value)):
            self.__hours = value

    def setMins(self, value):
        if(self.__minsValidator(value)):
            self.__mins = value

    def setSec(self, value):
        if(self.__secValidator(value)):
            self.__sec = value


    def getHours(self):
        return self.__hours

    def getMins(self):
        return self.__mins

    def getSec(self):
        return self.__sec
if __name__ == "__main__":
    t = Time(23,40,30)
    print(f"{t.getHours()} {t.getMins()} {t.getSec()}")
    t.changeHours(10)
    print(f"{t.getHours()} {t.getMins()} {t.getSec()}")
    t.changeMins(30)
    print(f"{t.getHours()} {t.getMins()} {t.getSec()}")
    t.changeSec(40)
    print(f"{t.getHours()} {t.getMins()} {t.getSec()}")