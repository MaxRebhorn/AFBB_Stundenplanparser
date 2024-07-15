import calendar
import datetime

import pandas
import pandas as pd
import numpy as np
import os
import json


class Parser:
    def __init__(self,file):
        self.originalDataFrame = self.createDataframe(file)
        self.german_months_dict = {
            'Jan': '01',
            'Feb': '02',
            'Mrz': '03',
            'Apr': '04',
            'Mai': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Okt': '10',
            'Nov': '11',
            'Dez': '12'
        }

    def createDataframe(self, file):
        tableDataframe = pd.read_html(file)[0]
        return tableDataframe

    def cleanDataFrame(self,dataFrame = 'getOrignialDataFrame') -> pandas.DataFrame:
        """
              This functions creates a Cleans the Pandas Dataframe via removing unnecessary

              Parameters:
             dataFrame(pandas.Dataframe): Is the Dataframe you want to clean

              Returns:
              pandas.DataFrame: returns a pandas Dataframe with unnecessary Data removed
              """
        if dataFrame == 'getOrignialDataFrame':
            dataFrame = self.originalDataFrame
        # drop all rows until the Condition is met
        newDataFrame = dataFrame
        dropCondition = 'Stand:'
        column = 0
        mask = dataFrame[column].str.contains(dropCondition, regex=False).fillna(False)
        if mask.any():  # checks if mask has at least one True value
            index = int(dataFrame[mask].index[0])
            indexesToDrop = dataFrame.index[:index + 1]
            newDataFrame = dataFrame.drop(indexesToDrop).reset_index(drop=True)

        # drop all rows after condition is met
        dropCondition = 'NaN'
        mask = newDataFrame[column].isna()
        if mask.any():  # checks if mask has at least one True value
            index = int(newDataFrame[mask].index[0])
            numberOfRows = newDataFrame.shape[0]
            indexesToDrop = range(index, numberOfRows)
            newDataFrame = newDataFrame.drop(indexesToDrop)
            print('lel')
        indexesToDrop = range(3, 11)
        newDataFrameCleaned = newDataFrame.drop([1], axis=1)
        newDataFrameCleaned = newDataFrameCleaned.drop(newDataFrameCleaned.columns[2:12], axis=1)
        newDataFrameCleaned.rename(columns={0: 'Dates'}, inplace=True)
        newDataFrameCleaned.rename(columns={2: 'Type'}, inplace=True)

        return newDataFrameCleaned

    def reformatDataFrameDates(self, dataFrame: pandas.DataFrame) -> pandas.DataFrame:

        dataFrame['Dates'] = dataFrame['Dates'].apply(self.reformatDate)
        return dataFrame

    def getSchulwochen(self):
        schulwochen = '2024/2025'
        dataFrame = self.originalDataFrame
        mask = dataFrame[0] == 'Schulwochen'
        if mask.any():  # checks if mask has at least one True value
            index = int(dataFrame[mask].index[0])
            indexToCheck = dataFrame.index[index + 1]
            schulwochen = dataFrame.at[indexToCheck,0]
        return schulwochen

    def reformatDate(self, date: str) -> datetime.date:
        german_months_dict = {
            'Jan': '01',
            'Feb': '02',
            'Mrz': '03',
            'Apr': '04',
            'Mai': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Okt': '10',
            'Nov': '11',
            'Dez': '12'
        }
        schulwochen = self.getSchulwochen()
        # Parse Schulwochen to get year before and after January
        yearUntilJanuary = schulwochen.split('/')[0]
        yearFromJanuary = schulwochen.split('/')[1]

        # Split date into day, month and year
        day, month = date.split('. ')[0], date.split('. ')[1]

        if int(german_months_dict[month]) in range(1,7):
            year = yearFromJanuary
        else:
            year = yearUntilJanuary

        # Reformat date to [year, month, day] format
        reformattedDate = year + "." + german_months_dict[month] + "." + day

        dateObject = self.parseStringToDateObject(reformattedDate)
        return dateObject
    def parseStringToDateObject(self,dateString: str)->datetime.date:
        try:
            return datetime.datetime.strptime(dateString, "%Y.%m.%d").date()
        except ValueError:
            raise ValueError(dateString)

# Usage
file = open('target/FI23.htm', 'r')
pd.set_option('display.max_rows', 500)
Parser = Parser(file)
df = Parser.cleanDataFrame()
df = Parser.reformatDataFrameDates(df)
print(df)
