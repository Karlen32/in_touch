"""Тесты создания, редактирования и удаления заданий (Page Object)."""

from locators.add_assignment_locators import AddAssignmentLocators
from data.texts_add_assignment import AddAssignmentTexts
from pages.doctor.add_assignment_page import AddAssignmentPage


class TestCreateHomework:
    """Тесты заданий врача."""

    def test_create_homework(self, add_assignment_page: AddAssignmentPage):
        """Создание задания с разными типами вопросов и сохранение как черновик."""
        add_assignment_page.open_add_assignment_form()
        add_assignment_page.fill_title_and_description(
            AddAssignmentTexts.TITLE,
            AddAssignmentTexts.DESCRIPTION,
        )
        add_assignment_page.search_and_select_image(AddAssignmentTexts.SEARCH_KEYWORD)
        add_assignment_page.select_type(AddAssignmentTexts.TYPE)
        add_assignment_page.select_language_english()

        add_assignment_page.add_open_question(AddAssignmentTexts.OPEN_QUESTION)
        add_assignment_page.add_text_question(AddAssignmentTexts.PARAGRAPH_QUESTION)
        add_assignment_page.add_single_choice_question(
            AddAssignmentTexts.SINGLE_QUESTION,
            AddAssignmentTexts.SINGLE_CHOICE_OPTIONS[:3],
        )
        add_assignment_page.add_multiple_choice_question(
            AddAssignmentTexts.MULTIPLE_QUESTION,
            AddAssignmentTexts.MULTIPLE_CHOICE_OPTIONS[:3],
        )
        add_assignment_page.add_range_question(
            AddAssignmentTexts.RANGE_QUESTION,
            AddAssignmentTexts.LEFT_POLE,
            AddAssignmentTexts.RIGHT_POLE,
            AddAssignmentTexts.RANGE_MIN,
            AddAssignmentTexts.RANGE_MAX,
        )
        add_assignment_page.add_image_question(
            AddAssignmentTexts.IMAGE_QUESTION,
            AddAssignmentLocators.MY_IMAGE,
        )
        add_assignment_page.wait_save_icon_active()

        old_url = add_assignment_page.get_current_url()
        add_assignment_page.save_as_draft()
        add_assignment_page.wait_for_url_change(old_url)

        new_url = add_assignment_page.get_current_url()
        assert new_url != old_url, f"URL не изменился (остался {new_url})"

    def test_edit_homework(self, add_assignment_page: AddAssignmentPage):
        """Редактирование задания из My Tasks и сохранение."""
        add_assignment_page.open_my_tasks()
        add_assignment_page.click_edit_first_assignment()

        add_assignment_page.append_title_and_description(
            AddAssignmentTexts.EDIT_TITLE,
            AddAssignmentTexts.EDIT_DESCRIPTION,
        )
        add_assignment_page.search_and_select_image(AddAssignmentTexts.EDIT_SEARCH_KEYWORD)
        add_assignment_page.select_type("exercise")
        add_assignment_page.select_language_french()

        add_assignment_page.append_open_question(AddAssignmentTexts.EDIT_OPEN_QUESTION)
        add_assignment_page.append_text_question(AddAssignmentTexts.EDIT_PARAGRAPH_QUESTION)
        add_assignment_page.append_single_question(
            AddAssignmentTexts.EDIT_SINGLE_QUESTION,
            AddAssignmentTexts.SINGLE_CHOICE_OPTIONS[3],
        )
        add_assignment_page.append_multiple_question(
            AddAssignmentTexts.EDIT_MULTIPLE_QUESTION,
            AddAssignmentTexts.MULTIPLE_CHOICE_OPTIONS[3],
        )
        add_assignment_page.append_range_question(
            AddAssignmentTexts.EDIT_RANGE_QUESTION,
            AddAssignmentTexts.LEFT_POLE,
            AddAssignmentTexts.RIGHT_POLE,
            AddAssignmentTexts.RANGE_MIN,
            AddAssignmentTexts.RANGE_MAX,
        )
        add_assignment_page.append_image_question_and_upload(
            AddAssignmentTexts.EDIT_IMAGE_QUESTION,
            AddAssignmentLocators.MY_IMAGE_EDIT,
        )

        add_assignment_page.change_view_to_preview()
        add_assignment_page.click_back_from_edit()

        add_assignment_page.save_as_draft()
        add_assignment_page.wait_for_assignments_page()

        assert "assignments" in add_assignment_page.get_current_url()

    def test_delete_homework(self, add_assignment_page: AddAssignmentPage):
        """Удаление задания по заголовку из My Tasks."""
        add_assignment_page.open_my_tasks()
        add_assignment_page.wait_for_assignment_tiles(timeout=5)
        title_text = "Daily English Practice — Lesson 1"
        add_assignment_page.delete_assignment_by_title(title_text)
