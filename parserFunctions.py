import calendar

import pandas as pd
from bs4 import BeautifulSoup
import dateparser
import os
import json


def createMonth():
    monthsDict = {
        'Jan': 1,
        'Feb': 2,
        'Mrz': 3,
        'Apr': 4,
        'Mai': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Okt': 10,
        'Nov': 11,
        'Dez': 12

    }
    return monthsDict


def createDataframe(file):
    soup = BeautifulSoup(file, 'html.parser')

    table_data = [[cell.text for cell in row("td")]
                  for row in soup("tr")]

    # Convert list of lists to a DataFrame
    df = pd.DataFrame(table_data)

    # Drop the first 4 rows
    df = df.iloc[5:]

    # Reset index if you want
    df = df.reset_index(drop=True)

    df.columns = ['Date', 'Day', 'Activity1', 'Activity2', 'Activity3', 'Activity4', 'Activity5', 'Activity6',
                  'Activity7', 'Activity8', 'Activity9', 'Activity10']
    return df


def getSchoolDaysFromDataframe(df):
    school_days = df[(df['Activity1'] != 'Betrieb') & (df['Activity1'] != '#NV') &
                     (df['Activity1'] != 'Betrieb/Ferien')]  # Filter activity for 'Betrieb'
    return school_days


def getOnlyDatesFromSchoolDays(school_days):
    school_days = school_days['Date']
    return school_days


def getStartingYear():
    # specify the path to your folder
    folder = 'target'

    # use os.listdir() to get a list of all files in the folder
    files = os.listdir(folder)
    year = '20' + files[0][:2]
    return year

def cleanDataFrame(df):
    df = df.dropna(subset=['Date'])  # This will remove rows where Date is None or pd.NaT
    return df
def fixDatesinDataframe(df):
    pass



def convertSchoolDaysListIntoJson(schoolDays):
    filename = 'school_days.json'
    with open(filename, 'w') as json_file:
        schoolDays.to_json(json_file, orient='records')
