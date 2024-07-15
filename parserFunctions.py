import calendar

import pandas
import pandas as pd
import numpy as np
import os
import json


def createDataframe(file)->pandas.DataFrame:
    """
      This functions creates a Pandas Dataframe from an inputted file

      Parameters:
     file(file): Is the File you want to parse, it has to be a html type file

      Returns:
      list: returns a pandas Dataframe
      """
    tableDataframe = pd.read_html(file)[0]
    return tableDataframe


def cleanDataFrame(dataFrame: pandas.DataFrame) -> pandas.DataFrame:
    """
          This functions creates a Cleans the Pandas Dataframe via removing unnecessary

          Parameters:
         dataFrame(pandas.Dataframe): Is the Dataframe you want to clean

          Returns:
          pandas.DataFrame: returns a pandas Dataframe with unnecessary Data removed
          """
    # drop all rows until the Condition is met
    newDataFrame = dataFrame
    dropCondition = 'Stand: 06.12.23'
    column = 0
    mask = dataFrame[column] == dropCondition
    if mask.any():  # checks if mask has at least one True value
        index = int(dataFrame[mask].index[0])
        indexesToDrop = dataFrame.index[:index +1]
        dataFrame = dataFrame.drop(indexesToDrop).reset_index(drop=True)

    # drop all rows after condition is met
    dropCondition = 'NaN'
    mask = dataFrame[column].isna()
    if mask.any():  # checks if mask has at least one True value
        index = int(dataFrame[mask].index[0])
        numberOfRows = dataFrame.shape[0]
        indexesToDrop = range(index,numberOfRows)
        newDataFrame = dataFrame.drop(indexesToDrop)
        print('lel')
    indexesToDrop = range(3,11)
    newDataFrameCleaned = newDataFrame.drop([1],axis=1)
    newDataFrameCleaned = newDataFrameCleaned.drop(newDataFrameCleaned.columns[2:12], axis = 1)

    return newDataFrameCleaned



file = open('target/FI23.htm', 'r')
pd.set_option('display.max_rows', 500)
df = createDataframe(file)
print(cleanDataFrame(df))
