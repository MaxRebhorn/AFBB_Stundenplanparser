import unittest
from datetime import datetime

from parserFunctions import Parser


class TestParserMethods(unittest.TestCase):
    def setUp(self):
        file = open('target/FI23.htm', 'r')  # provide your sample file path here
        self.Parser = Parser(file)
        self.expected_original_dataframe_shape = (500, 10)  # Modify according to your sample file

    def test_createDataframe(self):
        df = self.Parser.createDataframe('target/FI23.htm')  # provide your sample file path here
        self.assertEqual(df.shape, self.expected_original_dataframe_shape)

    def test_cleanDataFrame(self):
        original_df = self.Parser.createDataframe('target/FI23.htm')  # provide your sample file path here
        clean_df = self.Parser.cleanDataFrame(original_df)
        self.assertTrue('Dates' in clean_df.columns)

    def test_getSchulwochen(self):
        schulwochen = self.Parser.getSchulwochen()
        # check if schulwochen is of string type
        self.assertTrue(isinstance(schulwochen, str))

    def test_reformatDate(self):
        date = '06.12.23'  # provide a sample date
        reformattedDate = self.Parser.reformatDate(date)
        # check if reformattedDate is of datetime.date type
        self.assertIsInstance(reformattedDate, datetime.date)

    def test_parseStringToDateObject(self):
        dateString = '2023.12.06'  # provide a sample datestring
        dateObject = self.Parser.parseStringToDateObject(dateString)
        # check if dateObject is of datetime.date type
        self.assertIsInstance(dateObject, datetime.date)

    def test_reformatDataFrameDates(self):
        original_df = self.Parser.createDataframe('target/FI23.htm')  # provide your sample file path here
        clean_df = self.Parser.cleanDataFrame(original_df)
        reformatted_df = self.Parser.reformatDataFrameDates(clean_df)

        # check if reformatted_df's 'Dates' column is of datetime.date type
        self.assertTrue(all(isinstance(date, datetime.date) for date in reformatted_df['Dates']))


if __name__ == '__main__':
    unittest.main()
