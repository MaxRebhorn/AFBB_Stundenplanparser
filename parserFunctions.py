import calendar

import pandas
import pandas as pd
from bs4 import BeautifulSoup
import dateparser
import os
import json


def createDataframe(file):
    """
      This functions creates a Pandas Dataframe from an inputted file

      Parameters:
     file(file): Is the File you want to parse, it has to be a html type file

      Returns:
      list: returns a pandas Dataframe
      """
    tableDataframe = pd.read_html(file)[0]
    return tableDataframe