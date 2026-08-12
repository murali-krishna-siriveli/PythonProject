import time
from enum import member
from os import wait
import pyperclip

from pages import declaration_page, share_payment_page
from pages.quote_page import QuotePage
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.user_details_page import UserDetailsPage
from tests.conftest import setup
from utils.logger import LogGen

options = Options()
options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()),
#     options=options
# )
# options.add_argument("--incognito")
#
# driver.maximize_window()
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.quote_page import QuotePage
from pages.user_details_page import UserDetailsPage
from pages.member_details_page import MemberDetailsPage
from pages.medical_questionnaire_page import MedicalQuestionnairePage
from pages.share_payment_page import sharepaymentpage
from pages.declaration_page import DeclarationPage
from pages.payment_gateway_page import PaymentGatewayPage
import json
from pages.payment_success_page import PaymentSuccessPage


with open("data/test_data.json", "r") as file:
    test_data = json.load(file)
class TestQuote:

     # def test_login(self,setup):
     #    driver = setup
     #
     #    login_data = test_data["Login"]
     #    username = login_data["Username"]
     #    password = login_data["Password"]
     #    login_page = LoginPage(driver)
     #    login_page.login(username, password)

     def test_create_quote(self, setup):
         self.logger = LogGen.loggen()
         driver = setup
         self.logger.info("Test excution started")
         print("Step 1")

         login = LoginPage(driver)
         quote = QuotePage(driver)
         user_details = UserDetailsPage(driver)
         member = MemberDetailsPage(driver)
         medical = MedicalQuestionnairePage(driver)

         share_payment_page = sharepaymentpage(driver)
         declaration_page = DeclarationPage(driver)
         payment_gateway = PaymentGatewayPage(driver)
         payment_success = PaymentSuccessPage(driver)
         print("Step 2")

         # Login
         login.open()
         self.logger.info("Browser launched")

         login_data = test_data["Login"]
         username = login_data["Username"]
         password = login_data["Password"]

         login.login(username, password)
         self.logger.info("Logged in successfully")

         # OTP
         login.get_otp()
         self.logger.info("OTP completed")

         # Quote
         quote.create_quote()
         self.logger.info("Quote created")

         # User Details
         user_details.select_plan()
         self.logger.info("User details completed")

         # Member Details
         member.fill_member_details()
         self.logger.info("Member details completed")

         # Medical Questionnaire
         medical.skip_questionnaire()
         self.logger.info("Medical questionnaire completed")

         # Share Payment
         print("Starting Share Payment")

         share_payment_page.share_payment_link()

         print("Share Payment Completed")

         declaration_page.make_payment()

         self.logger.info("Declaration completed")

         payment_gateway.payment_page()

         self.logger.info("Payment page loaded")

         payment_success.verify_payment_success()
         payment_success.capture_payment_success_screenshot()




         self.logger.info("Payment successful screen verified ")

         self.logger.info("Test execution completed successfully")




# driver.get("https://insurance-agent-opt.apollo247.in/")
# wait = WebDriverWait(driver, 30)
# driver.refresh()
# button = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[text()='Sign in with Keycloak']")
#     )
# )
#
# driver.execute_script("arguments[0].click();", button)
# email = wait.until(
#     EC.visibility_of_element_located((By.ID, "username"))
# )
# email.send_keys("c.muralikrishna.siriveli@apollo247.org")
# password = wait.until(
#     EC.visibility_of_element_located((By.ID, "password"))
# )
# password.send_keys("Murali@14321")
# wait.until(
#     EC.element_to_be_clickable((By.ID, "kc-login"))
# ).click()
# # Save the application window
# main_window = driver.current_window_handle
#
# # Open Gmail
# driver.execute_script("window.open('https://mail.google.com','_blank');")
# driver.switch_to.window(driver.window_handles[1])
#
# driver.switch_to.window(driver.window_handles[1])
# # Gmail Email
# gmail_email = wait.until(
#     EC.visibility_of_element_located((By.ID, "identifierId"))
# )
# gmail_email.send_keys("c.muralikrishna.siriveli@apollo247.org")
#
# wait.until(
#     EC.element_to_be_clickable((By.ID, "identifierNext"))
# ).click()
#
# # Gmail Password
# gmail_password = wait.until(
#     EC.visibility_of_element_located((By.NAME, "Passwd"))
# )
# gmail_password.send_keys("Murali@143")
#
# wait.until(
#     EC.element_to_be_clickable((By.ID, "passwordNext"))
# ).click()
# time.sleep(5)
#
#
# # Wait for Gmail inbox
# time.sleep(5)
#
# # Click the latest OTP email
# emails = driver.find_elements(
#     By.XPATH,
#     "//span[contains(., 'Apollo247 login access code')]"
# )
#
# print("Emails found:", len(emails))
#
# driver.execute_script("arguments[0].click();", emails[0])
# import re
#
# # Read the OTP text
# email_text = wait.until(
#     EC.visibility_of_element_located(
#         (By.XPATH, "//div[contains(text(),'Access code:')]")
#     )
# ).text
#
# # Extract the 6-digit OTP
# otp = re.search(r"\d{6}", email_text).group()
#
# # Switch back to the application
# driver.switch_to.window(main_window)
#
# # Enter OTP
# otp_box = wait.until(
#     EC.visibility_of_element_located((By.ID, "emailCode"))
# )
# otp_box.clear()
# otp_box.send_keys(otp)
#
# # Click Sign In
# wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@value='Sign In']"))
# ).click()
#
# print(driver.title)
#
# time.sleep(2)
# wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Create Quote')]"))
# ).click()
#
# wait.until(
#     EC.element_to_be_clickable((By.ID, "new-customer-phone"))
# ).send_keys("8919206376")
# wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='Proceed']"))
# ).click()
# driver.execute_script("window.scrollBy(0, 500)")
# time.sleep(5)
# wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter 6 Digit pincode']"))
# ).send_keys("560037")
# driver.find_element(By.XPATH, "//input[@placeholder='Enter 6 Digit pincode']").send_keys(Keys.PAGE_DOWN)
# proceed = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[contains(.,'Proceed')]")
#     )
# )
# proceed.click()


