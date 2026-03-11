"""Page Object для формы создания/редактирования задания и списка заданий врача."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.add_assignment_locators import AddAssignmentLocators
from locators.edit_delete_assignment_locators import EditDeleteAssignmentLocators
from utils.config import Doctor


class AddAssignmentPage(BasePage):
    """Форма добавления/редактирования задания и действия со списком (My Tasks)."""

    def __init__(self, driver, base_url: str = None):
        super().__init__(driver, base_url or Doctor.BASE)

    def open_add_assignment_form(self) -> None:
        """Открыть форму создания задания (кнопка Add Assignment)."""
        self.click(AddAssignmentLocators.ADD_ASSIGNMENT_BUTTON)

    def fill_title_and_description(self, title: str, description: str) -> None:
        """Заполнить заголовок и описание задания."""
        self.type_text(AddAssignmentLocators.TITLE_INPUT, title)
        self.type_text(AddAssignmentLocators.DESCRIPTION_INPUT, description)

    def search_and_select_image(self, keyword: str) -> None:
        """Ввести ключевое слово поиска и выбрать первое изображение из результатов."""
        self.type_text(AddAssignmentLocators.SEARCH_INPUT, keyword)
        self.click(AddAssignmentLocators.SEARCH_BUTTON)
        self.wait_for_visible(AddAssignmentLocators.SEARCH_RESULT_IMAGE, timeout=5)
        self.click(AddAssignmentLocators.SEARCH_RESULT_IMAGE)

    def select_type(self, type_value: str) -> None:
        """Выбрать тип задания (lesson, exercise, study)."""
        self.click(AddAssignmentLocators.TYPE_DROPDOWN)
        self.click(AddAssignmentLocators.TYPE_OPTIONS[type_value])

    def select_language_english(self) -> None:
        """Выбрать язык English."""
        self.click(AddAssignmentLocators.LANGUAGE_DROPDOWN)
        self.click(AddAssignmentLocators.LANGUAGE_OPTION_ENGLISH)

    def select_language_french(self) -> None:
        """Выбрать язык French."""
        self.click(AddAssignmentLocators.LANGUAGE_DROPDOWN)
        self.click(AddAssignmentLocators.LANGUAGE_OPTION_FRENCH)

    def add_open_question(self, text: str) -> None:
        """Добавить открытый вопрос."""
        self.click(AddAssignmentLocators.QUESTION_TYPE_ICONS["open"])
        self.type_text(AddAssignmentLocators.QUESTION_INPUT, text)

    def add_text_question(self, text: str) -> None:
        """Добавить текстовый вопрос (параграф)."""
        self.click(AddAssignmentLocators.QUESTION_TYPE_ICONS["text"])
        self.type_text(AddAssignmentLocators.TEXT_INPUT, text)

    def add_single_choice_question(self, question_text: str, options: list) -> None:
        """Добавить вопрос с одиночным выбором (опции дописываются в поле)."""
        self.click(AddAssignmentLocators.QUESTION_TYPE_ICONS["single_choice"])
        self.type_text(AddAssignmentLocators.SINGLE_INPUT, question_text)
        option_elem = self.find(AddAssignmentLocators.OPTION_SINGLE_INPUT)
        for opt in options:
            option_elem.send_keys(opt)

    def add_multiple_choice_question(self, question_text: str, options: list) -> None:
        """Добавить вопрос с множественным выбором (опции дописываются в поле)."""
        self.click(AddAssignmentLocators.QUESTION_TYPE_ICONS["multiple_choice"])
        self.type_text(AddAssignmentLocators.MULTIPLE_INPUT, question_text)
        option_elem = self.find(AddAssignmentLocators.OPTION_MULTIPLE_INPUT)
        for opt in options:
            option_elem.send_keys(opt)

    def add_range_question(
        self,
        question_text: str,
        left_pole: str,
        right_pole: str,
        min_val,
        max_val,
    ) -> None:
        """Добавить вопрос со шкалой (range)."""
        self.click(AddAssignmentLocators.QUESTION_TYPE_ICONS["range"])
        self.type_text(AddAssignmentLocators.LINEAR_INPUT, question_text)
        self.type_text(AddAssignmentLocators.LEFT_POLE_INPUT, left_pole)
        self.type_text(AddAssignmentLocators.RIGHT_POLE_INPUT, right_pole)
        self.type_text(AddAssignmentLocators.RANGE_MIN_INPUT, str(min_val))
        self.type_text(AddAssignmentLocators.RANGE_MAX_INPUT, str(max_val))

    def add_image_question(self, question_text: str, image_path: str) -> None:
        """Добавить вопрос с изображением и загрузить файл."""
        self.click(AddAssignmentLocators.QUESTION_TYPE_ICONS["image"])
        self.type_text(AddAssignmentLocators.IMAGE_INPUT, question_text)
        file_input = self.find_present(AddAssignmentLocators.UPLOADING_IMAGE, timeout=3)
        file_input.send_keys(image_path)

    def append_open_question(self, text: str) -> None:
        """Дописать текст к полю открытого вопроса (редактирование)."""
        self.find(AddAssignmentLocators.QUESTION_INPUT).send_keys(text)

    def append_text_question(self, text: str) -> None:
        """Дописать текст к полю текстового вопроса."""
        self.find(AddAssignmentLocators.TEXT_INPUT).send_keys(text)

    def append_single_question(self, text: str, option_append: str = None) -> None:
        """Дописать к полю single choice и опционально к полю опции."""
        self.find(AddAssignmentLocators.SINGLE_INPUT).send_keys(text)
        if option_append:
            self.find(AddAssignmentLocators.OPTION_SINGLE_INPUT).send_keys(option_append)

    def append_multiple_question(self, text: str, option_append: str = None) -> None:
        """Дописать к полю multiple choice и опционально к полю опции."""
        self.find(AddAssignmentLocators.MULTIPLE_INPUT).send_keys(text)
        if option_append:
            self.find(AddAssignmentLocators.OPTION_MULTIPLE_INPUT).send_keys(option_append)

    def append_range_question(self, text: str, left_pole: str, right_pole: str, min_val, max_val) -> None:
        """Дописать к полю range и полям шкалы."""
        self.find(AddAssignmentLocators.LINEAR_INPUT).send_keys(text)
        self.find(AddAssignmentLocators.LEFT_POLE_INPUT).send_keys(left_pole)
        self.find(AddAssignmentLocators.RIGHT_POLE_INPUT).send_keys(right_pole)
        self.find(AddAssignmentLocators.RANGE_MIN_INPUT).send_keys(str(min_val))
        self.find(AddAssignmentLocators.RANGE_MAX_INPUT).send_keys(str(max_val))

    def append_image_question_and_upload(self, text: str, image_path: str) -> None:
        """Дописать к полю image question и загрузить файл."""
        self.find(AddAssignmentLocators.IMAGE_INPUT).send_keys(text)
        self.find_present(AddAssignmentLocators.UPLOADING_IMAGE, timeout=5).send_keys(image_path)

    def wait_save_icon_active(self, timeout: int = 3) -> None:
        """Дождаться активации иконки сохранения."""
        self.wait_for_visible(AddAssignmentLocators.SAVE_ICON_ACTIVE, timeout=timeout)

    def save_as_draft(self) -> None:
        """Нажать Save as Draft."""
        self.click(AddAssignmentLocators.SAVE_AS_DRAFT_BUTTON)

    def wait_for_url_change(self, old_url: str, timeout: int = 10) -> None:
        """Дождаться изменения URL (после сохранения)."""
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != old_url
        )

    # --- Поток создания задания (одним вызовом) ---
    def create_full_assignment(
        self,
        title: str,
        description: str,
        search_keyword: str,
        type_value: str,
        open_question: str = None,
        paragraph_question: str = None,
        single_question: str = None,
        single_options: list = None,
        multiple_question: str = None,
        multiple_options: list = None,
        range_question: str = None,
        left_pole: str = None,
        right_pole: str = None,
        range_min=None,
        range_max=None,
        image_question: str = None,
        image_path: str = None,
    ) -> None:
        """Заполнить форму задания и сохранить как черновик (минимально — заголовок, описание, поиск, тип, язык)."""
        self.open_add_assignment_form()
        self.fill_title_and_description(title, description)
        self.search_and_select_image(search_keyword)
        self.select_type(type_value)
        self.select_language_english()

        if open_question:
            self.add_open_question(open_question)
        if paragraph_question:
            self.add_text_question(paragraph_question)
        if single_question and single_options:
            self.add_single_choice_question(single_question, single_options)
        if multiple_question and multiple_options:
            self.add_multiple_choice_question(multiple_question, multiple_options)
        if range_question is not None and left_pole and right_pole and range_min is not None and range_max is not None:
            self.add_range_question(range_question, left_pole, right_pole, range_min, range_max)
        if image_question and image_path:
            self.add_image_question(image_question, image_path)
            self.wait_save_icon_active()

        self.save_as_draft()

    # --- My Tasks: редактирование и удаление ---
    def open_my_tasks(self) -> None:
        """Перейти в раздел My Tasks."""
        self.click(EditDeleteAssignmentLocators.MY_TASKS_BUTTON)

    def wait_for_assignment_tiles(self, timeout: int = 5) -> None:
        """Дождаться появления карточек заданий на странице My Tasks."""
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".assignment-tile"))
        )

    def click_edit_first_assignment(self) -> None:
        """Нажать Edit у первого задания в списке."""
        edit_buttons = self.driver.find_elements(*EditDeleteAssignmentLocators.EDIT_BUTTON)
        assert edit_buttons, "Нет кнопок редактирования"
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(edit_buttons[0])
        )
        edit_buttons[0].click()

    def append_title_and_description(self, title_append: str, description_append: str) -> None:
        """Дописать к заголовку и описанию без очистки (для редактирования)."""
        self.find(AddAssignmentLocators.TITLE_INPUT).send_keys(title_append)
        self.find(AddAssignmentLocators.DESCRIPTION_INPUT).send_keys(description_append)

    def change_view_to_preview(self) -> None:
        """Переключить вид на предпросмотр (иконка глаза)."""
        self.click(EditDeleteAssignmentLocators.CHANGE_VIEW_ICON)

    def click_back_from_edit(self) -> None:
        """Нажать Back в форме редактирования."""
        self.click(EditDeleteAssignmentLocators.BACK_EDIT_BUTTON, timeout=10)

    def wait_for_assignments_page(self, timeout: int = 25) -> None:
        """Дождаться перехода на страницу заданий (HEAD_URL)."""
        self.wait_for_url_contains(Doctor.HEAD_URL, timeout=timeout)

    def delete_assignment_by_title(self, title_text: str) -> None:
        """Найти карточку задания по заголовку и удалить (подтвердить удаление)."""
        assignment_card = self.driver.find_element(
            By.XPATH,
            f"//div[contains(@class, 'assignment-tile')][.//h3[normalize-space()='{title_text}']]"
        )
        delete_btn = assignment_card.find_element(
            *EditDeleteAssignmentLocators.DELETE_BUTTON_IN_CARD
        )
        delete_btn.click()
        self.click(EditDeleteAssignmentLocators.CONFIRM_DELETE_BUTTON, timeout=5)
