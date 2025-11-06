from selenium.webdriver.common.by import By



class AddAssignmentLocators:
    """Форма создания задания"""

    # Основные поля
    ADD_ASSIGNMENT_BUTTON = (By.XPATH, "//p[normalize-space(text())='Add Assignment']")
    TITLE_INPUT = (By.ID, "title")
    DESCRIPTION_INPUT = (By.ID, "text")

    # Поиск
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'relevant keyword')]")
    SEARCH_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Search']]")
    SEARCH_RESULT_IMAGE = ("css selector", "img[src*='unsplash.com']")

    # Dropdown’ы
    TYPE_DROPDOWN = (By.XPATH, "//select[@required]")
    LANGUAGE_DROPDOWN = (By.XPATH, "//select[@required and not(@multiple)]")
    LANGUAGE_OPTION_ENGLISH = (By.XPATH, "//option[@value='en']")
    LANGUAGE_OPTION_FRENCH = (By.XPATH, "//option[@value='fr']")

    # Опции типа
    TYPE_OPTIONS = {
        "lesson": (By.XPATH, "//option[@value='lesson']"),
        "exercise": (By.XPATH, "//option[@value='exercise']"),
        "study": (By.XPATH, "//option[@value='study']"),
    }

    # Иконки типов вопросов
    QUESTION_TYPE_ICONS = {
        "open": (By.XPATH, "//img[@alt='OpenQuestionIcon']"),
        "text": (By.XPATH, "//img[@alt='textParagraphIcon']"),
        "single_choice": (By.XPATH, "//img[@alt='singleChoiceIcon']"),
        "multiple_choice": (By.XPATH, "//img[@alt='multipleChoiceIcon']"),
        "range": (By.XPATH, "//img[@alt='linearScaleIcon']"),
        "image": (By.XPATH, "//img[@alt='imageIcon']"),
    }

    # Поля для контента
    QUESTION_INPUT = (
    "xpath",
    "(//div[contains(@class,'DraftEditor-root')]//div[@contenteditable='true'])[1]"
    )

    TEXT_INPUT = ("xpath",
        "(//div[contains(@class,'DraftEditor-root')]//div[@contenteditable='true'])[2]"
    )

    SINGLE_INPUT = ("xpath",
        "(//div[contains(@class,'DraftEditor-root')]//div[@contenteditable='true'])[3]"
    )

    MULTIPLE_INPUT = ("xpath",
        "(//div[contains(@class,'DraftEditor-root')]//div[@contenteditable='true'])[4]"
    )

    LINEAR_INPUT = ("xpath",
        "(//div[contains(@class,'DraftEditor-root')]//div[@contenteditable='true'])[5]"
    )

    IMAGE_INPUT = ("xpath",
        "(//div[contains(@class,'DraftEditor-root')]//div[@contenteditable='true'])[6]"
    )
    



    # Опций для полей Single-choice и Multiple-choice
    OPTION_SINGLE_INPUT = (By.XPATH, "(//input[@placeholder='Add option...'])[1]")
    OPTION_MULTIPLE_INPUT = (By.XPATH, "(//input[@placeholder='Add option...'])[2]")


    # Поля для шкалы Linear Scale
    LEFT_POLE_INPUT = (By.XPATH, "//input[@placeholder='Left pole...']")
    RIGHT_POLE_INPUT = (By.XPATH, "//input[@placeholder='Right pole...']")
    RANGE_MIN_INPUT = (By.ID, "rangeMinValue")
    RANGE_MAX_INPUT = (By.ID, "rangeMaxValue")

    # Кнопки управления шкалой
    RANGE_BUTTONS = {
        "min_down": (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[1]"),
        "min_up": (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[2]"),
        "max_down": (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[3]"),
        "max_up": (By.XPATH, "(//button[contains(@class, '_range_block__button_lrfby_24')])[4]"),
    }

    # Изображения
    BROWSE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Browse']]")
    UPLOADING_IMAGE = (By.XPATH, "//input[@type='file']")


    # Кнопки сохранения 
    COMPLETE_AND_PUBLISH_BUTTON = (By.XPATH,"//button[.//p[normalize-space(text())='Complete & Publish']]")
    SAVE_AS_DRAFT_BUTTON = (By.XPATH, "//button[normalize-space(.)='Save as Draft']")
    SAVE_ICON_DISABLED = (By.XPATH,"//img[@alt='save' and contains(@class, 'header__icon-save-disabled')]")
    SAVE_ICON_ACTIVE = (By.XPATH,"//img[@alt='save' and not(contains(@class, 'header__icon-save-disabled'))]")
    SUCCESS_TOAST = ("xpath", "//p[text()='Asad Vasad']")


    # Предпросмотр 
    CHANGE_VIEW_ICON_DISABLED = (By.XPATH,"//img[@alt='changeView' and contains(@class, 'header__icon-eye-disabled')]")
    CHANGE_VIEW_ICON_ACTIVE = (By.XPATH,"//img[@alt='changeView' and not(contains(@class, 'header__icon-eye-disabled'))]")
    
    # Нужно изменить путь к фотографии — сейчас указан путь на локальной машине автора
    MY_IMAGE =  r"C:\Image_In_touch\asd.JPG"
    MY_IMAGE_EDIT =  r"C:\Image_In_touch\dsa.JPG"