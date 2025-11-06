from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.onboarding_locators import OnboardingLocators, AddAssignmentOnboardingLocators, ClientOnboardingLocators
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
            (OnboardingLocators.STEP_MESSAGES[i], getattr(OnboardingTexts, f"STEP_{i}_MESSAGE"))
            for i in range(2, 11)
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
            (
                getattr(AddAssignmentOnboardingLocators, f"STEP_{i}_MESSAGE_ADDASSIG"),
                getattr(AddAssignmentOnboardingTexts, f"STEP_{i}_MESSAGE_ASSIG")
            )
            for i in range(1, 6)
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


            

    



    



    
