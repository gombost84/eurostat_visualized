import datetime
import json
import requests
eurostat_url = "https://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/"
datasetCode = "teina010"
response = requests.get(eurostat_url + datasetCode)

#filename = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

#class jsonMagic():    

#    def jsonPrint(object):
#        with open(filename + ".txt", 'w') as data:
#            data.write("Response:\n" + json.dumps(object, sort_keys=True, indent=" "))
    
#    def Logs(object):
#        with open(filename + "_log" + ".txt", 'w') as log:
#            log.write("Status code: " + str(object.status_code) + "\n\n" + str(object.headers))

data = json.loads(response.text)

print(data.keys())