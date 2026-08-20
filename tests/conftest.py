import time

import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

@pytest.fixture(scope="class")
def setup():
    # Chrome options for headless environments (CI/CD)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")


    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(config["settings"]["base_url"])

    yield driver
    time.sleep(10)
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    global screenshot_path
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("setup")

        if driver:
            screenshots_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "screenshots"
            )

            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)

            driver.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved: {screenshot_path}")
            import allure
            allure.attach.file(screenshot_path, name=item.name, attachment_type=allure.attachment_type.PNG)
            print(f"\nScreenshot saved: {screenshot_path}")
            import allure
            allure.attach.file(screenshot_path, name=item.name, attachment_type=allure.attachment_type.PNG)
