from datetime import datetime as dt, datetime
from typing import List, Optional

from WeatherScrapper import scrapeBetween,writeToFile,scrapeFor
areaID="EPWA:9:PL"
#data=scrapeBetween(areaID,dt(2022,1,1),dt(2023,12,31))
data=scrapeBetween(areaID,dt(2022,1,1),dt(2022,1,31))
writeToFile(data,"warsaw")
# Phase 1: Predict state(rain,cloudy,snow)
# Phase 2: Predict season
# Phase 3: Predict future attributes(temp,ws,press,hum)
