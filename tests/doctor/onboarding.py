from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OnboardingLocators, AddAssignmentOnboardingLocators, ClientOnboardingLocators
from data.texts_onboarding  import OnboardingTexts, AddAssignmentOnboardingTexts, ClientOnboardingTexts




class TestOnboarding:

    def test_main_onboarding(self, login_doctor):
        driver = login_doctor

        # --- Step 1 ---
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(OnboardingLocators.WELCOME_ICON)
        )
        driver.find_element(*OnboardingLocators.LETS_START_BUTTON).click()

        # --- Steps 2–10 ---
        steps = [
            (OnboardingLocators.STEP_2_MESSAGE, OnboardingTexts.STEP_2_MESSAGE),
            (OnboardingLocators.STEP_3_MESSAGE, OnboardingTexts.STEP_3_MESSAGE),
            (OnboardingLocators.STEP_4_MESSAGE, OnboardingTexts.STEP_4_MESSAGE),
            (OnboardingLocators.STEP_5_MESSAGE, OnboardingTexts.STEP_5_MESSAGE),
            (OnboardingLocators.STEP_6_MESSAGE, OnboardingTexts.STEP_6_MESSAGE),
            (OnboardingLocators.STEP_7_MESSAGE, OnboardingTexts.STEP_7_MESSAGE),
            (OnboardingLocators.STEP_8_MESSAGE, OnboardingTexts.STEP_8_MESSAGE),
            (OnboardingLocators.STEP_9_MESSAGE, OnboardingTexts.STEP_9_MESSAGE),
            (OnboardingLocators.STEP_10_MESSAGE, OnboardingTexts.STEP_10_MESSAGE),
        ]

        for locator, expected_text in steps:
            WebDriverWait(driver, 3).until(
                EC.text_to_be_present_in_element(locator, expected_text)
            )

            # Проверяем, что текст корректный
            message = driver.find_element(*locator).text
            assert expected_text in message

            # Кликаем “Next”
            driver.execute_script(
                "arguments[0].click();",
                driver.find_element(*OnboardingLocators.NEXT_BUTTON)
            )



    def test_full_onboarding_flow(self, login_without_onboarding):
        # Прохождение 3 онбордингов подряд: Add Assignment → Clients → Client Profile
        driver = login_without_onboarding

        # === ADD ASSIGNMENT ===
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AddAssignmentOnboardingLocators.ADD_ASSIGNMENT_BUTTON)
        )
        driver.find_element(*AddAssignmentOnboardingLocators.ADD_ASSIGNMENT_BUTTON).click()

        add_steps = [
            (AddAssignmentOnboardingLocators.STEP_1_MESSAGE_ADDASSIG, AddAssignmentOnboardingTexts.STEP_1_MESSAGE_ASSIG),
            (AddAssignmentOnboardingLocators.STEP_2_MESSAGE_ADDASSIG, AddAssignmentOnboardingTexts.STEP_2_MESSAGE_ASSIG),
            (AddAssignmentOnboardingLocators.STEP_3_MESSAGE_ADDASSIG, AddAssignmentOnboardingTexts.STEP_3_MESSAGE_ASSIG),
            (AddAssignmentOnboardingLocators.STEP_4_MESSAGE_ADDASSIG, AddAssignmentOnboardingTexts.STEP_4_MESSAGE_ASSIG),
            (AddAssignmentOnboardingLocators.STEP_5_MESSAGE_ADDASSIG, AddAssignmentOnboardingTexts.STEP_5_MESSAGE_ASSIG),
        ]
        self._run_onboarding_steps(driver, add_steps)

        # === CLIENTS PAGE ===
        driver.find_element(*ClientOnboardingLocators.CLIENTS_MENU_BUTTON).click()

        client_steps = [
            (ClientOnboardingLocators.STEP_1_MESSAGE_CLIENTS, ClientOnboardingTexts.STEP_1_MESSAGE_CLIENTS),
            (ClientOnboardingLocators.STEP_2_MESSAGE_CLIENTS, ClientOnboardingTexts.STEP_2_MESSAGE_CLIENTS),
        ]
        self._run_onboarding_steps(driver, client_steps)

        # === CLIENT PROFILE ===
        driver.find_element(*ClientOnboardingLocators.CLIENT_LINK).click()

        profile_steps = [
            (ClientOnboardingLocators.STEP_1_CLIENT_PROFILE, ClientOnboardingTexts.STEP_1_MESSAGE_CLIENT_PROFILE),
            (ClientOnboardingLocators.STEP_2_CLIENT_PROFILE, ClientOnboardingTexts.STEP_2_MESSAGE_CLIENT_PROFILE),
            (ClientOnboardingLocators.STEP_3_CLIENT_PROFILE, ClientOnboardingTexts.STEP_3_MESSAGE_CLIENT_PROFILE),
        ]
        self._run_onboarding_steps(driver, profile_steps)


    # ===== Универсальный метод для всех онбордингов =====
    def _run_onboarding_steps(self, driver, steps):

        for locator, expected_text in steps:
            WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element(locator, expected_text)
            )

            message = driver.find_element(*locator).text
            assert expected_text in message, f"Неверный текст: {message}"

            next_btn = driver.find_element(*OnboardingLocators.NEXT_BUTTON)
            driver.execute_script("arguments[0].click();", next_btn)


            

    



    



    
