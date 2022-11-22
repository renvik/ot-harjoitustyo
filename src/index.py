#import cowsay
import requests
#import pandas as pd
#from tabulate import tabulate

r = requests.get('https://rata.digitraffic.fi/api/v1/trains/2017-01-01/1')
print(r.status_code)
print(r.json())

