import pandas as pd

#read_file = pd.DataFrame(pd.read_excel('arvosanakooste.xlsx'))

#read_file.to_csv('arvosanakooste.csv', index = None, header=True)

def haevsk():
    # Load the data from the CSV file
    df = pd.read_csv('arvosanakooste.csv')
    
    vsk23a = df[df['group'].eq('23a')]
    vsk23b = df[df['group'].eq('23b')]
    vsk23c = df[df['group'].eq('23c')]
    vsk23d = df[df['group'].eq('23d')]
    vsk23e = df[df['group'].eq('23e')]
    vsk23f = df[df['group'].eq('23f')]
    vsk23v = df[df['group'].eq('23v')]
    vsk21a = df[df['group'].eq('21a')]
    vsk21b = df[df['group'].eq('21b')]
    vsk21c = df[df['group'].eq('21c')]
    vsk21d = df[df['group'].eq('21d')]
    vsk21e = df[df['group'].eq('21e')]
    vsk22a = df[df['group'].eq('22a')]
    vsk22b = df[df['group'].eq('22b')]
    vsk22c = df[df['group'].eq('22c')]
    vsk22d = df[df['group'].eq('22d')]
    vsk22e = df[df['group'].eq('22e')]
    vsk22f = df[df['group'].eq('22f')]
    
    # Save the filtered DataFrame to a new CSV file
    vsk23a.to_csv('vsk23a.csv', index=False)
    vsk23b.to_csv('vsk23b.csv', index=False)
    vsk23c.to_csv('vsk23c.csv', index=False)
    vsk23d.to_csv('vsk23d.csv', index=False)
    vsk23e.to_csv('vsk23e.csv', index=False)
    vsk23f.to_csv('vsk23f.csv', index=False)
    vsk23v.to_csv('vsk23v.csv', index=False)
    vsk21a.to_csv('vsk21a.csv', index=False)
    vsk21b.to_csv('vsk21b.csv', index=False)
    vsk21c.to_csv('vsk21c.csv', index=False)
    vsk21d.to_csv('vsk21d.csv', index=False)
    vsk21e.to_csv('vsk21e.csv', index=False)
    vsk22a.to_csv('vsk22a.csv', index=False)
    vsk22b.to_csv('vsk22b.csv', index=False)
    vsk22c.to_csv('vsk22c.csv', index=False)
    vsk22d.to_csv('vsk22d.csv', index=False)
    vsk22e.to_csv('vsk22e.csv', index=False)
    vsk22f.to_csv('vsk22f.csv', index=False)  


import pandas as pd

def filter_and_save(vsk23a, vsk23b, vsk23c, vsk23d, vsk23e,
                 vsk23f, vsk23v, vsk21a, vsk21b, vsk21c,
                 vsk21d, vsk21e, vsk22a, vsk22b, vsk22c,
                 vsk22d, vsk22e, vsk22f,  columns_to_keep, file_prefix):
    # Filter the DataFrames

    vsk23a = vsk23a[columns_to_keep]
    vsk23b = vsk23b[columns_to_keep]
    vsk23c = vsk23c[columns_to_keep]
    vsk23d = vsk23d[columns_to_keep]
    vsk23e = vsk23e[columns_to_keep]
    vsk23f = vsk23f[columns_to_keep]
    vsk23v = vsk23v[columns_to_keep]
    vsk21a = vsk21a[columns_to_keep]
    vsk21b = vsk21b[columns_to_keep]
    vsk21c = vsk21c[columns_to_keep]
    vsk21d = vsk21d[columns_to_keep]
    vsk21e = vsk21e[columns_to_keep]
    vsk22a = vsk22a[columns_to_keep]
    vsk22b = vsk22b[columns_to_keep]
    vsk22c = vsk22c[columns_to_keep]
    vsk22d = vsk22d[columns_to_keep]
    vsk22e = vsk22e[columns_to_keep]
    vsk22f = vsk22f[columns_to_keep]



    # Save the filtered DataFrames to new CSV files
    vsk23a.to_csv(f'vsk23a{file_prefix}.csv', index=False)
    vsk23b.to_csv(f'vsk23b{file_prefix}.csv', index=False)
    vsk23c.to_csv(f'vsk23c{file_prefix}.csv', index=False)
    vsk23d.to_csv(f'vsk23d{file_prefix}.csv', index=False)
    vsk23e.to_csv(f'vsk23e{file_prefix}.csv', index=False)
    vsk23f.to_csv(f'vsk23f{file_prefix}.csv', index=False)
    vsk23v.to_csv(f'vsk23v{file_prefix}.csv', index=False)
    vsk21a.to_csv(f'vsk21a{file_prefix}.csv', index=False)
    vsk21b.to_csv(f'vsk21b{file_prefix}.csv', index=False)
    vsk21c.to_csv(f'vsk21c{file_prefix}.csv', index=False)
    vsk21d.to_csv(f'vsk21d{file_prefix}.csv', index=False)
    vsk21e.to_csv(f'vsk21e{file_prefix}.csv', index=False)
    vsk22a.to_csv(f'vsk22a{file_prefix}.csv', index=False)
    vsk22b.to_csv(f'vsk22b{file_prefix}.csv', index=False)
    vsk22c.to_csv(f'vsk22c{file_prefix}.csv', index=False)
    vsk22d.to_csv(f'vsk22d{file_prefix}.csv', index=False)
    vsk22e.to_csv(f'vsk22e{file_prefix}.csv', index=False)
    vsk22f.to_csv(f'vsk22f{file_prefix}.csv', index=False)


