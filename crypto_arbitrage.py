import databaseConnection as connector;
import helper
import time

def executeForever():
    main()
    time.sleep(10)

def main():
    validCurrenciesSymbol=[]
    
    """Get info from database"""
    #get platformExchangePair
    platformExchange=connector.getPlaftormExchangePair()

    #get all currencies
    currenciesValids=connector.getValidCurrencies()
    for curren in currenciesValids:
        validCurrenciesSymbol.append(curren.symbol)
    #get exchange platform
    exchangePlatform=connector.getExchangePlatform()

    #Store the timestamp of request
    connector.storeStimestamp()

    idSetOfRequest=connector.getLatestSetOfRequest()

    #possible combinations of currencies for bitfinex
    arrayOfCurrencies=helper.generateCombinations(validCurrenciesSymbol,True)


    """Get info from API"""
    jsonOfBitfinex=helper.getInfofromBitfinex(arrayOfCurrencies)
    jsonOfCexio=helper.getInfofromCexio(validCurrenciesSymbol)



    #Save info to database
    connector.persistBitfinex(jsonOfBitfinex)
    connector.persistCexio(helper.generateCombinations(validCurrenciesSymbol,False),jsonOfCexio)







if __name__ == "__main__":
    # Recursive execution
    #while True:
    #    executeForever()
    main()