import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def select_plan(self):

        # Proceed to Customise - Aspire Platinum+
        aspire_proceed = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class,'PlanVariantCard_cardRoot')]"
                    "[.//div[contains(text(),'Aspire Platinum+')]]"
                    "//button[contains(.,'Proceed to Customise')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            aspire_proceed
        )
        time.sleep(2)
        self.driver.execute_script(
            "arguments[0].click();",
            aspire_proceed
        )

        # Click View More
        view_more = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(),'View more')]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            view_more
        )
        time.sleep(1)
        self.driver.execute_script(
            "arguments[0].click();",
            view_more
        )

        time.sleep(2)

        # Click Add for Safeguard+
        safeguard_add = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(),'Safeguard+')]/ancestor::div[contains(@class,'RiderCardDesktop_addOnCardDesktop')]//button"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            safeguard_add
        )
        time.sleep(1)
        self.driver.execute_script(
            "arguments[0].click();",
            safeguard_add
        )

        # Proceed to Member Selection
        proceed_btn = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Proceed to Member Selection')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            proceed_btn
        )
        time.sleep(2)
        self.driver.execute_script(
            "arguments[0].click();",
            proceed_btn
        )