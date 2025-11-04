from selenium.webdriver.common.by import By


class AddAssignmentOnboardingLocators:
    """Онбординг страницы Add Assignment"""

    ADD_ASSIGNMENT_BUTTON = (By.XPATH, "//p[normalize-space(text())='Add Assignment']")
    STEP_MESSAGES = {
        1: (By.ID, "constructorFillIn-description"),
        2: (By.ID, "constructorQuestionTypes-description"),
        3: (By.ID, "constructorPreview-description"),
        4: (By.ID, "constructorDraft-description"),
        5: (By.ID, "constructorPublish-description"),
    }


class AddAssignmentLocators:
    """Форма создания задания"""

    # Основные поля
    ADD_ASSIGNMENT_BUTTON = (By.XPATH, "//p[normalize-space(text())='Add Assignment']")
    TITLE_INPUT = (By.ID, "title")
    DESCRIPTION_INPUT = (By.ID, "text")

    # Поиск
    SEARCH_INPUT = (By.XPATH, "//input[contains(@placeholder, 'relevant keyword')]")
    SEARCH_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Search']]")

    # Dropdown’ы
    TYPE_DROPDOWN = (By.XPATH, "//select[@required]")
    LANGUAGE_DROPDOWN = (By.XPATH, "//select[@required and not(@multiple)]")

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
    QUESTION_INPUT = (By.CSS_SELECTOR, "div.public-DraftEditor-content[contenteditable='true']")
    OPTION_INPUT = (By.XPATH, "//input[@placeholder='Add option...']")
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
    IMAGE_HEADLINE = (By.XPATH, "//div[contains(@class, 'public-DraftEditorPlaceholder-inner') and normalize-space(text())='Image headline']")
    BROWSE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Browse']]")

    # Кнопки сохранения 
    COMPLETE_AND_PUBLISH_BUTTON = (By.XPATH,"//button[.//p[normalize-space(text())='Complete & Publish']]")
    SAVE_AS_DRAFT_BUTTON = (By.XPATH,"//button[.//p[normalize-space(text())='Save as Draft']]")
    SAVE_ICON_DISABLED = (By.XPATH,"//img[@alt='save' and contains(@class, 'header__icon-save-disabled')]")
    SAVE_ICON_ACTIVE = (By.XPATH,"//img[@alt='save' and not(contains(@class, 'header__icon-save-disabled'))]")


    # Предпросмотр 
    CHANGE_VIEW_ICON_DISABLED = (By.XPATH,"//img[@alt='changeView' and contains(@class, 'header__icon-eye-disabled')]")
    CHANGE_VIEW_ICON_ACTIVE = (By.XPATH,"//img[@alt='changeView' and not(contains(@class, 'header__icon-eye-disabled'))]")
    
