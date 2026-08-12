from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MedicalQuestionnairePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def skip_questionnaire(self):

        # Click Skip Questionnaire Checkbox
        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//img[@alt='checkbox']")
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkbox
        )

        # Click Confirm
        confirm_btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[.//span[normalize-space()='Confirm']]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm_btn
        )

        print("Confirm clicked")

        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Payment')]")
            )
        )

        print("Payment page loaded")

        # # Click Next
        # next_btn = self.wait.until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "//button[normalize-space()='Next']")
        #     )
        # )
        #
        # self.driver.execute_script(
        #     "arguments[0].scrollIntoView({block:'center'});",
        #     next_btn
        # )
        #
        # time.sleep(1)
        #
        # self.driver.execute_script(
        #     "arguments[0].click();",
        #     next_btn
        # )