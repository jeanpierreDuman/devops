import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSeach(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.url = "http://localhost:8000"
        self.driver = webdriver.Firefox()

        super().__init__(methodName)
    
    def test_add_num(self):
        driver = self.driver
        driver.get(self.url)

        inputNumSendValue = "999"
        
        # Input num
        inputNum = driver.find_element(By.NAME, "num")
        inputNum.send_keys(inputNumSendValue)
        
        # Button
        button = driver.find_element(By.ID, "submit-button")
        button.click()

        # Move back
        driver.back()

        # Check value input
        inputNum = driver.find_element(By.NAME, "num")
        inputNum.get_attribute("value")
        self.assertEqual(inputNumSendValue, inputNum.get_attribute("value"))

    def test_check_value_in_list(self):
        driver = self.driver
        driver.get(self.url)

        listValue = driver.find_element(By.XPATH, "/html/body/div[1]")
        self.assertIn("999", listValue.text)

    def test_element_in_title(self):
        driver = self.driver
        driver.get(self.url)

        self.assertIn("Add", driver.title)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()