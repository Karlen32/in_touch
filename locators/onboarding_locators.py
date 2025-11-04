from selenium.webdriver.common.by import By


class OnboardingLocators:
    """Главный онбординг (Doctor Dashboard)"""

    # Step 1 — Welcome
    WELCOME_ICON = (By.CSS_SELECTOR, "img.welcome-icon")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, "div.welcome-message")
    WELCOME_TITLE = (By.XPATH, "//div[text()='Welcome to INtouch!']")
    LETS_START_BUTTON = (By.XPATH, "//button[contains(text(), 'Let’s start!')]")

    # Общие элементы
    WINDOWS_ONBOARDING = (By.CSS_SELECTOR, ".shepherd-content")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.shepherd-button-icon.shepherd-button")

    # Step 2–10
    STEP_MESSAGES = {
        2: (By.ID, "library-description"),
        3: (By.ID, "favorites-description"),
        4: (By.ID, "my-tasks-description"),
        5: (By.ID, "add-assignment-description"),
        6: (By.ID, "all-assignment-intro-description"),
        7: (By.ID, "add-favourite-description"),
        8: (By.ID, "share-assignment-description"),
        9: (By.ID, "shared-times-description"),
        10: (By.ID, "assignment-rating-description"),
    }