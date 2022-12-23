from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='es',
                     help="Choose language (ru, en-gb, es, fr)")


@pytest.fixture(scope='function')
def browser(request):
    language = str(request.config.getoption("language"))
    browser = webdriver.Chrome()
    browser.get(
        f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    yield browser
    browser.quit()
