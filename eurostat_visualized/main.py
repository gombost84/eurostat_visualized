if __name__ == '__main__':

    import requests as r
    from eurostat_connections import EurostatConnection
    import bulk_download

    response = r.get(con.eurostatConnection.connect())

    if response.status_code == 200:
        print('It went ok.')
        bd.jsonMagic(response.text)
    else:
        print(f'Something went wrong. The error code is: {response.status_code}')