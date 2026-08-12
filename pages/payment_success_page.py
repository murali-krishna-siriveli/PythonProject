from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentSuccessPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    payment_success_message = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Payment Successful')]"
    )

    def verify_payment_success(self):
        success = self.wait.until(
            EC.visibility_of_element_located(self.payment_success_message)
        )

        assert success.is_displayed(), "Payment Successful message is not displayed"

        print("Payment Successful screen displayed")

    def capture_payment_success_screenshot(self):
            screenshot_path = "screenshots/payment_success.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"Payment Success screenshot saved: {screenshot_path}")