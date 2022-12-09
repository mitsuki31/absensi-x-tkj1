## ::: Importing Packages ::: ##
# -> System Packages
import os
import platform
import numpy as np
import pandas as pd

# -> Local Packages
from colors import *


## ::: Read CSV File ::: ##
absence = pd.read_csv('absen_xtkj1.csv').convert_dtypes(int)  # -> Read & convert all float to integer
absence.set_index('ID', inplace=True)


## ::: Info Variables ::: ##
# -> These variables still object instead str, so convert 1st
absence_desc = absence.describe()
absence_presence = absence['Presence'].sum()
absence_sick = absence['Sick'].sum()
absence_permite = absence['Permite'].sum()
absence_alfa = absence['Alfa'].sum()
absence_len = len(absence.index)
    
header_class = absence.loc[absence.index.min()]['Name']
    
# -> Still object, not str
min_presence = absence['Presence'].min()
max_presence = absence['Presence'].max()
max_sick = absence['Sick'].max()
max_permite = absence['Permite'].max()
max_alfa = absence['Alfa'].max()
all_alfa = [max_alfa, (absence[(absence['Alfa'] < max_alfa) & (absence['Alfa'] != 0)]['Alfa'].values[0])]
    
choice = ['Presence', 'Permite', 'Sick', 'Alfa']
    
# -- Lowest Presence Name
presence_low = absence[absence['Presence'] == min_presence]['Name']
presence_low = presence_low[(presence_low.index)[0]]
    
# -- Highest Sick Name
sick_high = absence[absence['Sick'] == max_sick]['Name']
sick_high = sick_high[(sick_high.index)[0]]
    
# -- Highest Permite Name
permite_high = absence[absence['Permite'] == max_permite]['Name']
permite_high = permite_high[(permite_high.index)[0]]
    
# -- Highest Alfa Name
alfa_high = absence[absence['Alfa'] == max_alfa]['Name']
alfa_high = alfa_high[(alfa_high.index)[0]]
    
alfa_otherhigh = absence[(absence['Alfa'] < max_alfa) & (absence['Alfa'] != 0)]['Name']
alfa_otherhigh = alfa_otherhigh[(alfa_otherhigh.index)[0]]


## ::: Output Text ::: ##
def all_info():
    print(str(absence), '\n')
    print('Info:')
    absence.info()
    print('\nDescription:', str(absence_desc) + '\n',
        '{}Month / Year\t: {}{}'.format(clrwhite,
                                        clrpurple,
                                        str(absence['Month'][1])),
        '{}Head of Class\t: {}{}{}'.format(clrwhite,
                                           clrblue2,
                                           str(header_class),
                                           clrdefault),
        '{}Total\t\t: {} student(s)'.format(clrwhite, str(absence_len)),
        '{}Presence\t: {} (total)\n....Highest\t: {}\n{}....Lowest\t: {}\n......Name\t: {}'.format(clrgreen,
                                                                                                   str(absence_presence),
                                                                                                   max_presence,
                                                                                                   clrred,
                                                                                                   min_presence,
                                                                                                   presence_low),
        '{}Sick\t\t: {} (total)\n....Highest\t: {}\n......Name\t: {}'.format(clryellow,
                                                                             str(absence_sick),
                                                                             max_sick,
                                                                             sick_high),
        '{}Permite\t\t: {} (total)\n....Highest\t: {}\n......Name\t: {}'.format(clrblue,
                                                                                str(absence_permite),
                                                                                max_permite,
                                                                                permite_high),
        '{}Alfa\t\t: {} (total)\n....Highest\t: {}\n......Name\t: {}'.format(clrred,
                                                                             str(absence_alfa),
                                                                             max_alfa,
                                                                             alfa_high),
        '{}....2nd Highest\t: {}\n......Name\t: {}{}'.format(clrred,
                                                             all_alfa[1],
                                                             alfa_otherhigh,
                                                             clrdefault),
        sep='\n', end='\n'*2)
        
def absences():
    print(absence)

def absences_desc():
    print(absence_desc)

def absences_info():
    absence.info()
        
def total_students():
    print(absence_len)

def head_class():
    print(f'Head of Class\t: {str(header_class)}')
    
def absence_month():
    print('Month / Year\t: {}'.format(str(absence['Month'][1])))

## ::: Data Visual ::: ##
def _show(set = False, index: int = 0):
    try:
        if not set:
            return 1
        else:
            import matplotlib.pyplot as plt
        
        ## ::: Settings Data Visual ::: ##
        plt.figure(figsize=[9*2, 24])  # -> Figure size (x, y)
        plt.barh(absence['Name'][::-1], absence[choice[index]][::-1])  # -> Make a horizontal bar
        plt.title(choice[index], size=24)  # -> Title figure
        plt.xlabel(None)  # -> X label
        plt.ylabel('Name', size=20)  # -> Y label
        
        ## ::: Showing Data Visual ::: ##
        plt.show()
    except:
        pass


if __name__ == '__main__':
    all_info()
    absences_desc()
    total_students()
