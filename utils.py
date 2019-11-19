# TODO: Put into a function for later data retrieve
## Get the data from Yahoo and save it into a file
## Original URL for yahoo finance
## url = "https://finance.yahoo.com/quote/TSLA/options?date=1574985600&p=TSLA&straddle=false"
#
## Data URL
#url1 = "https://query1.finance.yahoo.com/v7/finance/options/TSLA?date=1574985600&straddle=false"
##url2 = "https://query2.finance.yahoo.com/v7/finance/options/{ticker}" 
#
## Get data into dict
#response = urllib.request.urlopen(url1)
#data = json.loads(response.read())
#
#json = json.dumps(data)
#
#f = open("dict.json", "w")
#f.write(json)
#f.close()

# Shorter write
#  with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile) 
 
