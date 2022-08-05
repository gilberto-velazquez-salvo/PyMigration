import itertools
import requests
import json


def generateCombinations(validCurrenciesSymbol,isBitfinex):        
    #possible combinations of currencies for bitfinex

    arrayOfConmutations=[]
    permutations = list(itertools.permutations(validCurrenciesSymbol, r=2))
    for permutation in permutations:
        if isBitfinex:
            arrayOfConmutations.append('t'+permutation[0]+permutation[1])
        else:
            arrayOfConmutations.append(permutation[0]+permutation[1])
    
    return arrayOfConmutations


    
def getInfofromBitfinex(arrayOfCurrencies):
    url_bitfinex='https://api-pub.bitfinex.com/v2/tickers?symbols='+",".join(arrayOfCurrencies)
    response_bitfinex = requests.get(url_bitfinex)
    
    if response_bitfinex.ok:
        data = response_bitfinex.text
        return json.loads(data)
    else:
        print('Error getting info from bitfinex')

def getInfofromCexio(validCurrenciesSymbol):
    url_cexio='https://cex.io/api/tickers/'+"/".join(validCurrenciesSymbol)
    response_cexio = requests.get(url_cexio)
    
    if response_cexio.ok:
        data = response_cexio.text
        return json.loads(data)
    else:
        print('Error getting info from cex.io')