def haefys():

    vsk23a = pd.read_csv('vsk23a.csv')
    vsk23b = pd.read_csv('vsk23b.csv')
    vsk23c = pd.read_csv('vsk23c.csv')
    vsk23d = pd.read_csv('vsk23d.csv')
    vsk23e = pd.read_csv('vsk23e.csv')
    vsk23f = pd.read_csv('vsk23f.csv')
    vsk23v = pd.read_csv('vsk23v.csv')
    vsk21a = pd.read_csv('vsk21a.csv')
    vsk21b = pd.read_csv('vsk21b.csv')
    vsk21c = pd.read_csv('vsk21c.csv')
    vsk21d = pd.read_csv('vsk21d.csv')
    vsk21e = pd.read_csv('vsk21e.csv')
    vsk22a = pd.read_csv('vsk22a.csv')
    vsk22b = pd.read_csv('vsk22b.csv')
    vsk22c = pd.read_csv('vsk22c.csv')
    vsk22d = pd.read_csv('vsk22d.csv')
    vsk22e = pd.read_csv('vsk22e.csv')
    vsk22f = pd.read_csv('vsk22f.csv')
    

    columns_to_keep = ['group', 'lfy01', 'lfy02', 'lfy03', 'lfy04', 'lfy05', 'lfy06', 'lfy07', 'lfy08']
    filter_and_save(vsk23a, vsk23b, vsk23c, vsk23d, vsk23e,
                 vsk23f, vsk23v, vsk21a, vsk21b, vsk21c,
                 vsk21d, vsk21e, vsk22a, vsk22b, vsk22c,
                 vsk22d, vsk22e, vsk22f, columns_to_keep, 'Fysiikka')

def haekem():
    vsk23a = pd.read_csv('vsk23a.csv')
    vsk23b = pd.read_csv('vsk23b.csv')
    vsk23c = pd.read_csv('vsk23c.csv')
    vsk23d = pd.read_csv('vsk23d.csv')
    vsk23e = pd.read_csv('vsk23e.csv')
    vsk23f = pd.read_csv('vsk23f.csv')
    vsk23v = pd.read_csv('vsk23v.csv')
    vsk21a = pd.read_csv('vsk21a.csv')
    vsk21b = pd.read_csv('vsk21b.csv')
    vsk21c = pd.read_csv('vsk21c.csv')
    vsk21d = pd.read_csv('vsk21d.csv')
    vsk21e = pd.read_csv('vsk21e.csv')
    vsk22a = pd.read_csv('vsk22a.csv')
    vsk22b = pd.read_csv('vsk22b.csv')
    vsk22c = pd.read_csv('vsk22c.csv')
    vsk22d = pd.read_csv('vsk22d.csv')
    vsk22e = pd.read_csv('vsk22e.csv')
    vsk22f = pd.read_csv('vsk22f.csv')

    columns_to_keep = ['group', 'lke01', 'lke02', 'lke03', 'lke04', 'lke05', 'lke06']
    filter_and_save(vsk23a, vsk23b, vsk23c, vsk23d, vsk23e,
                 vsk23f, vsk23v, vsk21a, vsk21b, vsk21c,
                 vsk21d, vsk21e, vsk22a, vsk22b, vsk22c,
                 vsk22d, vsk22e, vsk22f, columns_to_keep, 'Kemia')

