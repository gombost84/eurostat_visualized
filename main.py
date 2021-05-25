if __name__ == '__main__':

    import requests
    import eurostat_connections as connections
    import eurostat_json as ejson

    response = requests.get(connections.eurostatConnection.connect())
    ejson.jsonMagic.Logs(response)
    ejson.jsonMagic.jsonPrint(response.json())

else:
    print("Function__name__ is set to: {}".format(__name__))