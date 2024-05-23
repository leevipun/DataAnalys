import pandas as pd
import numpy as np

course_list = {}
avg_list = {}
course_list2 = {}

fy_courses_w = [
1,
1,
1,
1,
1,
1,
1,
]

ke_courses_w = [
1,
1,
1,
1,
1,
]

lmaa_courses_w = [
2,
1,
1,
1.5,
0.5,
1,
1,
1,
1
]

bi_courses_w = [
1,
1,
1,
1,
1,
]

mab_courses_w = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]

mab_courses = [
    'lmab02', 'lmab03', 'lmab04', 'lmab05', 'lmab06', 'lmab07', 'lmab08', 'lmab09'
]

maa_courses = [
    'lmaa02', 'lmaa03', 'lmaa05', 'lmaa06', 'lmaa08', 'lmaa09', 'lmaa10', 'lmaa11', 'lmaa12'
]

fy_courses = [
    'lfy01', 'lfy03', 'lfy04', 'lfy05', 'lfy06', 'lfy07', 'lfy08'
]

ke_courses = [
    'lke01', 'lke03', 'lke04', 'lke05', 'lke06'
]

bi_courses = [
    'lbi01', 'lbi02', 'lbi04', 'lbi05', 'lbi04'
]

def make_average_file(files):
    for file in files:
        avg_list[file] = averageCalc(file)
    
    pd.DataFrame(avg_list, index=[0]).to_excel('pandas_data.xlsx', index=False)
    pd.DataFrame(course_list, index=[0]).to_excel('kurssien_osallistujamäärät.xlsx', index=False)    
    pd.DataFrame(course_list, index=[0]).to_csv('kurssien_osallistujamäärät.csv', index=False)

def averageCalc(csv):
    df = pd.read_csv(csv)
    pdf = df.apply(pd.to_numeric, errors='coerce')
    true_avg = 0
    course_num = 0
    course_list2 = {}
    courseName = ''
    for i in range(1, len(pdf.columns)):
        if pdf[pdf.columns[i]].name == 'lke02' or pdf[pdf.columns[i]].name == 'lbi03' or pdf[pdf.columns[i]].name == 'lfy02' or pdf[pdf.columns[i]].name == 'lmaa04' or pdf[pdf.columns[i]].name == 'lmaa07' or pdf[pdf.columns[i]].name == 'lmab07':
            continue
        
        for j in range(0, len(pdf.index)):
            if np.isnan(pdf[pdf.columns[i]][j]):
                continue
            course_num += 1
            true_avg += pdf[pdf.columns[i]][j]
        course_list2[courseName] = calculate_w_average(true_avg, course_num, pdf.columns[i], i)
    course_list2 = {}
    for i in range(1, len(pdf.columns)+1):
        courseName = pdf.columns[i] + csv
        amountofPeople = 0
        for j in range(1, len(pdf.index)):
            if np.isnan(pdf[pdf.columns[i]][j]):
                continue
            amountofPeople += 1
        course_list[courseName] = amountofPeople
    return avg

    

def calculate_w_average(list, people, column_name, i):
    print(i-1)
    if column_name in fy_courses:
        w = fy_courses_w[i-1]
        return (list* w) / people
    if column_name in ke_courses:
        w = ke_courses_w[i-1]
        return (list* w) / people
    if column_name in maa_courses:
        w = lmaa_courses_w[i-1]
        return (list* w) / people
    if column_name in mab_courses:
        w = mab_courses_w[i-1]
        return (list* w) / people
    if column_name in bi_courses:
        w = bi_courses_w[i-1]
        return (list* w) / people
              

averageCalc('vsk21aFysiikka.csv')

#    for i in range(1, len(avg)):
 #       if np.isnan(avg[i]):
  #          continue
   #     true_avg += avg[i]
