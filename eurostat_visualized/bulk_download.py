import requests
import datetime
import json

bulk_file = requests.get("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=table_of_contents_en.txt")

filename = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

class jsonMagic(object):
    def jsonPrint(object):
        with open(filename + ".txt", 'w') as data:
            data.write(json.loads(object))

class ProcessBulk:
    def __init__(self, data):
        title, code, datatype, last_update, last_change, start, end, values = data
        self.title = title.strip('\"')
        self.code = code.strip('\"')
        self.datatype = datatype.strip('\"')
        self.last_update = last_update.strip('\"')
        self.last_change = last_change.strip('\"')
        self.start = start.strip('\"')
        self.end = end.strip('\"')
        self.values = values.strip('\"')

jsonMagic.jsonPrint(bulk_file.text)