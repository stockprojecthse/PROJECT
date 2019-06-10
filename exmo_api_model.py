class ExmoApiModel: 
    
    METHOD_TICKER = "ticker"
    FIELD_SELL_PRICE = "sell_price"
    
    def __init__(self, exmoApiRepository, currenciesPair, initialMoneyAmount):
        self.__api = exmoApiRepository
        self.__srcAmount = initialMoneyAmount
        self.__dstAmount = 0
        self.__currenciesPair = currenciesPair
        currencies = currenciesPair.split('_')
        self.__dstCurrency = currencies[0]
        self.__srcCurrency = currencies[1]
        self.__currentRate = 0
    
    def buy(self):
        if self.__srcAmount != 0 and self.__currentRate != 0:
            self.__dstAmount = self.__srcAmount / self.__currentRate
            self.__srcAmount = 0
            return True
        return False
        
    def sell(self):
        if self.__dstAmount != 0 and self.__currentRate != 0:
            self.__srcAmount = self.__dstAmount * self.__currentRate
            self.__dstAmount = 0
            return True
        return False
    
    def getSrcCurrency(self):
        return self.__srcCurrency
    
    def getDstCurrency(self):
        return self.__dstCurrency
    
    def getSrcAmount(self):
        return self.__srcAmount
    
    def getDstAmount(self):
        return self.__dstAmount
    
    def getCurrencySellPrice(self):
        self.__currentRate = float(self.getTickerForPair()[self.FIELD_SELL_PRICE])
        return self.__currentRate 
    
    def getTickerForPair(self):
        return self.getTicker()[self.__currenciesPair]
    
    def getTicker(self):
        return self.__api.callMethod(self.METHOD_TICKER)
