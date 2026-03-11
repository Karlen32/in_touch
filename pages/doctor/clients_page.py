"""Page Object для страницы клиентов врача (список, добавление, редактирование, удаление)."""

from pages.base_page import BasePage
from locators.cliets_locators import ClientPageLocators
from utils.config import Doctor


class DoctorClientsPage(BasePage):
    """Страница раздела Clients в кабинете врача."""

    def __init__(self, driver, base_url: str = None):
        super().__init__(driver, base_url or Doctor.BASE)

    def open_clients_page(self) -> None:
        """Перейти в раздел Clients (клик по пункту меню)."""
        self.click(ClientPageLocators.CLIENTS_MENU)

    def open_add_client_dialog(self) -> None:
        """Открыть диалог добавления клиента."""
        self.click(ClientPageLocators.ADD_CLIENT_BUTTON)
        self.wait_for_visible(ClientPageLocators.ADD_CLIENT_TITLE, timeout=3)

    def fill_client_form(self, first_name: str, email: str) -> None:
        """Заполнить форму добавления клиента (имя и email)."""
        self.type_text(ClientPageLocators.FIRST_NAME_INPUT, first_name)
        self.type_text(ClientPageLocators.EMAIL_INPUT, email)

    def submit_add_client(self) -> None:
        """Нажать кнопку добавления клиента в диалоге."""
        self.click(ClientPageLocators.SUBMIT_ADD_CLIENT_BUTTON)

    def create_client(self, first_name: str, email: str) -> None:
        """Открыть диалог, заполнить форму и отправить (добавить клиента)."""
        self.open_add_client_dialog()
        self.fill_client_form(first_name, email)
        self.submit_add_client()

    def expect_on_clients_page(self, timeout: int = 5) -> None:
        """Дождаться перехода на страницу списка клиентов."""
        self.wait_for_url_contains(Doctor.CLIENTS_URL, timeout=timeout)

    def open_client_profile(self) -> None:
        """Открыть профиль первого клиента в списке (клик по ссылке)."""
        self.click(ClientPageLocators.CLIENT_LINK, timeout=5)

    def click_edit_client(self) -> None:
        """Нажать кнопку Edit Client."""
        self.click(ClientPageLocators.EDIT_CLIENT_BUTTON, timeout=5)

    def fill_about(self, text: str) -> None:
        """Заполнить поле About в форме редактирования клиента."""
        self.wait_for_visible(ClientPageLocators.ABOUT_INPUT, timeout=5)
        self.type_text(ClientPageLocators.ABOUT_INPUT, text)

    def save_client_changes(self) -> None:
        """Нажать Save Changes в форме редактирования."""
        self.click(ClientPageLocators.SAVE_CHANGES_BUTTON, timeout=5)

    def edit_client_about(self, text: str) -> None:
        """Открыть редактирование, ввести текст в About и сохранить."""
        self.click_edit_client()
        self.fill_about(text)
        self.save_client_changes()

    def get_client_about_text(self, timeout: int = 5) -> str:
        """Получить сохранённый текст блока About в профиле клиента."""
        return self.get_text(ClientPageLocators.CLIENT_ABOUT_TEXT, timeout=timeout)

    def open_delete_client_dialog(self) -> None:
        """Открыть диалог подтверждения удаления клиента (кнопка удаления)."""
        self.click(ClientPageLocators.DELETE_CLIENT_BUTTON)

    def get_delete_confirm_text_1(self, timeout: int = 3) -> str:
        """Текст первой строки в диалоге подтверждения удаления."""
        return self.get_text(ClientPageLocators.DELETE_CONFIRM_TEXT_1, timeout=timeout)

    def get_delete_confirm_text_2(self) -> str:
        """Текст второй строки в диалоге подтверждения удаления."""
        return self.get_text(ClientPageLocators.DELETE_CONFIRM_TEXT_2)

    def cancel_delete_client(self) -> None:
        """Нажать Cancel в диалоге удаления (через JS-клик)."""
        self.click_via_script(ClientPageLocators.CANCEL_DELETE_BUTTON, timeout=10)

    def confirm_delete_client(self) -> None:
        """Подтвердить удаление клиента (Yes, Delete) через JS-клик."""
        self.click_via_script(ClientPageLocators.CONFIRM_DELETE_BUTTON, timeout=10)

    def wait_delete_dialog_closed(self, timeout: int = 10) -> bool:
        """Дождаться исчезновения диалога подтверждения удаления."""
        return self.wait_for_not_present(ClientPageLocators.DELETE_CONFIRM_TEXT_1, timeout=timeout)
