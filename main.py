
import pandas as pd
import json
from parserFunctions import createDataframe, getSchoolDaysFromDataframe, getOnlyDatesFromSchoolDays, fixDatesinDataframe,convertSchoolDaysListIntoJson

file = open('target/FI23.html', 'r')
html_doc = file.read()
dataframe = createDataframe(html_doc)
print(dataframe['Date'])
dataframe = fixDatesinDataframe(dataframe)
daysInSchool = getSchoolDaysFromDataframe(dataframe)
datesInSchool = getOnlyDatesFromSchoolDays(daysInSchool)
convertSchoolDaysListIntoJson(datesInSchool)