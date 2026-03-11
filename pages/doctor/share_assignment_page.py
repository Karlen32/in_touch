"""Page Object для сценариев шаринга заданий клиенту."""

from pages.base_page import BasePage
from locators.share_assignment_locators import ShareAssignmentLocators


class ShareAssignmentPage(BasePage):
    """Действия по шарингу задания клиенту (из профиля клиента и из библиотеки)."""

    def open_clients_and_first_client(self) -> None:
        """Перейти в Clients и открыть первого клиента."""
        self.click(ShareAssignmentLocators.CLIENTS_MENU)
        self.wait_for_visible(ShareAssignmentLocators.CLIENT_LINK, timeout=3)
        self.click(ShareAssignmentLocators.CLIENT_LINK)

    def open_assignments_tab(self) -> None:
        """Открыть вкладку заданий у клиента."""
        self.wait_for_visible(ShareAssignmentLocators.ASSIGNMENTS_BUTTON, timeout=3)
        self.click(ShareAssignmentLocators.ASSIGNMENTS_BUTTON)

    def click_share_assignment_button(self) -> None:
        """Нажать кнопку Share assignment."""
        self.click(ShareAssignmentLocators.SHARE_ASSIGNMENT_BUTTON)

    def get_choose_assignment_modal_title(self, timeout: int = 3) -> str:
        """Получить заголовок модалки выбора задания (Choose assignment...)."""
        return self.get_text(ShareAssignmentLocators.CHOOSE_ASSIGNMENT_TITLE, timeout=timeout)

    def select_library_assignment_image(self, timeout: int = 15) -> None:
        """Выбрать задание из библиотеки (клик по изображению), с прокруткой при необходимости."""
        choice = self.find_clickable(ShareAssignmentLocators.LIBRARY_ASSIGNMENT_IMAGE, timeout=timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", choice)
        self.driver.execute_script("arguments[0].click();", choice)

    def click_share_button(self) -> None:
        """Нажать кнопку Share в модалке выбора задания."""
        self.click(ShareAssignmentLocators.SHARE_BUTTON, timeout=10)

    def get_success_sent_title(self, timeout: int = 2) -> str:
        """Получить заголовок успешной отправки (Assignment has been successfully sent!)."""
        return self.get_text(ShareAssignmentLocators.SUCCESS_ASSIGNMENT_SENT_TITLE, timeout=timeout)

    def click_ok_after_send(self) -> None:
        """Нажать OK после отправки задания."""
        self.click(ShareAssignmentLocators.OK_BUTTON)

    def wait_success_modal_closed(self, timeout: int = 2) -> bool:
        """Дождаться исчезновения модалки успешной отправки."""
        return self.wait_for_invisible(
            ShareAssignmentLocators.SUCCESS_ASSIGNMENT_SENT_TITLE,
            timeout=timeout
        )

    # --- Шаринг из библиотеки (Share assignment with...) ---
    def click_share_with_client_button(self) -> None:
        """Нажать кнопку Share with client (из карточки задания)."""
        self.click(ShareAssignmentLocators.SHARE_WITH_CLIENT_BUTTON)

    def get_share_modal_title_library(self, timeout: int = 5) -> str:
        """Заголовок модалки Share assignment with..."""
        return self.get_text(ShareAssignmentLocators.SHARE_MODAL_TITLE, timeout=timeout)

    def check_client_checkbox(self) -> None:
        """Отметить чекбокс клиента в модалке."""
        self.click(ShareAssignmentLocators.SHARE_ASSIGNMENT_CLIENT_CHECKBOX)

    def click_share_confirm_button(self) -> None:
        """Нажать Share в модалке шаринга с клиентами."""
        self.click(ShareAssignmentLocators.SHARE_ASSIGNMENT_CONFIRM_BUTTON)

    def get_share_success_title(self, timeout: int = 5) -> str:
        """Заголовок успешного шаринга (Assignment has been successfully shared!)."""
        return self.get_text(ShareAssignmentLocators.SHARE_ASSIGNMENT_SUCCESS_TITLE, timeout=timeout)

    def click_ok_after_share(self) -> None:
        """Нажать OK после шаринга."""
        self.click(ShareAssignmentLocators.SHARE_ASSIGNMENT_OK_BUTTON)

    def wait_share_success_modal_closed(self, timeout: int = 2) -> bool:
        """Дождаться исчезновения модалки успешного шаринга."""
        return self.wait_for_invisible(
            ShareAssignmentLocators.SHARE_ASSIGNMENT_SUCCESS_TITLE,
            timeout=timeout
        )
