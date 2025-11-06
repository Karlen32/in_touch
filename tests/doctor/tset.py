from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.add_assignment_locators import AddAssignmentLocators
from locators.edit_delete_assignment_locators import EditDeleteAssignmentLocators
from data.texts_add_assignment import AddAssignmentTexts
from utils.config import Doctor


class TestEditHomework:
    def test_edit_homework(self, driver_with_storage):
        driver = driver_with_storage

        # 1. НАВИГАЦИЯ

        # Переходим в раздел "My Tasks"
        driver.find_element(*EditDeleteAssignmentLocators.MY_TASKS_BUTTON).click()

        # 2. ВЫБОР ЗАДАНИЯ ДЛЯ РЕДАКТИРОВАНИЯ

        # Ждём появления кнопок редактирования
        edit_buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(EditDeleteAssignmentLocators.EDIT_BUTTON)
        )
        assert edit_buttons

        # Дожидаемся кликабельности первой кнопки и нажимаем "Edit"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(edit_buttons[0]))
        edit_buttons[0].click()

        # РЕДАКТИРОВАНИЕ ОСНОВНЫХ ПОЛЕЙ

        # Изменяем заголовок
        driver.find_element(*AddAssignmentLocators.TITLE_INPUT).send_keys(AddAssignmentTexts.EDIT_TITLE)

        # Изменяем описание
        driver.find_element(*AddAssignmentLocators.DESCRIPTION_INPUT).send_keys(AddAssignmentTexts.EDIT_DESCRIPTION)

        # ЗАМЕНА ИЗОБРАЖЕНИЯ

        # Вводим ключевое слово для поиска
        driver.find_element(*AddAssignmentLocators.SEARCH_INPUT).send_keys(AddAssignmentTexts.EDIT_SEARCH_KEYWORD)

        # Нажимаем кнопку поиска
        driver.find_element(*AddAssignmentLocators.SEARCH_BUTTON).click()

        # Ожидаем появления и выбираем новое изображение
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AddAssignmentLocators.SEARCH_RESULT_IMAGE)
        ).click()

        # ВЫБОР ТИПА И ЯЗЫКА

        # Выбираем тип задания "Exercise"
        driver.find_element(*AddAssignmentLocators.TYPE_DROPDOWN).click()
        driver.find_element(*AddAssignmentLocators.TYPE_OPTIONS["exercise"]).click()

        # Выбираем язык — "French"
        driver.find_element(*AddAssignmentLocators.LANGUAGE_DROPDOWN).click()
        driver.find_element(*AddAssignmentLocators.LANGUAGE_OPTION_FRENCH).click()

        # ЗАПОЛНЕНИЕ ВОПРОСОВ (РАЗНЫЕ ТИПЫ)

        # Открытый вопрос
        driver.find_element(*AddAssignmentLocators.QUESTION_INPUT).send_keys(AddAssignmentTexts.EDIT_OPEN_QUESTION)

        # Текстовый вопрос (параграф)
        driver.find_element(*AddAssignmentLocators.TEXT_INPUT).send_keys(AddAssignmentTexts.EDIT_PARAGRAPH_QUESTION)

        # Вопрос с одиночным выбором
        driver.find_element(*AddAssignmentLocators.SINGLE_INPUT).send_keys(AddAssignmentTexts.EDIT_SINGLE_QUESTION)
        driver.find_element(*AddAssignmentLocators.OPTION_SINGLE_INPUT).send_keys(AddAssignmentTexts.SINGLE_CHOICE_OPTIONS[3])

        # Вопрос с множественным выбором
        driver.find_element(*AddAssignmentLocators.MULTIPLE_INPUT).send_keys(AddAssignmentTexts.EDIT_MULTIPLE_QUESTION)
        driver.find_element(*AddAssignmentLocators.OPTION_MULTIPLE_INPUT).send_keys(AddAssignmentTexts.MULTIPLE_CHOICE_OPTIONS[3])

        # Шкала (линейный диапазон)
        driver.find_element(*AddAssignmentLocators.LINEAR_INPUT).send_keys(AddAssignmentTexts.EDIT_RANGE_QUESTION)
        driver.find_element(*AddAssignmentLocators.LEFT_POLE_INPUT).send_keys(AddAssignmentTexts.LEFT_POLE)
        driver.find_element(*AddAssignmentLocators.RIGHT_POLE_INPUT).send_keys(AddAssignmentTexts.RIGHT_POLE)
        driver.find_element(*AddAssignmentLocators.RANGE_MIN_INPUT).send_keys(AddAssignmentTexts.RANGE_MIN)
        driver.find_element(*AddAssignmentLocators.RANGE_MAX_INPUT).send_keys(AddAssignmentTexts.RANGE_MAX)

        # Вопрос с изображением
        driver.find_element(*AddAssignmentLocators.IMAGE_INPUT).send_keys(AddAssignmentTexts.EDIT_IMAGE_QUESTION)

        # ДОБАВЛЕНИЕ ИЗОБРАЖЕНИЯ

        # Загружаем новое изображение
        file_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(AddAssignmentLocators.UPLOADING_IMAGE)
        )
        file_input.send_keys(AddAssignmentLocators.MY_IMAGE_EDIT)

        # ПРОСМОТР И ВОЗВРАТ К СПИСКУ

        # Меняем вид отображения (иконка "глаз")
        driver.find_element(*EditDeleteAssignmentLocators.CHANGE_VIEW_ICON).click()

        # Нажимаем кнопку "Назад"
        back_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(EditDeleteAssignmentLocators.BACK_EDIT_BUTTON)
        )
        back_button.click()

        # СОХРАНЕНИЕ И ПРОВЕРКА ПЕРЕХОДА

        # Сохраняем задание как черновик
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(AddAssignmentLocators.SAVE_AS_DRAFT_BUTTON)
        ).click()

        # Проверяем успешный переход на HEAD_URL
        WebDriverWait(driver, 25).until(lambda d: Doctor.HEAD_URL in d.current_url)
        assert Doctor.HEAD_URL in driver.current_url, f"Переход не выполнен. Текущий URL: {driver.current_url}"
        print(f"✅ Успешный переход на {driver.current_url}")

