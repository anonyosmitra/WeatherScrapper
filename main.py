from datetime import datetime as dt
from WeatherScrapper import getDataset
country = "poland"
city = "warsaw"
start=dt(2023,9,1)
end=dt(2023,9,30)
print(getDataset(city,country,start,end))