import requests as r
import xmltodict as xtd


class EurostatConnection():

    """Class for creating connection
    to the Eurostat website and download
    either the bulk file or a target database."""

    def __init__(self):

        self.bulk_download = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=table_of_contents_en.txt"
        self.base_url = "https://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/"


    def bulklist_download(self):

        """Function for bulk download."""

        with open('bulklist.xml', 'w+', encoding = 'utf-8') as bulk_file:
            file = r.get(self.bulk_download, timeout = 10)
            bulk_file.write(file.text)
        
        with open('bulklist.xml', 'rb') as bulk_file:
            print(xtd.parse(bulk_file, process_namespaces=True))

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
