import numpy as np
import datetime
import urllib.request
import json
import pandas as pd

def getData(ticker, dateString):
    ''' Function to get data from Yahoo finance

    ticker: The ticker symbol for the underlying
    dateString: The maturity date in YYYY-MM-DD format as string

    Returns a pandas DataFrame of call options

    To be compatible with Yahoo finance convention a time zone adjustment have to be done
    when converting to unix time stamp

    '''

    timeZoneAdjustment = 3600
    maturity = datetime.datetime.strptime(dateString, "%Y-%m-%d").timestamp() + timeZoneAdjustment

    # Data URL
    url = 'https://query1.finance.yahoo.com/v7/finance/options/{ticker}?date={maturity}&straddle=false'.format(ticker=ticker, maturity=int(maturity))
    #url = 'https://query1.finance.yahoo.com/v7/finance/options/TSLA?date=1574985600&straddle=false'
    #url2 = "https://query2.finance.yahoo.com/v7/finance/options/{ticker}" 

    
    # Get data into dict
    response = urllib.request.urlopen(url)
    rawDict = json.loads(response.read())

    # Putting all data into a DataFrame
    optionData = rawDict['optionChain']['result'][0]['options'][0]['calls']
    df = pd.DataFrame()
    for act in optionData:
        df = df.append(act, ignore_index = True)
 
    return df
    

def rawImpVar(K, a, b, rho, m, sigma):
    term1 = np.sqrt((K - m)**2 + sigma**2)
    term2 = rho * (K - m)

    return a + b * (term1 + term2)

def naturalImpVar(K, delta, mu, rho, omega, zeta):
    term1 = 1 - rho**2
    term2 = (zeta * (K - mu) + rho)**2
    term3 = np.sqrt(term2 + term1)

    term4 = zeta * rho * (K - mu) 

    return delta + (omega / 2) * (1 + term4 + term3)
