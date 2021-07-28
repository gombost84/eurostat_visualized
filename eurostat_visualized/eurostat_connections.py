class eurostatConnection():
    def connect():
        eurostat_url = "https://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/"  
        
        parameters = {
            "geo" : "EU28",
            "precision" : "1",
            "na_item" : "B1GQ",
            "unit" : "CP_MEUR",
            "time" : "2010",
            "time" : "2011"
            }

        datasetCode = "teina010" #input("Dataset: ")
        #parameters[dictkey] = input("Parameter for " + dictkey + ": ")

        return eurostat_url + datasetCode #, params = parameters

