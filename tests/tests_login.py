from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from utils.credentials import Credentials
from data.texts_error import EmailErrorText



class TestAuthorizationDoctor:
    # Тесты на авторизацию и валидацию полей формы логина

    def test_login_valid(self, driver):
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Credentials.DOCTOR["email"])
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Credentials.DOCTOR["password"])
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/assignments"))
        assert "/assignments" in driver.current_url, "Авторизация врача не удалась"

    def test_login_invalid_email(self, driver):
        # Проверка ошибки и красной рамки при некорректном email
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Credentials.INVALID_EMAIL["email"])
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Credentials.DOCTOR["password"])
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE_EMAIL)
        )

        error_text = driver.find_element(*LoginLocators.ERROR_MESSAGE_EMAIL).text
        assert error_text == EmailErrorText.EMAIL_ERROR, f"Текст ошибки неверный: {error_text}"

    
        email_field = driver.find_element(*LoginLocators.EMAIL_INPUT)
        border_color = email_field.value_of_css_property("border-color")
        assert border_color in (
            EmailErrorText.ERROR_FIELD_COLOR_RGBA,
            EmailErrorText.ERROR_FIELD_COLOR_HEX
        ), f"Цвет рамки email не красный: {border_color}"

    def test_login_short_password(self, driver):
        # Проверка ошибки при коротком пароле (<8 символов)

        # Вводим email и короткий пароль
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Credentials.DOCTOR["email"])
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Credentials.INVALID_PASSWORD["password"])

        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        # Ждём появления ошибки
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.PASSWORD_ERROR_MESSAGE)
        )

        # Проверяем текст ошибки
        error_text = driver.find_element(*LoginLocators.PASSWORD_ERROR_MESSAGE).text
        assert error_text == EmailErrorText.PASSWORD_ERROR, f"Неверный текст ошибки: {error_text}"

        # Проверяем цвет рамки у поля пароля
        password_field = driver.find_element(*LoginLocators.PASSWORD_INPUT)
        border_color = password_field.value_of_css_property("border-color")

        assert border_color in (
            EmailErrorText.ERROR_FIELD_COLOR_RGBA,
            EmailErrorText.ERROR_FIELD_COLOR_HEX
        ), f"Цвет рамки password не красный: {border_color}"


    def test_login_invalid_credentials(self, driver):
        # Проверка ошибки при неверных логине или пароле
        driver.find_element(*LoginLocators.EMAIL_INPUT).send_keys(Credentials.INVALID_CREDENTIALS["email"])
        driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(Credentials.INVALID_CREDENTIALS["password"])
        driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginLocators.ERROR_MESSAGE)
        )

        error_text = driver.find_element(*LoginLocators.ERROR_MESSAGE).text
        assert error_text == EmailErrorText.PASSWORD_OR_LOGIN_ERROR, (
            f"Текст ошибки неверный: {error_text}"
        )

    
    def test_logout(self, login_without_onboarding):
        # Проверка выхода из системы
        login_without_onboarding.find_element(*LoginLocators.BUTTON_LOGOUT).click()
        

        WebDriverWait(login_without_onboarding, 5).until(
            EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)
        )
        email_input = login_without_onboarding.find_element(*LoginLocators.EMAIL_INPUT)
        assert email_input.is_displayed(), "Поле Email не отображается после выхода"

        



        


        