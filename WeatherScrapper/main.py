import requests, json, re
from datetime import timedelta as td
from datetime import datetime as dt


class obj:
    def __init__(self, date, data):
        self.year = date.year
        self.month = date.month
        self.date = date.day
        self.timestamp = data["c"][0]["h"][:5].split(":")
        self.timestamp = dt(date.year, date.month, date.day, int(self.timestamp[0]), int(self.timestamp[1]))
        self.hour = self.timestamp.hour
        self.minute = self.timestamp.minute
        print(self.timestamp.strftime("%d/%m/%Y %H:%M"))
        self.temp = int(data['c'][2]['h'][:data['c'][2]['h'].find("&")])
        print(str(self.temp) + "°C")
        self.weather = data["c"][3]["h"][:-1]
        print(self.weather)
        self.windSpeed = data["c"][4]["h"][:data["c"][4]["h"].find(" ")]
        if self.windSpeed == "No":
            self.windSpeed = 0
        else:
            self.windSpeed = int(self.windSpeed)
        self.humidity = int(data["c"][6]['h'][:-1])
        self.pressure = int(data['c'][7]['h'][:data['c'][7]['h'].find(" ")])
        self.visibility = data['c'][8]['h'][:data['c'][8]['h'].find("&")]
        if self.visibility == "N/":
            self.visibility = None
        else:
            self.visibility = int(self.visibility)
urlTemp = "https://www.timeanddate.com/scripts/cityajax.php?n=%country/%city&mode=historic&hd=%d&month=%m&year=%y&json=1"


def getForDate(city, country, date):
    a = urlTemp.replace("%country", country)
    a = a.replace("%city", city)
    a = a.replace("%d", date.strftime("%Y%m%d"))
    a = a.replace("%y", str(date.year))
    a = a.replace("%m", str(date.month))
    print(a)
    resp = (requests.get(a)).text
    print(resp)
    resp = re.sub(r'(?<![0-9"])(\w+|"\d+"):', lambda match: f'"{match.group(1)}":', resp)
    resp = json.loads(resp)
    dataset = []
    for i in resp:
        dataset.append(obj(date, i))
    return dataset


def getDataset(city, country, fromDate, toDate):
    dataset = []
    delta = td(days=1)
    while fromDate <= toDate:
        dataset.extend(getForDate(city, country, fromDate))
        fromDate = fromDate + delta
    return dataset
