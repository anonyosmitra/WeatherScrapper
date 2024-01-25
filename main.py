from datetime import datetime as dt, datetime
from typing import List, Optional
from knn_test import knnModel

from WeatherScrapper import getDataset
def match(a,b):
    for i in a:
        if i in b:
            return True
    return False
country = "poland"
city = "warsaw"
start = dt(2020, 1, 1)
end = dt(2022, 12, 31)

data = getDataset(city, country, start, end)
s={""}
for d in data:
    for i in d.weather:
        s.add(i)
s.remove("")
km=knnModel(s)
for d in data:
    km.add(d)
km.make()
start = dt(2023, 1, 1)
end = dt(2023, 10, 31)
data = getDataset(city, country, start, end)
t = a = 0
for d in data:
    t += 1
    r = km.predict(d)
    if match(r,d.weather):
        a += 1
    print("%s\t%s\t%s" % (d.weather, r, match(r,d.weather)))
print("Accuracy: %f%%" % (a * 100 / t))
print("Total: %i/%i"%(a,t))
# Phase 1: Predict state
# Phase 2: Predict season
# Phase 3: Predict future attributes(temp,ws,press,hum)
