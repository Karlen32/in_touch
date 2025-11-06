from selenium.webdriver.common.by import By



class ClientPageLocators:

    # --- Навигация и меню ---
    CLIENTS_MENU = (By.XPATH, "//a[@href='/clients' and contains(., 'Clients')]")
    ADD_CLIENT_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Add Client']]")
    ASSIGNMENTS_BUTTON = (By.XPATH, "//button[@id='client-assignments-onboarding']")
    DIARY_BUTTON = (By.XPATH, "//button[@id='client-diary-onboarding']")
    BACK_ICON = (By.XPATH, "//img[contains(@src, '417D88')]")  # стрелка "Назад"

    # --- Добавление клиента ---
    ADD_CLIENT_TITLE = (By.XPATH, "//h2[normalize-space(text())='Add Client']")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='firstName']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    SUBMIT_ADD_CLIENT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Add Client']")
    CLIENT_LINK = (By.XPATH, "//a[contains(@href, '/clients/') and contains(@class, 'link-to-client')]")

    # --- Шаринг заданий клиенту ---
    SHARE_ASSIGNMENT_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Share assignment']]")
    SHARE_MODAL_TITLE = (By.XPATH, "//h3[contains(@class, 'share-assignment__title') and normalize-space(text())='Choose assignment you want to share']")
    ASSIGNMENT_TILE = (By.XPATH, "//div[contains(@class, 'assignment-tile')]")
    SHARE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Share']]")
    SUCCESS_ASSIGNMENT_SENT_TITLE = (By.XPATH, "//h2[normalize-space(text())='Assignment has been successfully sent!']")
    OK_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='OK']]")

    # --- Отзыв задания у клиента ---
    RECALL_ASSIGNMENT_BUTTON = (By.XPATH, "//button[contains(@class, 'assignment-actions__share-with-client_recall')]")
    RECALL_CONFIRM_TEXT = (By.XPATH,"//p[contains(., 'recall') and contains(., 'assignment')]")
    CANCEL_BUTTON = (By.XPATH,"//button[.//p[normalize-space(text())='Cancel']]")



    # --- Просмотр выполненных заданий ---
    ASSIGNMENT_STATUS_BLOCK = (By.XPATH, "//div[contains(@class, 'date-and-type')]")
    VIEW_DONE_ASSIGNMENT_BUTTON = (By.XPATH, "//button[@title='view done assignment']")

    # --- Раздел "Emotion Journal" ---
    DIARY_TITLE = (By.XPATH, "//div[normalize-space(text())='Emotion Journal']")
    DIARY_CARD = (By.XPATH, "//div[contains(@class, '_diary__card_')]")
    DIARY_BACK_BUTTON = (By.XPATH, "//img[@alt='back']")

    # --- Редактирование клиента ---
    EDIT_CLIENT_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Edit Client']]")
    ABOUT_INPUT = (By.XPATH, "//input[@name='about']")
    SAVE_CHANGES_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Save Changes']]")
    CLIENT_ABOUT_TEXT = (By.XPATH,"//h3[@class='profile-about']/following-sibling::p[1]")

    # --- Удаление клиента ---
    DELETE_CLIENT_BUTTON = (By.XPATH, "//button[contains(@class, 'trash')]")
    DELETE_CONFIRM_TEXT_1 = (By.XPATH, "//p[normalize-space(text())='Are you sure you want to delete this client?']")
    DELETE_CONFIRM_TEXT_2 = (By.XPATH, "//p[contains(normalize-space(.), \"Once deleted, all the client's data will be removed from your account\")]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[.//p[contains(text(), 'Yes, Delete')]]")
    CANCEL_DELETE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Cancel']]")

