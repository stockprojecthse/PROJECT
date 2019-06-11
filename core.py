from simple_math import SimpleMath
from repeated_timer import RepeatedTimer

class Core:
    
    REFRESH_INTERVAL_SEC = 10
    DATA_COUNT = 5
    MIN_DATA_COUNT_REQUIRED = 3
    OPERATION_NONE = -1
    OPERATION_SELL = 0
    OPERATION_BUY = 1
    ANGLE_OFFSET = 0.1
    
    def __init__(self, exmoApiModel):
        self.__exmoApiModel = exmoApiModel
        self.__timer = RepeatedTimer(self.REFRESH_INTERVAL_SEC, self.__step)
        self.__data = []
        self.__lastOperation = self.OPERATION_NONE
        self.__math = SimpleMath()
        self.__currentRate = 0
        self.__lastRate = 0
        self.__printCurrentBalance()
        
    def __printCurrentBalance(self):
        print("Текущий баланс: {:.2f} {:s} и {:.2f} {:s}!".format(
                self.__exmoApiModel.getSrcAmount(), 
                self.__exmoApiModel.getSrcCurrency(), 
                self.__exmoApiModel.getDstAmount(), 
                self.__exmoApiModel.getDstCurrency()))
             
    def __printCurrentRate(self):
        print("Текущий курс: {:.2f} {:s} за 1 {:s}.".format(
                self.__currentRate, 
                self.__exmoApiModel.getSrcCurrency(), 
                self.__exmoApiModel.getDstCurrency()))
         
    def __buy(self):
        result = self.__exmoApiModel.buy()
        if result:
            print("Совершена покупка по цене {:.2f} {:s}!".format(
                    self.__currentRate,
                    self.__exmoApiModel.getDstCurrency()))
            self.__printCurrentBalance()
            
    def __sell(self):
        result = self.__exmoApiModel.sell()
        if result:
            print("Совершена продажа по цене {:.2f} {:s}!".format(
                    self.__currentRate, 
                    self.__exmoApiModel.getSrcCurrency()))
            self.__printCurrentBalance()
            
    def __step(self):
        try:
            self.__currentRate = self.__exmoApiModel.getCurrencySellPrice()
            self.__data.append(self.__currentRate)
            if (len(self.__data) > self.DATA_COUNT):
                del self.__data[0]
        
            if (len(self.__data) >= self.MIN_DATA_COUNT_REQUIRED):
                angle = self.__math.getInclinationAngle(self.__data, self.REFRESH_INTERVAL_SEC)
                if angle > self.ANGLE_OFFSET:
                    if self.__lastOperation != self.OPERATION_BUY:
                        self.__lastOperation = self.OPERATION_BUY
                        self.__buy()
                elif angle < -self.ANGLE_OFFSET:
                    if self.__lastOperation != self.OPERATION_SELL:
                        self.__lastOperation = self.OPERATION_SELL
                        self.__sell()
            if round(self.__currentRate, 2) != round(self.__lastRate, 2):
                self.__printCurrentRate()
                self.__lastRate = self.__currentRate
                
        except Exception as e:
            self.__timer.stop()
            print("Ошибка: " + str(e))
        
    def start(self):
       self.__timer.start()
