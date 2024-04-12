import pandas as pd

particles = pd.read_csv('peakdata6.csv')

new_column_names = {
    'Run': 'Tapahtuma',
    'Event': 'Tapahtuma',
    'Type1': 'Tyyppi1',
    'E1': '1-Energia',
    'px1': 'X-Kulma',
    'py1': 'Y-Kulma',
    'pz1': 'Z-Kulma',
    'pt1': 'Transversaalinen-liike-energia',
    'eta1': 'Eta',
    'phi1': 'Phi',
    'Q1': 'Varaus',
    'Type2': 'Tyyppi2',
    'E2': '2-Energia',
    'px2': 'X-Kulma2',
    'py2': 'Y-Kulma2',
    'pz2': 'Z-Kulma2',
    'pt2': 'Transversaalinen-liike-energia2',
    'eta2': 'Eta2',
    'phi2': 'Phi2',
    'Q2': 'Varaus2',
    'M': 'Massa[GeV]',
}

data = particles.rename(columns=new_column_names)

def replace_m_with_mc2(csv_file_path):
    df = pd.read_csv(csv_file_path)
    c = 299792458
    df['Massa(kg)'] = (df['Massa[GeV]'] * (10**9) * 1.60217663 * (10**(-19))) / (c**2)
    df.to_csv(csv_file_path, mode='w', index=False)

def replace_phi_with_deg(csv_file_path):
    df = pd.read_csv(csv_file_path)
    df['Phi(deg)'] = df['Phi'] * 180 / 3.14159265359
    df['Phi2(deg)'] = df['Phi2'] * 180 / 3.14159265359
    df.to_csv(csv_file_path, index=False)


data.to_csv("peak_data.csv", index=False)
data.to_csv("peak_data_01.csv", index=False)


replace_m_with_mc2('peak_data_01.csv')
replace_phi_with_deg('peak_data_01.csv')