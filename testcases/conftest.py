from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import pytest_html

# @pytest.fixture(scope="function")
# def setup():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get("https://www.yatra.com/")
#     driver.maximize_window()
#     time.sleep(10)
#     driver.find_element(By.CSS_SELECTOR, "span[class='style_cross__q1ZoV'] img[alt='cross']").click()
#     yield driver
#     driver.quit()

@pytest.fixture(autouse=True)

def setup(request,browser,url):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    #wait = WebDriverWait(driver, 10) 
    #driver.get("https://www.yatra.com/")
    driver.get(url)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "span[class='style_cross__q1ZoV'] img[alt='cross']").click()
    request.cls.driver = driver
    #request.cls.wait = wait
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def url(request):
    return request.config.getoption("--url")



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://yatra.com"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras

def pytest_html_report_title(report):
    report.title = "Yatra Flight Booking Platfrom"

    
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or edge")

# @pytest.fixture(scope="class")
# def setup(request):
#     browser = request.config.getoption("--browser")

#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")

#     driver.get("https://www.yatra.com/")
#     driver.maximize_window()
#     time.sleep(10)
#     driver.find_element(By.CSS_SELECTOR, "span[class='style_cross__q1ZoV'] img[alt='cross']").click()

#     request.cls.driver = driver
#     yield 
#     driver.close()
    