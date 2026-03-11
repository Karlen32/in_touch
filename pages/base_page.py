"""Базовый класс Page Object для всех страниц приложения."""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

DEFAULT_TIMEOUT = 10


class BasePage:
    """Базовый класс страницы. Инкапсулирует общие операции с WebDriver."""

    def __init__(self, driver: WebDriver, base_url: str = ""):
        self.driver = driver
        self.base_url = base_url

    def open(self, url: str = None) -> None:
        """Открыть страницу по URL. Если url не передан — используется base_url."""
        target = url or self.base_url
        if target:
            self.driver.get(target)

    def find(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """Найти элемент с ожиданием видимости."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_present(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """Найти элемент с ожиданием присутствия в DOM."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """Найти элемент и дождаться, пока он станет кликабельным."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Клик по элементу с ожиданием кликабельности."""
        element = self.find_clickable(locator, timeout)
        element.click()

    def type_text(self, locator: tuple, text: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Ввести текст в поле с ожиданием видимости элемента."""
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> str:
        """Получить текст элемента с ожиданием видимости."""
        return self.find(locator, timeout).text

    def wait_for_visible(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """Дождаться видимости элемента."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisible(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Дождаться исчезновения элемента из DOM или невидимости."""
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_not_present(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Дождаться отсутствия элемента в DOM."""
        return WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_element_located(locator)
        )

    def scroll_into_view(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> WebElement:
        """Прокрутить к элементу и вернуть его."""
        element = self.find(locator, timeout)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        return element

    def click_via_script(self, locator: tuple, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Клик по элементу через JavaScript (для элементов, перекрытых другими)."""
        element = self.find_clickable(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self) -> str:
        """Текущий URL страницы."""
        return self.driver.current_url

    def wait_for_url_contains(self, substring: str, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Дождаться, пока в URL появится подстрока."""
        return WebDriverWait(self.driver, timeout).until(
            lambda d: substring in d.current_url
        )
