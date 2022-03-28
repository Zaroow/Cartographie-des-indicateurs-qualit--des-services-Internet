import pandas as pd
from _datetime import datetime

# a) Read dataset

dataBrute = pd.read_csv("AllData.csv", sep=";")
print(dataBrute)

# b) Display dataset information
print("  * * * * * * * I)  Data information * * * * * * *  ")
print(" b1) Statistics   ")
print(dataBrute.describe())
print("______________________________________")
print(" b2) Information (Column, Non-Null, Count, Dtype)  _  info ()  ")
print(dataBrute.info())


# c) Select used Data
data_use = dataBrute[['id','sim_provider','name','location_latitude','location_longitude','status','launch_duration','trace_cellular_lte_rsrp','protocol','user_location_type','trace_cellular_bandwidth']]
# d) Encodage
status_values = {"status": {"FAILED": 0,
                                        "TIMEOUT": 1,
                                        "OK": 2
                                }
                }
data_use = data_use.replace(status_values)
print(data_use.loc[:, ["status"]])
data_use.loc[:,'quality']=''

# e) Encodage Qualité
for i in range(len(data_use)):
    print("i = ", i)
    if data_use.trace_cellular_lte_rsrp[i] >= -80:
        data_use.loc[{i},'quality'] = "Excellent"
    elif (data_use.trace_cellular_lte_rsrp[i] < -80) & (data_use.trace_cellular_lte_rsrp[i] >= -90):
        data_use.loc[{i},'quality'] = "Good"
    elif (data_use.trace_cellular_lte_rsrp[i] < -90) & (data_use.trace_cellular_lte_rsrp[i] > -100):
        data_use.loc[{i},'quality'] = "Middle Cell"
    elif data_use.trace_cellular_lte_rsrp[i] <= -100:
        data_use.loc[{i},'quality'] = "Cell Edge"
# f) we drop the irrevelant tests (status: Failed or Timeout)
data_use.drop(data_use.index[data_use['status'] == 0], inplace = True)
data_use.drop(data_use.index[data_use['status'] == 1], inplace = True)
# f) Export data
print("  * * * * * * * Export DataBrut2  * * * * * * *  ")
data_use.to_csv('SelectedData.csv', index=False, header=True, sep=";")




"""
dataframe1 = pd.read_csv("TracesdwProcedure.csv", sep=";")
dataframe2 = pd.read_csv("AllData.csv", sep=";")

frames = [dataframe1, dataframe2]
dataBrute = pd.concat(frames)
"""
"""
# d) Mis en forme dates afin que le train/test puisse aboutir
for i in range(data_use.size):
    date_time_str = data_use.start_date[i]
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


# e) replace empty values by ???
from sklearn.impute import SimpleImputer

minDownBitrate = data_use.loc[:,'DownBitrate'].min()
print(minDownBitrate)
imputer = SimpleImputer(missing_values="np.nan", strategy='constant',fill_value=int(minDownBitrate))
imputer = imputer.fit(DFdataV1.iloc[:,1:2])
DFdataV1.iloc[:,1:2]= imputer.transform(DFdataV1.iloc[:,1:2])
print(DFdataV1.DownBitrate)

data_use = data_use.replace(status_values)
print(data_use.loc[:, ["status"]])

brand_values = {"brand": {"Apple": 1,
                                        "Redmi": 2,
                                }
                }
data_use = data_use.replace(brand_values)
print(data_use.loc[:, ["brand"]])

# d) Encodage
status_values = {"status": {"FAILED": 0,
                                        "TIMEOUT": 1,
                                        "OK": 2
                                }
                }
data_use = data_use.replace(status_values)
print(data_use.loc[:, ["status"]])

"""