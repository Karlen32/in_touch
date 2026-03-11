"""Тесты шаринга заданий клиенту (Page Object)."""

from data.texts_clients_page import ClientsPagetexts
from pages.doctor.share_assignment_page import ShareAssignmentPage


class TestShareAssignment:
    """Тесты отправки заданий клиенту."""

    def test_share_assignment_client_link(self, share_assignment_page: ShareAssignmentPage):
        """Отправка задания клиенту через его личную ссылку (профиль клиента)."""
        share_assignment_page.open_clients_and_first_client()
        share_assignment_page.open_assignments_tab()
        share_assignment_page.click_share_assignment_button()

        title = share_assignment_page.get_choose_assignment_modal_title()
        assert title == ClientsPagetexts.SHARE_MODAL_TEXT

        share_assignment_page.select_library_assignment_image()
        share_assignment_page.click_share_button()

        sent_title = share_assignment_page.get_success_sent_title()
        assert sent_title == ClientsPagetexts.SHARE_ASSIGNMENT_SUCCESS_TEXT

        share_assignment_page.click_ok_after_send()
        share_assignment_page.wait_success_modal_closed()

    def test_share_assignment_library(self, share_assignment_page: ShareAssignmentPage):
        """Отправка задания через модалку Share assignment with... из библиотеки."""
        share_assignment_page.click_share_with_client_button()

        title = share_assignment_page.get_share_modal_title_library()
        assert title == ClientsPagetexts.SHARE_MODAL_TEXT1

        share_assignment_page.check_client_checkbox()
        share_assignment_page.click_share_confirm_button()

        text1 = share_assignment_page.get_share_success_title()
        assert text1 == ClientsPagetexts.SHARE_ASSIGNMENT_SUCCESS_TEXT1

        share_assignment_page.click_ok_after_share()
        share_assignment_page.wait_share_success_modal_closed()
