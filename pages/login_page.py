
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import LogGen

class LoginPage:
    URL = "https://qa-insurance-agent-opt.apollo247.in/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.logger = LogGen.loggen()

    def open(self):
        self.driver.get(self.URL)

        self.driver.refresh()
    def login(self,username,password):
        self.logger.info("Logging in started")
        # login code

        # Click Keycloak Login
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[text()='Sign in with Keycloak']")
            )
        )
        self.driver.execute_script("arguments[0].click();", button)

        # Username
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

        # Login
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "kc-login"))
        ).click()

    def get_otp(self):
        # Save application window
        main_window = self.driver.current_window_handle

        # Open Gmail
        self.driver.execute_script(
            "window.open('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fservice%3Dmail%26flowName%3DGlifWebSignIn%26flowEntry%3DAccountChooser%26ec%3Dasw-gmail-globalnav-signin&dsh=S-398746652%3A1785941547375841&uj=gafb-gmail_asw-globalnav-en&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=Ac50bxtVkM2yQ6kztpJj3-34DsGqSKnB6f8FWaCTfHt3N-IXeawkP1-PvI6RLakkSymK7jnOMLKBDw');"
        )

        # Switch to Gmail tab
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # Gmail Email
        gmail_email = self.wait.until(
            EC.visibility_of_element_located((By.ID, "identifierId"))
        )
        gmail_email.send_keys("c.muralikrishna.siriveli@apollo247.org")

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "identifierNext"))
        ).click()

        # Gmail Password
        gmail_password = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "Passwd"))
        )
        gmail_password.send_keys("Murali@143")

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "passwordNext"))
        ).click()

        # Wait until Gmail Inbox opens
        # Wait for Gmail inbox
        self.wait.until(
            lambda d: "mail.google.com" in d.current_url
        )

        # Wait for OTP email
        email_locator = (
            By.XPATH,
            "//span[contains(text(),'Apollo247 login access code')]"
        )

        # Wait until at least one OTP email exists
        self.wait.until(
            EC.presence_of_element_located(email_locator)
        )

        # Get all matching emails
        emails = self.driver.find_elements(*email_locator)

        print("Emails found:", len(emails))

        # IMPORTANT: Gmail normally shows newest message/thread first
        # Use the LAST matching email element only if Gmail DOM is oldest -> newest.
        # First inspect which one is newest.
        for i, email in enumerate(emails):
            print(i, email.text)

        # Click the first result because Gmail normally sorts newest first
        latest_email = emails[0]

        self.driver.execute_script(
            "arguments[0].click();",
            latest_email
        )

        # Wait for the email body
        email_body = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Access code:')]")
            )
        )

        email_text = email_body.text

        print("Email Text:", email_text)

        # Extract OTP
        match = re.search(r"\b\d{6}\b", email_text)

        if not match:
            raise Exception("OTP not found in email body")

        otp = match.group(0)

        print("OTP:", otp)

        # Switch back to Apollo application
        self.driver.switch_to.window(main_window)

        # Enter OTP
        otp_box = self.wait.until(
            EC.visibility_of_element_located((By.ID, "emailCode"))
        )
        otp_box.clear()
        otp_box.send_keys(otp)

        # Click Sign In
        sign_in = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@value='Sign In']")
            )
        )

        self.driver.execute_script("arguments[0].click();", sign_in)

        print("Logged In Successfully")
        print(self.driver.title)

