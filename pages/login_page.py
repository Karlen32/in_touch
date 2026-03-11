"""Page Object для страницы логина."""

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.config import Urls
from utils.credentials import Credentials


class LoginPage(BasePage):
    """Страница авторизации (логин)."""

    def __init__(self, driver, base_url: str = None):
        super().__init__(driver, base_url or Urls.BASE_URL)

    def open_login(self) -> None:
        """Открыть страницу логина."""
        self.open(Urls.LOGIN_URL)

    def login(self, email: str, password: str) -> None:
        """Ввести email, пароль и нажать Login."""
        self.type_text(LoginLocators.EMAIL_INPUT, email)
        self.type_text(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def login_as_doctor(self) -> None:
        """Авторизоваться под врачом."""
        self.login(Credentials.DOCTOR["email"], Credentials.DOCTOR["password"])

    def login_as_client(self) -> None:
        """Авторизоваться под клиентом."""
        self.login(Credentials.CLIENT["email"], Credentials.CLIENT["password"])

    def expect_success_login(self, timeout: int = 5) -> None:
        """Дождаться успешного входа (URL содержит /assignments)."""
        self.wait_for_url_contains("/assignments", timeout=timeout)

    def get_email_error_text(self, timeout: int = 10) -> str:
        """Получить текст ошибки для поля email."""
        return self.get_text(LoginLocators.ERROR_MESSAGE_EMAIL, timeout=timeout)

    def get_password_error_text(self, timeout: int = 10) -> str:
        """Получить текст ошибки для поля пароля."""
        return self.get_text(LoginLocators.PASSWORD_ERROR_MESSAGE, timeout=timeout)

    def get_generic_error_text(self, timeout: int = 10) -> str:
        """Получить текст общей ошибки (неверный логин/пароль)."""
        return self.get_text(LoginLocators.ERROR_MESSAGE, timeout=timeout)

    def is_email_error_highlighted(self) -> bool:
        """Проверить, что у поля email красная рамка (ошибка валидации)."""
        element = self.find(LoginLocators.EMAIL_INPUT)
        border_color = element.value_of_css_property("border-color")
        return border_color in ("rgb(255, 0, 0)", "#FF0000", "rgb(255, 0, 0)")

    def is_password_error_highlighted(self) -> bool:
        """Проверить, что у поля пароля красная рамка."""
        element = self.find(LoginLocators.PASSWORD_INPUT)
        border_color = element.value_of_css_property("border-color")
        return border_color in ("rgb(255, 0, 0)", "#FF0000", "rgb(255, 0, 0)")

    def logout(self) -> None:
        """Выйти из системы (клик по кнопке Logout)."""
        self.click(LoginLocators.BUTTON_LOGOUT)

    def expect_login_form_visible(self, timeout: int = 5) -> None:
        """Дождаться появления формы логина (поле email видимо)."""
        self.wait_for_visible(LoginLocators.EMAIL_INPUT, timeout=timeout)

    def is_login_form_displayed(self) -> bool:
        """Проверить, что форма логина отображается (поле email видимо)."""
        return self.find(LoginLocators.EMAIL_INPUT).is_displayed()
