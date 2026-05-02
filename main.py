'''
I want do a project on MLR using oops concepts
'''
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error,r2_score
import warnings
warnings.filterwarnings("ignore")
import sys

#Creating class
class MLR:
    def __init__(self,path):
        try:

            self.path=path
            self.df=pd.read_csv(self.path)
            print(self.df)
            self.df['city'] = self.df['city'].map({'Shoreline': 0, 'Seattle': 1, 'Kent': 2, 'Bellevue': 3, 'Redmond': 4,
                                              'Maple Valley': 5, 'North Bend': 6, 'Lake Forest Park': 7, 'Sammamish': 8,
                                              'Auburn': 9, 'Des Moines': 10, 'Bothell': 11, 'Federal Way':12, 'Kirkland':13,
                                             'Issaquah':14, 'Woodinville':15, 'Normandy Park':16, 'Fall City':17, 'Renton':18,
                                             'Carnation':19, 'Snoqualmie':20, 'Duvall':21, 'Burien':22, 'Covington':23,
                                             'Inglewood-Finn Hill':24, 'Kenmore':25, 'Newcastle':26, 'Mercer Island':27,
                                             'Black Diamond':28, 'Ravensdale':29, 'Clyde Hill':30, 'Algona':31, 'Skykomish':32,
                                             'Tukwila':33, 'Vashon':34, 'Yarrow Point':35, 'SeaTac':36, 'Medina':37,
                                             'Enumclaw':38, 'Snoqualmie Pass':39, 'Pacific':40, 'Beaux Arts Village':41,
                                             'Preston':42, 'Milton':43}).astype(int)
            self.df['country']=self.df['country'].map({'USA':0}).astype(int)
            self.X=self.df.iloc[:,1:]
            self.y=self.df.iloc[:,0]
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=7)
            print(f'Training data size:{len(self.X_train)}: {len(self.y_train)}')
            print(f'Testing data size:{len(self.X_test)}:{len(self.y_test)}')
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f'error in line no :{er_line.tb_lineno} :due to :{er_type} and reason :{er_msg}')
    def training(self):
        try:
            self.reg=LinearRegression()
            self.reg.fit(self.X_train,self.y_train)
            self.y_train_prediction=self.reg.predict(self.X_train)
            print(f'Train Accuracy:{r2_score(self.y_train,self.y_train_prediction)}')
            print(f'Train Loss:{root_mean_squared_error(self.y_train,self.y_train_prediction)}')
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f'error in line no :{er_line.tb_lineno} :due to :{er_type} and reason :{er_msg}')
    def testing(self):
        try:
            self.y_test_prediction = self.reg.predict(self.X_test)
            print(f'Test Accuracy:{r2_score(self.y_test, self.y_test_prediction)}')
            print(f'Test Loss:{root_mean_squared_error(self.y_test, self.y_test_prediction)}')
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f'error in line no :{er_line.tb_lineno} :due to :{er_type} and reason :{er_msg}')
    def check_own_data(self):
        try:
            bedrooms=3
            bathrooms=1.50
            sqft_living=1340
            sqft_lot=7912
            floors=1.5
            waterfront=0
            view=0
            condition=3
            sqft_above=1340
            sqft_basement=0
            yr_built=1955
            yr_renovated=2005
            city=1
            country=0
            print(f'Own point predictions :{self.reg.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated,city,country]])}')
        except Exception as e:
            er_type,er_msg,er_line=sys.exc_info()
            print(f'error in line no :{er_line.tb_lineno} :due to :{er_type} and reason :{er_msg}')

if __name__=="__main__":
    try:
        path='House.csv'
        obj=MLR(path)
        obj.training()
        obj.testing()
        obj.check_own_data()
    except Exception as e:
        er_type,er_msg, er_line = sys.exc_info()
        print(f'error in line no :{er_line.tb_lineno} :due to :{er_type} and reason :{er_msg}')










