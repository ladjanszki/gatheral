import numpy as np
import pandas as pd
import urllib.request
import json
import matplotlib.pyplot as plt
import datetime
from scipy.optimize import curve_fit 

import util

ticker = 'TSLA'
maturity = '2019-11-29'

## Get data from Yahoo finance and save for testing
#data = util.getData(ticker, maturity)
#nowString = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
#fileName = ticker + '__' + nowString
#data.to_csv(fileName)

# Read existing data

#df = pd.read_csv('TSLA__2019_11_19-19_29_07')
df = pd.read_csv('TSLA__2019_11_19-20_10_38')

# TODO Get rid of implied volatility undex 1E-4


# In yahoo finance implied volatility is Standard Deviation

# a = 1.0
# b = 2.0
# rho = 4.0
# m = 2.5
# sigma = 0.2
# 
# 
# K = np.arange(100, 500, 10)
# print(K)
# smile = util.rawImpVar(a, b, rho, m, sigma, K)
# 
# plt.scatter(K, smile)
# plt.show()


# Get the log-strike and implied volatility
logStrike = np.log(df['strike'].to_numpy())
impVol = df['impliedVolatility'].to_numpy()


# Fitting parameters and plot fitted model

# TODO: Think of better way to get these init params!
idx = np.argmin(impVol)
print(idx)
aInit = impVol[idx]
print(aInit)
mInit = logStrike[idx]
print(mInit)


#def rawImpVar(K, a, b, rho, m, sigma):
initParam = [0.25, 0.0, 0.0, 5.8, 0.4]
print(initParam)


params, params_covariance = curve_fit(util.rawImpVar, logStrike, impVol, p0=initParam)
print(params)

a = params[0]
b = params[1]
rho = params[2]
m = params[3]
sigma = params[4]


plt.plot(logStrike, util.rawImpVar(logStrike, a, b, rho, m, sigma))

plt.scatter(logStrike, impVol)

# The plot from the article
#tmpx = np.arange(-1.5, 1.5, 0.1)
#tmpy = util.rawImpVar(tmpx, -0.0410, 0.1331, 0.3586, 0.3060, 0.4153)
#plt.plot(tmpx, tmpy)

plt.show()






