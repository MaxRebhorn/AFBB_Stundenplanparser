import unittest
import pandas as pd
from parserFunctions import createDataframe  # change 'your_module' to the name of your Python file


class TestCreateDataframe(unittest.TestCase):
    def test_create_dataframe(self):
        # create a simple HTML file for testing
        html_content = """
        <table>
        <tr>
        <th>Name</th>
        <th>Age</th>
        </tr>
        <tr>
        <td>John</td>
        <td>30</td>
        </tr>
        <tr>
        <td>Jane</td>
        <td>25</td>
        </tr>
        </table>
        """
        with open('test.html', 'w') as f:
            f.write(html_content)

        df = createDataframe('test.html')

        expected_data = {'Name': ['John', 'Jane'], 'Age': [30, 25]}
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal(df, expected_df)


if __name__ == '__main__':
    unittest.main()
