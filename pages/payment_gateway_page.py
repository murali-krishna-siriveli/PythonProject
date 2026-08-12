from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import LogGen

class PaymentGatewayPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def payment_page(self):

        # PayU username
        username = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter payu as username']")
            )
        )
        username.send_keys("payu")

        # PayU password
        password = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Enter payu as password']")
            )
        )
        password.send_keys("payu")

        # Submit
        submit = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@type='submit']")
            )
        )
        submit.click()

        print("Payment Gateway Login Successful")

        # Wait for Payment Successful button
        payment_success = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Simulate Success Response']")
            )
        )

        # Assertion 1
        assert payment_success.is_displayed(), \
            "Simulate Success Response button is not displayed"

         # Assertion 2
        assert payment_success.is_enabled(), \
            "Simulate Success Response button is disabled"

        payment_success.click()

        print("Simulate Success Response clicked")