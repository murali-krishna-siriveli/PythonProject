from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuotePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def create_quote(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Create Quote')]")
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "new-customer-phone")
            )
        ).send_keys("8919206376")

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Proceed']")
            )
        ).click()

        self.driver.execute_script("window.scrollBy(0, 500)")

        pincode = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Enter 6 Digit pincode']")
            )
        )

        pincode.send_keys("560037")
        pincode.send_keys(Keys.PAGE_DOWN)

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Proceed')]")
            )
        ).click()