import time
import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class sharepaymentpage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def share_payment_link(self):
        import time

        # Scroll down first
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        share_payment = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(),'Share Payment Link')]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            share_payment
        )
        time.sleep(5)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(),'Share Payment Link')]")
            )
        )

        self.driver.execute_script("arguments[0].click();", share_payment)
        print("Share Payment clicked")

        self.driver.execute_script(
            "arguments[0].click();",
            share_payment
        )
        time.sleep(10)

        # Click Copy Link
        # Wait until Copy Link is clickable
        copy_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Copy Link']")
            )
        )

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", copy_link)

        # Wait before clicking
        time.sleep(2)

        # Click using JavaScript
        self.driver.execute_script("arguments[0].click();", copy_link)

        # Wait for operation to complete
        time.sleep(3)

        # Wait for the payment URL to be displayed
        time.sleep(2)

        payment_url = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'https://l.apollo247.com')]"
                )
            )
        ).text

        print("Payment URL:", payment_url)

        # Open new tab
        self.driver.switch_to.new_window('tab')

        # Open payment URL
        self.driver.get(payment_url)

        time.sleep(5)
        # Wait for 3 seconds

        # Reload the current page
        self.driver.refresh()

        # Wait for the page to load
        time.sleep(5)
