from selenium.webdriver.common.by import By



class ShareAssignmentLocators:

    # --- Шаринг заданий клиенту через линк клиента ---
    CLIENTS_MENU = (By.XPATH, "//a[@href='/clients' and contains(., 'Clients')]")
    CLIENT_LINK = (By.XPATH, "//a[contains(@href, '/clients/') and contains(@class, 'link-to-client')]")
    ASSIGNMENTS_BUTTON = (By.XPATH, "//button[@id='client-assignments-onboarding']")
    SHARE_ASSIGNMENT_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Share assignment']]")
    CHOOSE_ASSIGNMENT_TITLE = (By.XPATH, "//h3[@class='share-assignment__title' and normalize-space(text())='Choose assignment you want to share']")
    ASSIGNMENT_TITLE = (By.XPATH, "//h3[normalize-space(text())='Values Clarification and Alignment']")
    # ASSIGNMENT_TILE = (By.CSS_SELECTOR,"div.assignment-tile.assignment-tile_selected")
    LIBRARY_ASSIGNMENT_IMAGE = (By.XPATH, "//img[contains(@src, 'unsplash.com')]")

    SHARE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Share']]")
    SUCCESS_ASSIGNMENT_SENT_TITLE = (By.XPATH, "//h2[normalize-space(text())='Assignment has been successfully sent!']")
    OK_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='OK']]")

    # --- Шаринг заданий клиентам с библеотеки ---
    SHARE_WITH_CLIENT_BUTTON = (By.CSS_SELECTOR, "button.assignment-actions__share-with-client")
    SHARE_MODAL_TITLE = (By.XPATH, "//h3[@class='share-assignment__title' and normalize-space(text())='Share assignment with...']")
    SHARE_ASSIGNMENT_CLIENT_CHECKBOX = (By.CSS_SELECTOR, "input.share-assignment__checkbox")
    SHARE_ASSIGNMENT_CONFIRM_BUTTON = (By.XPATH, "//button[.//p[text()='Share']]")
    SHARE_ASSIGNMENT_SUCCESS_TITLE = (By.XPATH,"//h2[@class='share-assignment__title' and text()='Assignment has been successfully shared!']")
    SHARE_ASSIGNMENT_OK_BUTTON = (By.XPATH, "//button[.//p[text()='OK']]")

    # --- Просмотр выполненных заданий ---
    ASSIGNMENT_STATUS_BLOCK = (By.XPATH, "//div[contains(@class, 'date-and-type')]")
    VIEW_DONE_ASSIGNMENT_BUTTON = (By.XPATH, "//button[@title='view done assignment']")

    # --- Отозвать задания у клиента ---
    RECALL_ASSIGNMENT_BUTTON = (By.XPATH, "//button[contains(@class, 'assignment-actions__share-with-client_recall')]")
    RECALL_CONFIRM_TEXT = (By.XPATH,"//p[contains(., 'recall') and contains(., 'assignment')]")
    CANCEL_BUTTON = (By.XPATH,"//button[.//p[normalize-space(text())='Cancel']]")

    # --- Добавление в избранное (Favorites) ---
    FAVORITE_BUTTON = (By.CSS_SELECTOR, "button.favorite-button")
    FAVORITE_BUTTON_SELECTED = (By.CSS_SELECTOR, "button.favorite-button.favorite-button_selected")
    FAVORITES_TAB_BUTTON = (By.ID, "onboarding-favorites")
