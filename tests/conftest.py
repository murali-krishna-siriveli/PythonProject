import time
import os
from datetime import datetime
import configparser

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Read configuration
config = configparser.ConfigParser()
config.read("config/config.ini")


@pytest.fixture(scope="class")
def setup():
    chrome_options = Options()

    # Detect if running in CI environment
    is_ci = os.getenv("CI") or os.getenv("GITHUB_ACTIONS")

    if is_ci:
        # CI/Headless configuration
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-translate")
        chrome_options.add_argument("--disable-background-networking")
        chrome_options.add_argument("--disable-client-side-phishing-detection")
        chrome_options.add_argument("--disable-component-update")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--start-maximized")

    # Common arguments for both local and CI
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Initialize driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Add implicit wait - critical for CI environments
    driver.implicitly_wait(15)

    # Maximize window for local, already set for CI via arguments
    if not is_ci:
        driver.maximize_window()

    # Open application with retry logic for CI
    max_retries = 3
    for attempt in range(max_retries):
        try:
            driver.get(config["settings"]["base_url"])
            time.sleep(3)  # Allow page to fully load
            break
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                time.sleep(2)
            else:
                raise

    yield driver

    # Keep browser open for verification (local only)
    if not is_ci:
        time.sleep(10)

    # Close browser
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Take screenshot after test execution
    if report.when == "call":
        driver = item.funcargs.get("setup")

        if driver:
            # Create screenshots directory
            screenshots_dir = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                "screenshots"
            )

            os.makedirs(screenshots_dir, exist_ok=True)

            # Create timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Screenshot path
            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{timestamp}.png"
            )

            # Take screenshot
            try:
                driver.save_screenshot(screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")

                # Attach screenshot to Allure report
                allure.attach.file(
                    screenshot_path,
                    name=item.name,
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to save screenshot: {e}")