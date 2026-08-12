import time

import pytest
import os
from datetime import datetime
from selenium import webdriver
import configparser
config = configparser.ConfigParser()
config.read("config/config.ini")

@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config["settings"]["base_url"])

    yield driver
    time.sleep(10)
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
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

                print(f"\nScreenshot saved: {screenshot_path}")
            import allure
            allure.attach.file(screenshot_path, name=item.name, attachment_type=allure.attachment_type.PNG)