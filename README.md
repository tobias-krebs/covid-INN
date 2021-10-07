# covid-INN
 Parameter estimation using INNs
 
 This repo contains the code base for the final project of the advance machine learning lecture held by Ullrich Köthe at the Heidelberg university in the summer semester 2021. If you are interested in the associated report, feel free to email us.
 
 create_data.py can be used to generate more training data. This uses the code in covid_abs taken from https://bit.ly/COVID19_ABSsystem.
 Also included is the FrEIA package from https://github.com/VLL-HD/FrEIA with some modifications described in the report.
 
 We additionally include the owid-covid-data.csv which contains real word statistics of the covid pandemic taken from https://github.com/owid/covid-19-data/tree/master/public/data, downloaded on the 6.10.21 to test our models on real data.
 
 We only include subsets of our used training data, as the whole sets were too large to upload here. With the included subsets, at least the notebooks can be executed however results may be different from what we present in the report due to the lower statistics. 
 
 There is a notebook for every data set used, labeled accordingly set_1 to set_3 and toy_problem. All further details on what exactly was the difference between the data sets and parameters to recreate them using create_data.py are also included in the report.
