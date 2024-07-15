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


def cleanDataFrame(DataFrame) -> pandas.DataFrame:
    #drop all rows until the Condition is met
    dropCondition = 'Stand: 06.12.23'
    column = 0
    mask = DataFrame[column] == dropCondition
    index = int(DataFrame[mask].index[0])
    topRemovedDataframe =DataFrame.drop(DataFrame.index[:index], inplace=True)

    #drop all rows after condition is met
    dropCondition = 'NaN'
    mask = DataFrame[column] == dropCondition
    index = int(DataFrame[mask].index[0])
    bottomRemovedDataframe = topRemovedDataframe.drop(topRemovedDataframe.index[index:], inplace=True)
    return bottomRemovedDataframe


file = open('target/FI23.htm', 'r')
pd.set_option('display.max_rows', 500)
df = createDataframe(file)
print(cleanDataFrame(df))
