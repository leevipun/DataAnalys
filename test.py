import pandas as pd
import numpy as np

files = pd.read_csv('vsk23clmaa.csv')

avg = files.mean()

print(avg)