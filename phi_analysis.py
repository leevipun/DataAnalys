import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('peak_data_01.csv')

# Extract the 'Tapahtuma' column from the DataFrame
x = df['Tapahtuma']

# Initialize variables
x1 = 0
x2 = 0
kuinkamonta = []
t2 = []
t1 = []

last = 1

for i in range(len(x)):
    if x[i] != x1:
        x1 = x[i]
        kuinkamonta.append(x2)
        x2 = 0
    else:
        x2 += 1


montamennyt = 0



for i in range(len(kuinkamonta)):
    t1 = []
    if kuinkamonta[i] < 2:
        for k in range(0, kuinkamonta[i+1]):
            t1.append(df['Transversaalinen-liike-energia'][k])
        montamennyt += kuinkamonta[i+1]+1
        t2.append(t1)
    else:
        for k in range(montamennyt, montamennyt+kuinkamonta[i]):
            t1.append(df['Transversaalinen-liike-energia'][k])
        montamennyt += kuinkamonta[i]
        t2.append(t1)
            

for i in range(len(t2)):
    plt.clf()
    x = []
    if i == 0:
        for j in range(kuinkamonta[i+1]):
            x.append(j)
    else:
        for j in range(kuinkamonta[i]):
            x.append(j)
    plt.step(x, t2[i])
    plt.xlabel('Tapahtuma')
    plt.ylabel('Transverse Momentum')
    plt.savefig('kuva'+str(i)+'.png')