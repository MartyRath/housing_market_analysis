import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Leinster = pd.read_csv(r'C:\Users\User\PycharmProjects\MartyRath\Leinster_PPR_2010-2020.csv')
inflation = pd.read_csv(r'C:\Users\User\PycharmProjects\MartyRath\Inflation.csv')
Leinster_budget=Leinster[Leinster['SALE_PRICE']<110000]


