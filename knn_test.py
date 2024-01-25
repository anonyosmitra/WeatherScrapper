from sklearn.neighbors import NearestCentroid
import numpy as np
class knnField:
    def __init__(self,name):
        self.clf = None
        self.x=[]
        self.y=[]
        self.name=name
    def add(self,d):
        data=[d.year,d.month,d.date,d.timestamp.hour,d.temp,d.windSpeed,d.pressure,d.humidity]
        self.x.append(data)
        self.y.append(self.name in d.weather)
    def make(self):
        self.clf=NearestCentroid()
        self.clf.fit(np.array(self.x),np.array(self.y))
    def predict(self,d):
        return self.clf.predict([[d.year,d.month,d.date,d.timestamp.hour,d.temp,d.windSpeed,d.pressure,d.humidity]])[0]
class knnModel:
        def __init__(self,vals):
            self.kms=[]
            for i in vals:
                self.kms.append(knnField(i))
        def add(self,d):
            for i in self.kms:
                i.add(d)
        def make(self):
            for i in self.kms:
                i.make()
        def predict(self,d):
            resp=[]
            for i in self.kms:
                if i.predict(d):
                    resp.append(i.name)
            return resp