import datetime
import json

FILENAME = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

def jsonMagic(input):
    with open(FILENAME + ".txt", 'w') as data:
        data.write(input)
    data.close()
    print(f'Data saved as {FILENAME}')

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
