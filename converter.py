import datetime

def timestampToUTC(timestampIn):
    result = int(timestampIn[:10])
    timestamp = datetime.datetime.utcfromtimestamp(result)
    print timestamp

timestampToTUC("1508865643712")
