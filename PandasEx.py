import pandas as pd
import numpy as np




cars = pd.Series([8323, 2312, 22132, 12345, 4344, 3243, 12342, 11434 ],
                 index=['Tlv','Jerusalem','Haifa','Bat-yam','Beer-Sheva','Petah-tikva','Holon','Acco'])
m = cars.mean()
med = cars.median()
cars_std = cars.std()

print(cars)