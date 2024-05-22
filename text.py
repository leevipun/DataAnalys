import pandas as pd
import numpy as np

avg_list = {}
course_list = {}

def make_average_file(files):
    for file in files:
        avg_list[file] = averageCalc(file)
    
    pd.DataFrame(avg_list, index=[0]).to_excel('pandas_data.xlsx', index=False)
    pd.DataFrame(course_list, index=[0]).to_excel('kurssien_osallistujamäärät.xlsx', index=False)    
    pd.DataFrame(course_list, index=[0]).to_csv('kurssien_osallistujamäärät.csv', index=False)

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
    for i in range(1, len(pdf.columns)):
        courseName = pdf.columns[i] + csv
        amountofPeople = 0
        for j in range(1, len(pdf.index)):
            print(pdf[pdf.columns[i]][j])
            if np.isnan(pdf[pdf.columns[i]][j]):
                continue
            amountofPeople += 1
        course_list[courseName] = amountofPeople
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

course_amount = {}

def tt_course():
     abitt = pd.read_csv('vsk21c.csv')
     kakctt = pd.read_csv('vsk22c.csv')
     kakdtt = pd.read_csv('vsk22d.csv')
     koktt = pd.read_csv('vsk23d.csv')

     kursYht = 0

     for i in range(0, len(abitt)):
        kursYht += abitt['Arvosanojen lukumäärä'][i]
     for i in range(0, len(kakctt)):
        kursYht += kakctt['Arvosanojen lukumäärä'][i]
    
     for i in range(0, len(kakdtt)):
        kursYht += kakdtt['Arvosanojen lukumäärä'][i]
     for i in range(0, len(koktt)):
        kursYht += koktt['Arvosanojen lukumäärä'][i]

     print(kursYht)
     course_amount['Tiede- ja teknologialinja'] = kursYht


def yl_course():
    abiayl = pd.read_csv('vsk21a.csv')
    kakayl = pd.read_csv('vsk22a.csv')
    kokayl = pd.read_csv('vsk23a.csv')
    kokbyl = pd.read_csv('vsk23b.csv')

    kursYht = 0

    for i in range(0, len(abiayl)):
        kursYht += abiayl['Arvosanojen lukumäärä'][i]

    for i in range(0, len(kakayl)):
        kursYht += kakayl['Arvosanojen lukumäärä'][i]

    for i in range(0, len(kokayl)):
        kursYht += kokayl['Arvosanojen lukumäärä'][i]
    
    for i in range(0, len(kokbyl)):
        kursYht += kokbyl['Arvosanojen lukumäärä'][i]

    print(kursYht)
    course_amount['Yleislinja'] = kursYht

def yt_course():
    abiyt = pd.read_csv('vsk21b.csv')
    kakytt = pd.read_csv('vsk22b.csv')
    kokytt = pd.read_csv('vsk23c.csv')

    kursYht = 0

    for i in range(0, len(abiyt)):
        kursYht += abiyt['Arvosanojen lukumäärä'][i]
    
    for i in range(0, len(kakytt)):
        kursYht += kakytt['Arvosanojen lukumäärä'][i]
    
    for i in range(0, len(kokytt)):
        kursYht += kokytt['Arvosanojen lukumäärä'][i]
    
    print(kursYht)
    course_amount['Yhteiskunta- ja talouslinja'] = kursYht

def en_course():
    abiden = pd.read_csv('vsk21d.csv')
    abien = pd.read_csv('vsk21e.csv')
    kaken = pd.read_csv('vsk22e.csv')
    kakfen = pd.read_csv('vsk22f.csv')
    koken = pd.read_csv('vsk23e.csv')
    kokfen = pd.read_csv('vsk23f.csv')

    kursYht = 0

    for i in range(0, len(abiden)):
        kursYht += abiden['Arvosanojen lukumäärä'][i]

    for i in range(0, len(abien)):
        kursYht += abien['Arvosanojen lukumäärä'][i]
    
    for i in range(0, len(kaken)):
        kursYht += kaken['Arvosanojen lukumäärä'][i]

    for i in range(0, len(kakfen)):
        kursYht += kakfen['Arvosanojen lukumäärä'][i]

    for i in range(0, len(koken)):
        kursYht += koken['Arvosanojen lukumäärä'][i]

    for i in range(0, len(kokfen)):
        kursYht += kokfen['Arvosanojen lukumäärä'][i]
    
    print(kursYht)
    course_amount['Englanninkielinen linja'] = kursYht

def makeCourse_file():
    pd.DataFrame(course_amount, index=[0]).to_excel('course_data.xlsx', index=False)
    pd.DataFrame(course_amount, index=[0]).to_csv('course_data.csv', index=False)

#tt_course()
#yl_course()
#yt_course()
#en_course()
#makeCourse_file()