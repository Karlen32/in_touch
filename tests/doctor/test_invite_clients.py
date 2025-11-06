from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.cliets_locators import ClientPageLocators
from data.texts_clients_page import ClientsPagetexts
from utils.config import Doctor



class TestInviteClients:
    def test_invite_client(self, driver_with_storage):
        driver = driver_with_storage

        # Переходим в раздел Clients
        driver.find_element(*ClientPageLocators.CLIENTS_MENU).click()
        # Нажимаем кнопку Add client
        driver.find_element(*ClientPageLocators.ADD_CLIENT_BUTTON).click()

        # Ожидаем появления заголовка окна добавления клиента
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(ClientPageLocators.ADD_CLIENT_TITLE)
        )
        # Вводим имя клиента
        driver.find_element(*ClientPageLocators.FIRST_NAME_INPUT).send_keys(ClientsPagetexts.FIRST_NAME_TEXT)
        # 5️⃣Вводим email клиента
        driver.find_element(*ClientPageLocators.EMAIL_INPUT).send_keys(ClientsPagetexts.EMAIL_TEXT)
        # Нажимаем кнопку Submit
        driver.find_element(*ClientPageLocators.SUBMIT_ADD_CLIENT_BUTTON).click()
        
        # Проверяем, что произошёл переход на страницу Clients
        WebDriverWait(driver, 5).until(lambda d: Doctor.CLIENTS_URL in d.current_url)
        assert Doctor.CLIENTS_URL in driver.current_url



    def test_edit_client_about(self, driver_with_storage):
        driver = driver_with_storage

        # Переход в Clients
        driver.find_element(*ClientPageLocators.CLIENTS_MENU).click()

        # Клик по клиенту в списке
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(ClientPageLocators.CLIENT_LINK)
        ).click()

        # Ждём появления кнопки Edit Client и кликаем
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(ClientPageLocators.EDIT_CLIENT_BUTTON)
        ).click()

        # Ждём появления поля About
        WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(ClientPageLocators.ABOUT_INPUT)
        )

        # Вводим текст
        driver.find_element(*ClientPageLocators.ABOUT_INPUT).send_keys(
                ClientsPagetexts.ABOUT_CLIENT_TEXT
        )

        # Сохраняем изменения
        WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(ClientPageLocators.SAVE_CHANGES_BUTTON)
        ).click()

        # Проверяем, что окно редактирования закрылось и текст сохранился
        saved_text = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(ClientPageLocators.CLIENT_ABOUT_TEXT)
        ).text

        assert saved_text == ClientsPagetexts.ABOUT_CLIENT_TEXT

        

    
    def test_cancel_client_deletion(self, driver_with_storage):
        driver = driver_with_storage

        # Переходим в раздел Clients
        driver.find_element(*ClientPageLocators.CLIENTS_MENU).click()
        # Нажимаем кнопку удаления клиента
        driver.find_element(*ClientPageLocators.DELETE_CLIENT_BUTTON).click()

        # Проверяем, что появилось окно подтверждения удаления — первая строка текста
        text1 = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(ClientPageLocators.DELETE_CONFIRM_TEXT_1)
        ).text
        assert text1 == ClientsPagetexts.DELETE_CONFIRM_TEXT_1

        # Проверяем вторую строку текста
        text2 = driver.find_element(*ClientPageLocators.DELETE_CONFIRM_TEXT_2).text
        assert text2 == ClientsPagetexts.DELETE_CONFIRM_TEXT_2
       
        # Находим и кликаем по кнопке Cancel
        cancel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ClientPageLocators.CANCEL_DELETE_BUTTON)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cancel_button)
        driver.execute_script("arguments[0].click();", cancel_button)
        
        # Проверяем, что окно подтверждения удаления закрылось
        WebDriverWait(driver, 5).until_not(
            EC.presence_of_element_located(ClientPageLocators.DELETE_CONFIRM_TEXT_1)
        )


    def test_client_deletion(self, driver_with_storage):
        driver = driver_with_storage

        # Переходим в раздел Clients
        driver.find_element(*ClientPageLocators.CLIENTS_MENU).click()
        # Нажимаем кнопку удаления клиента
        driver.find_element(*ClientPageLocators.DELETE_CLIENT_BUTTON).click()

        # Подтверждаем удаление клиента
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ClientPageLocators.CONFIRM_DELETE_BUTTON)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_button)
        driver.execute_script("arguments[0].click();", confirm_button)

        # Проверяем, что окно подтверждения исчезло
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located(ClientPageLocators.DELETE_CONFIRM_TEXT_1)
        )





