import pandas as pd
import numpy as np

avg_list = {}

def make_average_file(files):
    for file in files:
        avg_list[file] = averageCalc(file)
    
    pd.DataFrame(avg_list, index=[0]).to_excel('pandas_data.xlsx', index=False)


        

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
    for i in range(1, len(avg)):
        if np.isnan(avg[i]):
            continue
        true_avg += avg[i]
    return true_avg/colum_len

    

avg_lista = ['vsk21aFysiikka.csv',
'vsk21aKemia.csv',
'vsk21aLbi.csv',
'vsk21almaa.csv',
'vsk21aLmab.csv',
'vsk21bFysiikka.csv',
'vsk21bKemia.csv',
'vsk21bLbi.csv',
'vsk21blmaa.csv',
'vsk21bLmab.csv',
'vsk21cFysiikka.csv',
'vsk21cKemia.csv',
'vsk21cLbi.csv',
'vsk21clmaa.csv',
'vsk21cLmab.csv',
'vsk21dFysiikka.csv',
'vsk21dKemia.csv',
'vsk21dLbi.csv',
'vsk21dlmaa.csv',
'vsk21dLmab.csv',
'vsk21eFysiikka.csv',
'vsk21eKemia.csv',
'vsk21eLbi.csv',
'vsk21elmaa.csv',
'vsk21eLmab.csv',
'vsk22aFysiikka.csv',
'vsk22aKemia.csv',
'vsk22aLbi.csv',
'vsk22almaa.csv',
'vsk22aLmab.csv',
'vsk22bFysiikka.csv',
'vsk22bKemia.csv',
'vsk22bLbi.csv',
'vsk22blmaa.csv',
'vsk22bLmab.csv',
'vsk22cFysiikka.csv',
'vsk22cKemia.csv',
'vsk22cLbi.csv',
'vsk22clmaa.csv',
'vsk22cLmab.csv',
'vsk22dFysiikka.csv',
'vsk22dKemia.csv',
'vsk22dLbi.csv',
'vsk22dlmaa.csv',
'vsk22dLmab.csv',
'vsk22eFysiikka.csv',
'vsk22eKemia.csv',
'vsk22eLbi.csv',
'vsk22elmaa.csv',
'vsk22eLmab.csv',
'vsk22fFysiikka.csv',
'vsk22fKemia.csv',
'vsk22fLbi.csv',
'vsk22flmaa.csv',
'vsk22fLmab.csv',
'vsk23aFysiikka.csv',
'vsk23aKemia.csv',
'vsk23aLbi.csv',
'vsk23almaa.csv',
'vsk23aLmab.csv',
'vsk23bFysiikka.csv',
'vsk23bKemia.csv',
'vsk23bLbi.csv',
'vsk23blmaa.csv',
'vsk23bLmab.csv',
'vsk23cFysiikka.csv',
'vsk23cKemia.csv',
'vsk23cLbi.csv',
'vsk23clmaa.csv',
'vsk23cLmab.csv',
'vsk23dFysiikka.csv',
'vsk23dKemia.csv',
'vsk23dLbi.csv',
'vsk23dlmaa.csv',
'vsk23dLmab.csv',
'vsk23eFysiikka.csv',
'vsk23eKemia.csv',
'vsk23eLbi.csv',
'vsk23elmaa.csv',
'vsk23eLmab.csv',
'vsk23fFysiikka.csv',
'vsk23fKemia.csv',
'vsk23fLbi.csv',
'vsk23flmaa.csv',
'vsk23fLmab.csv',
'vsk23vFysiikka.csv',
'vsk23vKemia.csv',
'vsk23vLbi.csv',
'vsk23vlmaa.csv',
'vsk23vLmab.csv',]
make_average_file(avg_lista)
print(avg_list)