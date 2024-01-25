import requests, json
from datetime import datetime as dt
from datetime import timedelta as td


class Obj:
    def __init__(self):
        pass
    def to_dict(self):
        r=self.__dict__
        r["time"]=self.time.strftime("%Y%m%d %H:%M")
        return r
    def loadFromDict(time, day, temp, dewPoint, heat, humidity, pressure, visibility, wc, wdir, wspd, feel, uv, condition, show_condition=True):
        o = Obj()
        o.time = dt.strptime(time,"%Y%m%d %H:%M")
        o.day = day
        o.temp = temp
        o.dewPoint = dewPoint
        o.heat = heat
        o.humidity = humidity
        o.pressure = pressure
        o.visibility = visibility
        o.wc = wc
        o.wdir = wdir
        o.wspd = wspd
        o.feel = feel
        o.uv = uv
        o.condition = None
        if show_condition:
            o.condition = condition
        return o
    def loadFromResp(payload, show_condition=True):
        o = Obj()
        o.time = dt.fromtimestamp(payload["valid_time_gmt"])
        o.day = payload["day_ind"]
        o.temp = payload["temp"]
        o.dewPoint = payload["dewPt"]
        o.heat = payload["heat_index"]
        o.humidity = payload["rh"]
        o.pressure = payload["pressure"]
        o.visibility = payload["vis"]
        o.wc = payload["wc"]
        o.wdir = payload["wdir"]
        o.wspd = payload["wspd"]
        o.feel = payload["feels_like"]
        o.uv = payload["uv_index"]
        o.condition = None
        if show_condition:
            o.condition = payload["wx_phrase"]
        return o


url = "https://api.weather.com/v1/location/EPWA:9:PL/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=m&startDate=%date"
date = dt(2016, 12, 12, 0, 0, 0)


def scrapeFor(date):
    payload = json.loads(requests.get(url.replace("%date", date.strftime("%Y%m%d"))).text)["observations"]
    data = []
    for i in payload:
        data.append(Obj.loadFromResp(i))
    return data

def scrapeBetween(start, end):
    dataset = []
    delta = td(days=1)
    while start <= end:
        dataset.extend(scrapeFor(start))
        start = start + delta
    return dataset

def writeToFile(data, name):
    for i in range(len(data)):
        if type(data[i]) == Obj:
            data[i]=data[i].to_dict()
    with open("%s.json" % name, 'w') as file:
        json.dump(data, file)


def readFromFile(name):
    with open("%s.json" % name, 'r') as file:
        data = json.load(file)
        for i in range(len(data)):
            data[i]=Obj.loadFromDict(**data[i])
        return data


#writeToFile(scrapeFor(date), "test");
print(readFromFile("test")[0].__dict__)

