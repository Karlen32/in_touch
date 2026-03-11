import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config import Urls
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from utils.credentials import Credentials
from locators.login_locators import LoginLocators
from urllib.parse import urlparse
from pages.login_page import LoginPage
from pages.doctor.clients_page import DoctorClientsPage
from pages.doctor.add_assignment_page import AddAssignmentPage
from pages.doctor.share_assignment_page import ShareAssignmentPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    """Page Object страницы логина."""
    return LoginPage(driver)


@pytest.fixture
def doctor_clients_page(driver_with_storage):
    """Page Object страницы клиентов врача (требует авторизованный driver)."""
    return DoctorClientsPage(driver_with_storage)


@pytest.fixture
def add_assignment_page(driver_with_storage):
    """Page Object формы создания/редактирования задания и списка заданий."""
    return AddAssignmentPage(driver_with_storage)


@pytest.fixture
def share_assignment_page(driver_with_storage):
    """Page Object сценариев шаринга заданий клиенту."""
    return ShareAssignmentPage(driver_with_storage)


def get_origin(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}"

@pytest.fixture(scope="function")
def driver_with_storage(driver):
    
    driver.get(Urls.BASE_URL)
    try:
        with open("localstorage.json", "r", encoding="utf-8") as f:
            localstorage_data = json.load(f)
    except FileNotFoundError:
        pytest.skip("localstorage.json не найден — сначала запусти save_localstorage.py и создай файл")

    print(">>> localstorage.json keys:", list(localstorage_data.keys()))

    driver.execute_script("window.localStorage.clear();")

    for key, value in localstorage_data.items():

        if isinstance(value, (dict, list)):
            js_value = json.dumps(value, ensure_ascii=False)
            driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, js_value)
        else:
            driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    current_ls = driver.execute_script("return JSON.stringify(window.localStorage);")
    print(">>> current localStorage after restore:", current_ls)

    driver.get("https://test24.intouch.care/assignments")

    return driver




@pytest.fixture
def login_without_onboarding(driver):
    """Авторизация врача с автоматическим закрытием онбординга."""
    page = LoginPage(driver)
    page.open_login()
    page.login_as_doctor()

    # Ожидаем появления основной страницы или онбординга
    WebDriverWait(driver, 10).until(
        lambda d: "/assignments" in d.current_url or "onboarding" in d.page_source
    )

    # Отправляем клавишу ESC, если есть онбординг
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    # Дополнительно ждём, пока появится кнопка выхода
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginLocators.BUTTON_LOGOUT)
    )

    return driver



@pytest.fixture()
def login_doctor(driver):
    page = LoginPage(driver)
    page.open_login()
    page.login_as_doctor()
    page.expect_success_login(timeout=5)
    return driver


@pytest.fixture()
def login_client(driver):
    page = LoginPage(driver)
    page.open_login()
    page.login_as_client()
    page.expect_success_login(timeout=5)
    return driver

