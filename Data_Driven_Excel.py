from selenium import webdriver
import xlrd, unittest
from ddt import ddt, data, unpack

def get_data(filename):
    rows = []
    # create an empty list to store rows
    book = xlrd.open_workbook(filename)
    # open the specified Excel spreadsheet as workbook
    sheet = book.sheet_by_index(0)
    # get the first sheet
    print('No of filled Rows in File :',sheet.nrows)
    print('No of filled Columns in File :',sheet.ncols)
    # iterate through the sheet and get data from rows in list
    # here we have taken range from 1, so it would skip 1st row and start taking value form next row.
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
        print(row_idx)
        print(sheet.row_values(row_idx, 0, sheet.ncols))
        print(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

@ddt
class SearchExcelDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com")

    @data(*get_data("datasheet.xlsx"))
    @unpack


    def test_Google_Search_FF(self, search_value, Expected_result):
        driver = self.driver
        elem = self.driver.find_element_by_id("lst-ib")
        elem.send_keys(search_value)
        elem.submit()
        print(self.driver.title)
        self.assertEqual(self.driver.title, Expected_result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()