import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MemberDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def fill_member_details(self):

        # First Name
        first_name = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='First Name']")
            )
        )
        first_name.send_keys("Murali")

        # Last Name
        self.driver.find_element(
            By.XPATH,
            "//input[@placeholder='Last Name']"
        ).send_keys("Krishna")

        # DOB
        dob = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='dd/mm/yyyy']")
            )
        )

        # Open Calendar
        self.driver.execute_script("arguments[0].click();", dob)

        # Select Date
        day = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//abbr[@aria-label='15 August 2001']]")
            )
        )

        self.driver.execute_script("arguments[0].click();", day)

        # Click Done
        done = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Done']")
            )
        )

        self.driver.execute_script("arguments[0].click();", done)

        # Feet
        feet_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Feet']")
            )
        )
        feet_dropdown.click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[normalize-space()='6 ft']")
            )
        ).click()

        # Inches
        inches_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Inches']")
            )
        )
        inches_dropdown.click()

        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//p[normalize-space()='5 in']")
            )
        ).click()

        # Weight
        weight = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "weight")
            )
        )

        weight.clear()
        weight.send_keys("65")

        # Next
        next_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Next']")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            next_btn
        )
        self.driver.execute_script(
            "arguments[0].click();",
            next_btn
        )