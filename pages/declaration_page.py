import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DeclarationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def make_payment(self):

        print("Declaration page URL:", self.driver.current_url)

        # Give payment-link page time to load
        time.sleep(5)

        # Wait for declaration checkboxes
        checkboxes = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//img[@alt='unselected']")
            )
        )

        print("Found:", len(checkboxes))

        # Click all checkboxes
        for checkbox in checkboxes:

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                checkbox
            )

            time.sleep(1)

            self.driver.execute_script(
                "arguments[0].click();",
                checkbox
            )

        print("All declaration checkboxes clicked")

        # Click Buy Now
        buy_now = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[normalize-space()='Buy Now']/ancestor::button"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            buy_now
        )

        time.sleep(1)

        self.driver.execute_script(
            "arguments[0].click();",
            buy_now
        )

        print("Buy Now clicked")

        # Select Net Banking
        net_banking = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Net Banking']")
            )
        )

        net_banking.click()

        print("Net Banking selected")

        # Click Pay button
        pay_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Pay')]")
            )
        )

        pay_btn.click()

        print("Pay button clicked")

        time.sleep(8)

        # Switch to new window if opened
        windows = self.driver.window_handles

        print("Windows:", windows)

        if len(windows) > 1:
            self.driver.switch_to.window(windows[-1])
            print("Switched to payment window")
        else:
            print("Payment opened in same window")