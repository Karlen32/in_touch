"""Тесты приглашения, редактирования и удаления клиентов (Page Object)."""

from data.texts_clients_page import ClientsPagetexts
from pages.doctor.clients_page import DoctorClientsPage
from utils.config import Doctor


class TestInviteClients:
    """Тесты раздела Clients."""

    def test_invite_client(self, doctor_clients_page: DoctorClientsPage):
        """Добавление нового клиента и переход на страницу Clients."""
        doctor_clients_page.open_clients_page()
        doctor_clients_page.create_client(
            ClientsPagetexts.FIRST_NAME_TEXT,
            ClientsPagetexts.EMAIL_TEXT,
        )
        doctor_clients_page.expect_on_clients_page()
        assert Doctor.CLIENTS_URL in doctor_clients_page.get_current_url()

    def test_edit_client_about(self, doctor_clients_page: DoctorClientsPage):
        """Редактирование поля About в профиле клиента."""
        doctor_clients_page.open_clients_page()
        doctor_clients_page.open_client_profile()
        doctor_clients_page.edit_client_about(ClientsPagetexts.ABOUT_CLIENT_TEXT)
        saved_text = doctor_clients_page.get_client_about_text()
        assert saved_text == ClientsPagetexts.ABOUT_CLIENT_TEXT

    def test_cancel_client_deletion(self, doctor_clients_page: DoctorClientsPage):
        """Отмена удаления клиента: диалог подтверждения закрывается."""
        doctor_clients_page.open_clients_page()
        doctor_clients_page.open_delete_client_dialog()

        text1 = doctor_clients_page.get_delete_confirm_text_1()
        assert text1 == ClientsPagetexts.DELETE_CONFIRM_TEXT_1

        text2 = doctor_clients_page.get_delete_confirm_text_2()
        assert text2 == ClientsPagetexts.DELETE_CONFIRM_TEXT_2

        doctor_clients_page.cancel_delete_client()
        doctor_clients_page.wait_delete_dialog_closed()

    def test_client_deletion(self, doctor_clients_page: DoctorClientsPage):
        """Удаление клиента: подтверждение и закрытие диалога."""
        doctor_clients_page.open_clients_page()
        doctor_clients_page.open_delete_client_dialog()
        doctor_clients_page.confirm_delete_client()
        doctor_clients_page.wait_delete_dialog_closed()
