from selenium.webdriver.common.by import By


class LoginLocators:
    # Поля ввода
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div.password-field input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Login']]")

    # Ошибки
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error__text_login > div")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'Password must be at least 8 characters long')]")
    ERROR_MESSAGE_EMAIL = (By.CSS_SELECTOR, "div.error__text_login > div")
    # Валидация
    RED_BORDER = (By.CSS_SELECTOR, ".input.error")

    # Выход
    BUTTON_LOGOUT = (By.ID, "logout")
