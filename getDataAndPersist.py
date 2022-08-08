import databaseConnection as connector;
import BasicProvitioning.configuration as config
import helper
import time

def executeForever():
    main()
    time.sleep(config.SECONDS_TO_EXECUTE)

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

    #possible combinations of currencies for bitfinex
    arrayOfCurrencies=helper.generateCombinations(validCurrenciesSymbol,False)


    """Get info from API"""
    jsonOfBitfinex=helper.getInfofromBitfinex(helper.generateCombinations(validCurrenciesSymbol,True))
    jsonOfCexio=helper.getInfofromCexio(validCurrenciesSymbol)

    #Save info to database
    connector.persistBitfinex(jsonOfBitfinex)
    connector.persistCexio(arrayOfCurrencies,jsonOfCexio)

    for currencyToCheck in arrayOfCurrencies:
        krakenResponseDict=helper.getInfofromKraken(currencyToCheck)
        if not krakenResponseDict['error']:
            connector.persistKraken(currencyToCheck,krakenResponseDict)





if __name__ == "__main__":
    # Recursive execution
    while True:
        executeForever()
    #Only once execution
    #main()