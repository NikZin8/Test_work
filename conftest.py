import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loguru import logger

logger.add("debug.log", format="{time}, {level}, {message}", level="DEBUG", rotation="2 min")


@pytest.fixture(scope="session")
@logger.catch()
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)
    return browser
