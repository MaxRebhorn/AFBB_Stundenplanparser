import pandas as pd
import unittest

from parserFunctions import cleanDataFrame


class TestDataFrameClean(unittest.TestCase):

    def test_cleanDataFrame(self):
        # Setup
        data = {
            0: ['a', 'Stand: 06.12.23', 'NaN', 'b', 'c', 'd'],
            1: ['a', 'b', 'NaN', 'b', 'c', 'd'],
            3: ['a', 'b', 'NaN', 'b', 'c', 'd'],
            10: ['a', 'b', 'NaN', 'b', 'c', 'd'],
        }

        df = pd.DataFrame(data)
        clean_df = cleanDataFrame(df)

        # Checks
        self.assertIsInstance(clean_df, pd.DataFrame)
        self.assertNotIn(1, clean_df.columns)  # Check that column 1 has been removed
        self.assertNotIn(range(3, 11), clean_df.columns)  # Check that columns from 3-11 has been removed

        # Add more checks here as necessary depending on the functionality of your function


if __name__ == '__main__':
    unittest.main()
