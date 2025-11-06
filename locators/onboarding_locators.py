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


class AddAssignmentOnboardingLocators:
    ADD_ASSIGNMENT_BUTTON = (By.XPATH, "//p[normalize-space(text())='Add Assignment']")
    STEP_1_MESSAGE_ADDASSIG = (By.ID, "constructorFillIn-description")
    STEP_2_MESSAGE_ADDASSIG = (By.ID, "constructorQuestionTypes-description")
    STEP_3_MESSAGE_ADDASSIG = (By.ID, "constructorPreview-description")
    STEP_4_MESSAGE_ADDASSIG = (By.ID, "constructorDraft-description")
    STEP_5_MESSAGE_ADDASSIG = (By.ID, "constructorPublish-description")



class ClientOnboardingLocators:
    CLIENTS_MENU_BUTTON = (By.XPATH, "//a[normalize-space(text())='Clients']")
    STEP_1_MESSAGE_CLIENTS = (By.ID, "clientsName-description")
    STEP_2_MESSAGE_CLIENTS = (By.ID, "clientsStatus-description")
    CLIENT_LINK = (By.CSS_SELECTOR, "a.link-to-client[href^='/clients/']")
    STEP_1_CLIENT_PROFILE = (By.ID, "clientProfile-description")
    STEP_2_CLIENT_PROFILE = (By.ID, "clientAssignments-description")
    STEP_3_CLIENT_PROFILE = (By.ID, "clientDiary-description")
    