import globalConfig as config;
import mysql.connector;
import databaseConnection as connector;
import requests
import json

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
    
    """Get info from API"""
    url_bitfinex='https://api-pub.bitfinex.com/v2/tickers?symbols=ALL'
    response_bitfinex = requests.get(url_bitfinex)
    
    if response_bitfinex.ok:
        data = response_bitfinex.text
        jsonBitFinex = json.loads(data)
    else:
        print('Error getting info from bitfinex')

    url_kraken='https://api.kraken.com/0/public/Ticker?pair='+",".join(validCurrenciesSymbol)
    response_kraken = requests.get(url_kraken)

    if response_kraken.ok:
        data_kraken = response_kraken.text
        json_kraken = json.loads(data_kraken)
    else:
        print('Error getting info from bitfinex')

    url_cexio='https://cex.io/api/tickers/'+"/".join(validCurrenciesSymbol)
    response_cexio = requests.get(url_kraken)

    if response_cexio.ok:
        data_cexio = response_cexio.text
        json_cexio = json.loads(data_cexio)
    else:
        print('Error getting info from bitfinex')


    if jsonBitFinex and json_kraken and json_cexio:
        print ('ok')
    else:
        print ('missing parameters, ending process in request: ')
    print("ended")





if __name__ == "__main__":
    main()