# aspire_proceed = wait.until(
#     EC.element_to_be_clickable(
#         (
#             By.XPATH,
#             "//div[contains(@class,'PlanVariantCard_cardRoot')][.//div[contains(text(),'Aspire Platinum+')]]//button[contains(.,'Proceed to Customise')]"
#         )
#     )
# )
#
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", aspire_proceed)
# time.sleep(2)
# driver.execute_script("arguments[0].click();", aspire_proceed)
#
#
#
# # Click View More
# view_more = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//*[contains(text(),'View more')]")
#     )
# )
#
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", view_more)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", view_more)
#
# time.sleep(2)
#
# ## Click Add for Safeguard+
# safeguard_add = wait.until(
#     EC.element_to_be_clickable(
#         (
#             By.XPATH,
#             "//*[contains(text(),'Safeguard+')]/ancestor::div[contains(@class,'RiderCardDesktop_addOnCardDesktop')]//button"        )
#     )
# )
#
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", safeguard_add)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", safeguard_add)
# proceed_btn = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH, "//*[contains(text(),'Proceed to Member Selection')]")
#     )
# )
#
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", proceed_btn)
# time.sleep(2)
# driver.execute_script("arguments[0].click();", proceed_btn)




# # first_name = wait.until(
#     EC.visibility_of_element_located(
#         (By.XPATH, "//input[@placeholder='First Name']")
#     )
# )
# first_name.send_keys("Murali")
# # Last Name
# driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Krishna")
#
# # DOB
# dob = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//input[@placeholder='dd/mm/yyyy']")
#     )
# )
#
# # Open calendar
# driver.execute_script("arguments[0].click();", dob)
#
# # Select day 15 August 2001
# day = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[.//abbr[@aria-label='15 August 2001']]")
#     )
# )
#
# driver.execute_script("arguments[0].click();", day)
#
# # Click Done
# done = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[normalize-space()='Done']")
#     )
# )
#
# driver.execute_script("arguments[0].click();", done)
#
#
# # ==========================
# # Select Height - Feet = 5
# # ==========================
#
# feet_dropdown = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//input[@placeholder='Feet']")
#     )
# )
# feet_dropdown.click()
#
# wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//p[normalize-space()='6 ft']")
#     )
# ).click()# ==========================
# # Select Inches = 8
# # ==========================
#
# inches_dropdown = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//input[@placeholder='Inches']")
#     )
# )
# inches_dropdown.click()
#
# wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//p[normalize-space()='5 in']")
#     )
# ).click()
#
# # ==========================
# # Enter Weight = 70
# # ==========================
#
# weight = wait.until(
#     EC.element_to_be_clickable(
#         (By.ID, "weight")
#     )
# )
#
# weight.clear()
# weight.send_keys("65")
#
# # Click Next
# # ==========================
#
# next_btn = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[normalize-space()='Next']")
#     )
# )
#
# driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
# driver.execute_script("arguments[0].click();", next_btn)
# # # Click Skip Questionnaire Checkbox
# # ==========================
#
# checkbox = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//img[@alt='checkbox']")
#     )
# )
#
# driver.execute_script("arguments[0].click();", checkbox)
# # Click Confirm
# confirm_btn = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[.//span[normalize-space()='Confirm']]")
#     )
# )
# driver.execute_script("arguments[0].click();", confirm_btn)
#
# # ==========================
# # Click Next
# # ==========================
#
# next_btn = wait.until(
#     EC.element_to_be_clickable(
#         (By.XPATH, "//button[normalize-space()='Next']")
#     )
# )
#
# driver.execute_script("arguments[0].click();", next_btn)

#


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 
# wait = WebDriverWait(driver, 10)
# 
# checkboxes = WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located(
#         (By.XPATH, "//img[@alt='unselected']")
#     )
# )
# 
# print("Found:", len(checkboxes))
# 
# for checkbox in checkboxes:
#     driver.execute_script("arguments[0].scrollIntoView({block:'center'});", checkbox)
#     time.sleep(1)
#     driver.execute_script("arguments[0].click();", checkbox)
# 
#     buy_now = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//span[normalize-space()='Buy Now']/ancestor::button")
#         )
#     )
# 
#     driver.execute_script("arguments[0].scrollIntoView({block:'center'});", buy_now)
#     driver.execute_script("arguments[0].click();", buy_now)
# 
#     net_banking = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//div[text()='Net Banking']")
#         )
#     )
#     driver.execute_script("arguments[0].click();", net_banking)
# 
#     pay_btn = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//button[contains(text(),'Pay')]")
#         )
#     )
#     pay_btn.click()