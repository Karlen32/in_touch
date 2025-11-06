from selenium.webdriver.common.by import By


class loginLocators:
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div.password-field input[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Login']]")

    # Ошибки
    ERROR_MESSAGE_EMAIL = (By.CSS_SELECTOR, "div.error__text_login > div")
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//div[contains(text(), 'Password must be at least 8 characters long')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error__text_login > div")

    # Рамка
    RED_BORDER = (By.CSS_SELECTOR, ".input.error")

    # выход
    BUTTON_LOGOUT = (By.ID, "logout")


class OnboardingLocators:
    # Step 1 — Welcome
    WELCOME_ICON = (By.CSS_SELECTOR, "img.welcome-icon")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, "div.welcome-message")
    WELCOME_TITLE = (By.XPATH, "//div[text()='Welcome to INtouch!']")
    LETS_START_BUTTON = (By.XPATH, "//button[contains(text(), 'Let’s start!')]")

    # Общие элементы
    WINDOWS_ONBOARDING = (By.CSS_SELECTOR, ".shepherd-content")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button.shepherd-button-icon.shepherd-button")

    # Step 2–10 — каждый шаг по ID
    STEP_2_MESSAGE = (By.ID, "library-description")
    STEP_3_MESSAGE = (By.ID, "favorites-description")
    STEP_4_MESSAGE = (By.ID, "my-tasks-description")
    STEP_5_MESSAGE = (By.ID, "add-assignment-description")
    STEP_6_MESSAGE = (By.ID, "all-assignment-intro-description")
    STEP_7_MESSAGE = (By.ID, "add-favourite-description")
    STEP_8_MESSAGE = (By.ID, "share-assignment-description")
    STEP_9_MESSAGE = (By.ID, "shared-times-description")
    STEP_10_MESSAGE = (By.ID, "assignment-rating-description")



class AddAssignmentLocators:
    ADD_ASSIGNMENT_BUTTON = (By.XPATH, "//p[normalize-space(text())='Add Assignment']")
    TITLE_INPUT = (By.ID, "title")
    DESCRIPTION_INPUT = (By.ID, "text")
    SEARCH_INPUT = (By.XPATH,"//input[contains(@placeholder, 'relevant keyword')]")
    SEARCH_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Search']]")
    TYPE_DROPDOWN = (By.XPATH, "//select[@required]")
    TYPE_PLACEHOLDER_OPTION = (By.XPATH, "//option[contains(text(), 'Type')]") # Если нужно проверить, что поле по умолчанию пустое или подсвечено красным:
    TYPE_OPTION_LESSON = (By.XPATH, "//option[@value='lesson']")
    TYPE_OPTION_EXERCISE = (By.XPATH, "//option[@value='exercise']")
    TYPE_OPTION_STUDY = (By.XPATH, "//option[@value='study']")
    LANGUAGE_DROPDOWN = (By.XPATH, "//select[@required and not(@multiple)]")
    LANGUAGE_PLACEHOLDER = (By.XPATH, "//option[normalize-space(text())='Language']") # Если нужно проверить, что поле по умолчанию пустое или подсвечено красным:
    LANGUAGE_ENGLISH = (By.XPATH, "//option[@value='en']")
    LANGUAGE_ITALIAN = (By.XPATH, "//option[@value='it']")
    OPEN_QUESTION_ICON = (By.XPATH, "//img[@alt='OpenQuestionIcon']")
    QUESTION_EDITOR_INPUT = (By.CSS_SELECTOR,"div.public-DraftEditor-content[contenteditable='true']") # первое поле
    TEXT_PARAGRAPH_ICON = (By.XPATH,"//img[@alt='textParagraphIcon']")
    QUESTION_INPUT = (By.XPATH,"(//div[@contenteditable='true' and contains(@class, 'public-DraftEditor-content')])[1]") # остальные
    SINGLE_CHOICE_ICON = (By.XPATH,"//img[@alt='singleChoiceIcon']")
    MULTIPLE_СHOICE_ICON = (By.XPATH,"//img[@alt='multipleChoiceIcon']")
    LINEAR_SCALE_ICON = (By.XPATH,"//img[@alt='linearScaleIcon']")
    IMAGE_ICON = (By.XPATH,"//img[@alt='imageIcon']")
    OPTION_INPUT = (By.CSS_SELECTOR,"input._choice_block__input_yy2nk_13[placeholder='Add option...']")
    OPTION_INPUT = (By.XPATH,"//input[@placeholder='Add option...']")
    LEFT_POLE_INPUT = (By.XPATH,"//input[@placeholder='Left pole...']")
    RIGHT_POLE_INPUT = (By.XPATH,"//input[@placeholder='Right pole...']")  
    RANGE_MIN_INPUT = (By.ID, "rangeMinValue")
    RANGE_MAX_INPUT = (By.ID, "rangeMaxValue")
    # Кнопки для MIN
    MIN_DECREASE_BUTTON = (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[1]")
    MIN_INCREASE_BUTTON = (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[2]")

    # Кнопки для MAX
    MAX_DECREASE_BUTTON = (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[3]")
    MAX_INCREASE_BUTTON = (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[4]")
    IMAGE_HEADLINE_PLACEHOLDER = (By.XPATH,"//div[contains(@class, 'public-DraftEditorPlaceholder-inner') ""and normalize-space(text())='Image headline']")
    BROWSE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Browse']]")


