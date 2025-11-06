from selenium.webdriver.common.by import By



class EditDeleteAssignmentLocators:

    MY_TASKS_BUTTON = (By.ID, "onboarding-my-tasks")
    ASSIGNMENT_TITLE = (By.CSS_SELECTOR, ".assignment-info h3")
    EDIT_BUTTON = (By.CSS_SELECTOR, "button.assignment__edit-btn")
    DELETE_BUTTON_IN_CARD = (By.CSS_SELECTOR, "button.assignment__delete-btn")
    CHANGE_VIEW_ICON = (By.XPATH, "//img[@alt='changeView']")
    CANCEL_DELETE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Cancel']]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[.//p[normalize-space(text())='Yes, delete']]")
    BACK_EDIT_BUTTON = (By.XPATH, "//button[.//p[normalize-space()='Back']]")