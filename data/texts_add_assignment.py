class AddAssignmentTexts:
    """Тестовые данные для формы Add Assignment"""

    # Заголовки и описания
    TITLE = "Daily English Practice — Lesson 1"
    DESCRIPTION = "This lesson helps students practice basic English conversation and vocabulary."

    # Поиск
    SEARCH_KEYWORD = "grammar"

    # Тип задания
    TYPE = "lesson"
    LANGUAGE = "English"

    # Вопросы (по типам)
    OPEN_QUESTION = "Describe your favorite book in English."
    PARAGRAPH_QUESTION = "Write a short paragraph about your weekend."
    SINGLE_CHOICE_QUESTION = "Choose the correct synonym for 'happy'."
    MULTIPLE_CHOICE_QUESTION = "Select all adjectives that describe a person."
    RANGE_QUESTION = "How confident do you feel about your speaking skills?"
    IMAGE_QUESTION = "What do you see in the picture?"

     # --- Single Choice Question ---
    SINGLE_CHOICE_QUESTION = "Choose the correct synonym for 'happy'."
    SINGLE_CHOICE_OPTIONS = [
        "Joyful",
        "Sad",
        "Excited",
        "Angry"
    ]

    # --- Multiple Choice Question ---
    MULTIPLE_CHOICE_QUESTION = "Select all adjectives that describe positive emotions."
    MULTIPLE_CHOICE_OPTIONS = [
        "Kind",
        "Optimistic",
        "Lazy",
        "Honest"
    ]

    # Шкала
    LEFT_POLE = "Not confident"
    RIGHT_POLE = "Very confident"
    RANGE_MIN = 1
    RANGE_MAX = 10

    # Изображение
    IMAGE_HEADLINE = "Describe what this image represents"

