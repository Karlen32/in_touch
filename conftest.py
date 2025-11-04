import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   # ✅ вот этот импорт важен
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import Urls
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.credentials import Credentials
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from locators import loginLocators





@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login_without_onboarding(driver):
    """Авторизация врача с автоматическим закрытием онбординга"""
    driver.get(Urls.LOGIN_URL)
    driver.find_element(*loginLocators.EMAIL_INPUT).send_keys(Credentials.DOCTOR["email"])
    driver.find_element(*loginLocators.PASSWORD_INPUT).send_keys(Credentials.DOCTOR["password"])
    driver.find_element(*loginLocators.LOGIN_BUTTON).click()

    # Ожидаем появления основной страницы или онбординга
    WebDriverWait(driver, 10).until(
        lambda d: "/assignments" in d.current_url or "onboarding" in d.page_source
    )

    # Отправляем клавишу ESC, если есть онбординг
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Дополнительно ждём, пока появится кнопка выхода
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(loginLocators.BUTTON_LOGOUT)
    )

    return driver



@pytest.fixture()
def login_doctor(driver):
    driver.find_element(*loginLocators.EMAIL_INPUT).send_keys(Credentials.DOCTOR["email"])
    driver.find_element(*loginLocators.PASSWORD_INPUT).send_keys(Credentials.DOCTOR["password"])
    driver.find_element(*loginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_contains("/assignments"))
    
    return driver


@pytest.fixture()
def login_client(driver):
    driver.find_element(*loginLocators.EMAIL_INPUT).send_keys(Credentials.CLIENT["email"])
    driver.find_element(*loginLocators.PASSWORD_INPUT).send_keys(Credentials.CLIENT["password"])
    driver.find_element(*loginLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_contains("/assignments"))
    
    return driver

