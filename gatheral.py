import numpy as np
import pandas as pd
#import urllib
import urllib.request
import json
import matplotlib.pyplot as plt



# Get the data from the file
with open('dict.json') as json_file:
    data = json.load(json_file)

# Pretty print it
# print(json.dumps(data, indent=4))

act = data['optionChain']['result'][0]['options'][0]['calls']

df = pd.DataFrame()

for i in act:
    df = df.append(i, ignore_index = True)

#print(df)

#df.plot(x='strike', y='impliedVolatility') 
plt.scatter(df['strike'], df['impliedVolatility'])
plt.show()






