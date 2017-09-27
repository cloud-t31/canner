import pandas as pd
from itertools import combinations

class Read():
    def __init__(self):
        self.data = None
        self.categoty = ''
    def read_cat(self,path):
        self.category = path[:-5]
        print(self.category)
        self.data = pd.read_excel('CSO Catetogy/'+path, header=None).loc[:,0]
        self.data = self.data.dropna()
        return self.data

    def bat_data(self):
        terms = list(combinations(list(self.data),3))
        return terms




