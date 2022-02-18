import requests as r
import xmltodict as xtd


class EurostatConnection():

    def __init__(self):
        
        self.bulk_download = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&file=table_of_contents.xml"
        self.base_url = "https://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/"


    def bulklist_download(self):

        with open('bulklist.xml', 'w+', encoding = 'utf-8') as f:
            file = r.get(self.bulk_download)
            f.write(file.text)

    #def connect(self):
        
    #    parameters = {
    #        "geo" : "eu28",
    #        "precision" : "1",
    #        "na_item" : "b1gq",
    #        "unit" : "cp_meur",
    #        "time" : "2010",
    #        "time" : "2011"
    #        }

    #    datasetcode = "teina010" #input("dataset: ")
    #    #parameters[dictkey] = input("parameter for " + dictkey + ": ")

    #    return self.url + datasetcode #, params = parameters

