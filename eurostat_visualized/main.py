if __name__ == '__main__':
    
    import eurostat_connections as ec
    import bulk_download as bd

    connection = ec.EurostatConnection()

    connection.bulklist_download()
