import pandas as pd
import numpy as np

files = pd.read_csv('vsk23clmaa.csv')

avg = files.mean()
print(len(files.index))
print(avg)
course_list = {}
def averageCalc(csv):
    df = pd.read_csv(csv)
    pdf = df.apply(pd.to_numeric, errors='coerce')
    avg = pdf.mean()
    colum_len = 0
    for i in range(1, len(avg)):
            colum_len += 1
            if np.isnan(avg[i]):
                colum_len -= 1
    true_avg = 0
    print(avg)
    for i in range(1, len(avg)):
        if np.isnan(avg[i]):
            continue
        true_avg += avg[i]
    for i in range(1, len(pdf.columns)):
        courseName = pdf.columns[i]
        amountofPeople = 0
        for j in range(1, len(pdf.index)):
            if np.isnan(pdf[pdf.columns[i]][j]):
                continue
            amountofPeople += 1
        course_list[courseName] = amountofPeople
    print(colum_len, true_avg)
    return true_avg/colum_len

averageCalc('vsk23dlmaa.csv')
print(course_list)