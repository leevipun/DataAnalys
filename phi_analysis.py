import pandas as pd
import matplotlib.pyplot as plt
import aspose.words as aw
# Read the CSV file into a DataFrame
df = pd.read_csv('peak_data_01.csv')

# Extract the 'Tapahtuma' column from the DataFrame
x = df['Tapahtuma']
x_cord1 = df['X-Kulma']
x_cord2 = df['X-Kulma2']
y_cord1 = df['Y-Kulma']
y_cord2 = df['Y-Kulma2']
z_cord1 = df['Z-Kulma']
z_cord2 = df['Z-Kulma2']

# Initialize variables
x1 = 0
x2 = 0
kuinkamonta = []
t2 = []
t1 = []


x_c1 = []
x_c2 = []
x_tc1 = []
x_tc2 = []

y_c1 = []
y_c2 = []
y_tc1 = []
y_tc2 = []

z_c1 = []
z_c2 = []
z_tc1 = []
z_tc2 = []

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
    x_c1 = []
    x_c2 = []
    y_c1 = []
    y_c2 = []
    z_c1 = []
    z_c2 = []
    if kuinkamonta[i] < 2:
        for k in range(0, kuinkamonta[i+1]):
            t1.append(df['Transversaalinen-liike-energia'][k])
            x_c1.append(df['X-Kulma'][k])
            x_c2.append(df['X-Kulma2'][k])
            y_c1.append(df['Y-Kulma'][k])
            y_c2.append(df['Y-Kulma2'][k])
            z_c1.append(df['Z-Kulma'][k])
            z_c2.append(df['Z-Kulma2'][k])
        montamennyt += kuinkamonta[i+1]+1
        t2.append(t1)
        x_tc1.append(x_c1)
        x_tc2.append(x_c2)
        y_tc1.append(y_c1)
        y_tc2.append(y_c2)
        z_tc1.append(z_c1)
        z_tc2.append(z_c2)
    else:
        for k in range(montamennyt, montamennyt+kuinkamonta[i]):
            t1.append(df['Transversaalinen-liike-energia'][k])
            x_c1.append(df['X-Kulma'][k])
            x_c2.append(df['X-Kulma2'][k])
            y_c1.append(df['Y-Kulma'][k])
            y_c2.append(df['Y-Kulma2'][k])
            z_c1.append(df['Z-Kulma'][k])
            z_c2.append(df['Z-Kulma2'][k])
        montamennyt += kuinkamonta[i]
        t2.append(t1)
        x_tc1.append(x_c1)
        x_tc2.append(x_c2)
        y_tc1.append(y_c1)
        y_tc2.append(y_c2)
        z_tc1.append(z_c1)
        z_tc2.append(z_c2)

def create_tra_analysis(x, i, t2):
    plt.step(x, t2[i])
    plt.xlabel('Tapahtuma')
    plt.ylabel('Transverse Momentum')
    plt.savefig('kuva'+str(i)+'.png')
    plt.clf()

def create_x_analysis(x, i):
    plt.scatter(x, x_tc1[i])
    plt.scatter(x, x_tc2[i])
    plt.xlabel('Tapahtuma')
    plt.ylabel('X-Kulma')
    plt.savefig('kuvax'+str(i)+'.png')
    plt.clf()

def create_y_analysis(x, i):
    plt.scatter(x, y_tc1[i])
    plt.scatter(x, y_tc2[i])
    plt.xlabel('Tapahtuma')
    plt.ylabel('Y-Kulma')
    plt.savefig('kuvay'+str(i)+'.png')
    plt.clf()
def create_z_analysis(x, i):
    plt.scatter(x, z_tc1[i])
    plt.scatter(x, z_tc2[i])
    plt.xlabel('Tapahtuma')
    plt.ylabel('Z-Kulma')
    plt.savefig('kuvaz'+str(i)+'.png')
    plt.clf()
            
def create_analysis_graphs():
    for i in range(len(t2)):
        plt.clf()
        x = []
        if i == 0:
            for j in range(kuinkamonta[i+1]):
                x.append(j)
        else:
            for j in range(kuinkamonta[i]):
                x.append(j)
        create_tra_analysis(x, i, t2)
        create_x_analysis(x, i)
        create_y_analysis(x, i)
        create_z_analysis(x, i)

def create_analysis_tra_interval(interval):
    last = 0
    for i in range(len(t2)):
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
        if i == last + interval:
            plt.savefig('f'+str(i)+'.png')
            last = i
            plt.clf()
        elif i == 63:
            plt.savefig('f'+str(i)+'.png')
            plt.clf()

# Create the analysis graphs
create_analysis_graphs()
# Create the analysis graphs with 5 interval
create_analysis_tra_interval(5)