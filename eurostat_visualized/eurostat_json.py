import datetime
import json
import requests
eurostat_url = "https://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/"
datasetCode = "teina010"
response = requests.get(eurostat_url + datasetCode)

data = json.loads(response.text)

countries = {'title': str(data['label']),
             'countries': dict(data['dimension']['geo']['category']['label'])
             }