def haelmaa():
    vsk23a = pd.read_csv('vsk23a.csv')
    vsk23b = pd.read_csv('vsk23b.csv')
    vsk23c = pd.read_csv('vsk23c.csv')
    vsk23d = pd.read_csv('vsk23d.csv')
    vsk23e = pd.read_csv('vsk23e.csv')
    vsk23f = pd.read_csv('vsk23f.csv')
    vsk23v = pd.read_csv('vsk23v.csv')
    vsk21a = pd.read_csv('vsk21a.csv')
    vsk21b = pd.read_csv('vsk21b.csv')
    vsk21c = pd.read_csv('vsk21c.csv')
    vsk21d = pd.read_csv('vsk21d.csv')
    vsk21e = pd.read_csv('vsk21e.csv')
    vsk22a = pd.read_csv('vsk22a.csv')
    vsk22b = pd.read_csv('vsk22b.csv')
    vsk22c = pd.read_csv('vsk22c.csv')
    vsk22d = pd.read_csv('vsk22d.csv')
    vsk22e = pd.read_csv('vsk22e.csv')
    vsk22f = pd.read_csv('vsk22f.csv')

    columns_to_keep = ['group', 'lmaa02', 'lmaa03', 'lmaa04', 'lmaa05', 'lmaa06', 'lmaa07', 'lmaa08', 'lmaa09', 'lmaa10', 'lmaa11', 'lmaa12']
    filter_and_save(vsk23a, vsk23b, vsk23c, vsk23d, vsk23e,
                 vsk23f, vsk23v, vsk21a, vsk21b, vsk21c,
                 vsk21d, vsk21e, vsk22a, vsk22b, vsk22c,
                 vsk22d, vsk22e, vsk22f, columns_to_keep, 'lmaa')

def haelmab():
    vsk23a = pd.read_csv('vsk23a.csv')
    vsk23b = pd.read_csv('vsk23b.csv')
    vsk23c = pd.read_csv('vsk23c.csv')
    vsk23d = pd.read_csv('vsk23d.csv')
    vsk23e = pd.read_csv('vsk23e.csv')
    vsk23f = pd.read_csv('vsk23f.csv')
    vsk23v = pd.read_csv('vsk23v.csv')
    vsk21a = pd.read_csv('vsk21a.csv')
    vsk21b = pd.read_csv('vsk21b.csv')
    vsk21c = pd.read_csv('vsk21c.csv')
    vsk21d = pd.read_csv('vsk21d.csv')
    vsk21e = pd.read_csv('vsk21e.csv')
    vsk22a = pd.read_csv('vsk22a.csv')
    vsk22b = pd.read_csv('vsk22b.csv')
    vsk22c = pd.read_csv('vsk22c.csv')
    vsk22d = pd.read_csv('vsk22d.csv')
    vsk22e = pd.read_csv('vsk22e.csv')
    vsk22f = pd.read_csv('vsk22f.csv')

    columns_to_keep = ['group', 'lmab02', 'lmab03', 'lmab04', 'lmab05', 'lmab06', 'lmab07', 'lmab08', 'lmab09']
    filter_and_save(vsk23a, vsk23b, vsk23c, vsk23d, vsk23e,
                 vsk23f, vsk23v, vsk21a, vsk21b, vsk21c,
                 vsk21d, vsk21e, vsk22a, vsk22b, vsk22c,
                 vsk22d, vsk22e, vsk22f, columns_to_keep, 'Lmab')

def haebi():
    vsk23a = pd.read_csv('vsk23a.csv')
    vsk23b = pd.read_csv('vsk23b.csv')
    vsk23c = pd.read_csv('vsk23c.csv')
    vsk23d = pd.read_csv('vsk23d.csv')
    vsk23e = pd.read_csv('vsk23e.csv')
    vsk23f = pd.read_csv('vsk23f.csv')
    vsk23v = pd.read_csv('vsk23v.csv')
    vsk21a = pd.read_csv('vsk21a.csv')
    vsk21b = pd.read_csv('vsk21b.csv')
    vsk21c = pd.read_csv('vsk21c.csv')
    vsk21d = pd.read_csv('vsk21d.csv')
    vsk21e = pd.read_csv('vsk21e.csv')
    vsk22a = pd.read_csv('vsk22a.csv')
    vsk22b = pd.read_csv('vsk22b.csv')
    vsk22c = pd.read_csv('vsk22c.csv')
    vsk22d = pd.read_csv('vsk22d.csv')
    vsk22e = pd.read_csv('vsk22e.csv')
    vsk22f = pd.read_csv('vsk22f.csv')

    columns_to_keep = ['group', 'lbi01', 'lbi02', 'lbi03', 'lbi04', 'lbi05', 'lbi06']
    filter_and_save(vsk23a, vsk23b, vsk23c, vsk23d, vsk23e,
                 vsk23f, vsk23v, vsk21a, vsk21b, vsk21c,
                 vsk21d, vsk21e, vsk22a, vsk22b, vsk22c,
                 vsk22d, vsk22e, vsk22f, columns_to_keep, 'Lbi')


# Call the functions
haevsk()
haefys()
haekem()
haelmaa()
haebi()
haelmab()