"""Тесты авторизации и валидации формы логина (Page Object)."""

from data.texts_error import EmailErrorText
from pages.login_page import LoginPage
from utils.credentials import Credentials


class TestAuthorizationDoctor:
    """Тесты на авторизацию и валидацию полей формы логина."""

    def test_login_valid(self, login_page: LoginPage) -> None:
        """Успешный вход под врачом."""
        login_page.open_login()
        login_page.login_as_doctor()
        login_page.expect_success_login()
        assert "/assignments" in login_page.get_current_url(), "Авторизация врача не удалась"

    def test_login_invalid_email(self, login_page: LoginPage) -> None:
        """Проверка ошибки и красной рамки при некорректном email."""
        login_page.open_login()
        login_page.login(
            Credentials.INVALID_EMAIL["email"],
            Credentials.INVALID_EMAIL["password"],
        )
        error_text = login_page.get_email_error_text()
        assert error_text == EmailErrorText.EMAIL_ERROR, f"Текст ошибки неверный: {error_text}"

        assert login_page.is_email_error_highlighted(), "Цвет рамки email не красный"

    def test_login_short_password(self, login_page: LoginPage) -> None:
        """Проверка ошибки при коротком пароле (<8 символов)."""
        login_page.open_login()
        login_page.login(
            Credentials.DOCTOR["email"],
            Credentials.INVALID_PASSWORD["password"],
        )
        error_text = login_page.get_password_error_text()
        assert error_text == EmailErrorText.PASSWORD_ERROR, f"Неверный текст ошибки: {error_text}"

        assert login_page.is_password_error_highlighted(), "Цвет рамки password не красный"

    def test_login_invalid_credentials(self, login_page: LoginPage) -> None:
        """Проверка ошибки при неверных логине или пароле."""
        login_page.open_login()
        login_page.login(
            Credentials.INVALID_CREDENTIALS["email"],
            Credentials.INVALID_CREDENTIALS["password"],
        )
        error_text = login_page.get_generic_error_text()
        assert error_text == EmailErrorText.PASSWORD_OR_LOGIN_ERROR, (
            f"Текст ошибки неверный: {error_text}"
        )

    def test_logout(self, login_without_onboarding) -> None:
        """Проверка выхода из системы."""
        page = LoginPage(login_without_onboarding)
        page.logout()
        page.expect_login_form_visible(timeout=5)
        assert page.is_login_form_displayed(), "Поле Email не отображается после выхода"