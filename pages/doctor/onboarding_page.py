"""Page Object для онбординга врача (главный онбординг, Add Assignment, Clients, Client Profile)."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.onboarding_locators import (
    OnboardingLocators,
    AddAssignmentOnboardingLocators,
    ClientOnboardingLocators,
)
from data.texts_onboarding import (
    OnboardingTexts,
    AddAssignmentOnboardingTexts,
    ClientOnboardingTexts,
)


class OnboardingPage(BasePage):
    """Онбординг: приветствие, шаги по разделам (Add Assignment, Clients, Client Profile)."""

    def wait_welcome_visible(self, timeout: int = 5) -> None:
        """Дождаться появления приветственного экрана."""
        self.wait_for_visible(OnboardingLocators.WELCOME_ICON, timeout=timeout)

    def click_lets_start(self) -> None:
        """Нажать кнопку Let's start!"""
        self.click(OnboardingLocators.LETS_START_BUTTON)

    def run_steps(self, steps: list, timeout: int = 5) -> None:
        """
        Пройти шаги онбординга: для каждой пары (locator, expected_text)
        дождаться текста в элементе, проверить и нажать Next.
        """
        for locator, expected_text in steps:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, expected_text)
            )
            message = self.find(locator).text
            assert expected_text in message, f"Неверный текст: {message}"
            next_btn = self.find(OnboardingLocators.NEXT_BUTTON)
            self.driver.execute_script("arguments[0].click();", next_btn)

    def run_main_onboarding_steps_2_to_10(self) -> None:
        """Шаги 2–10 главного онбординга (Library, Favorites, My tasks, ...)."""
        steps = [
            (OnboardingLocators.STEP_MESSAGES[i], getattr(OnboardingTexts, f"STEP_{i}_MESSAGE"))
            for i in range(2, 11)
        ]
        self.run_steps(steps, timeout=3)

    def run_add_assignment_onboarding_steps(self) -> None:
        """Шаги онбординга раздела Add Assignment (1–5)."""
        steps = [
            (
                getattr(AddAssignmentOnboardingLocators, f"STEP_{i}_MESSAGE_ADDASSIG"),
                getattr(AddAssignmentOnboardingTexts, f"STEP_{i}_MESSAGE_ASSIG"),
            )
            for i in range(1, 6)
        ]
        self.run_steps(steps, timeout=5)

    def wait_add_assignment_button_visible(self, timeout: int = 5) -> None:
        """Дождаться появления кнопки Add Assignment на экране."""
        self.wait_for_visible(
            AddAssignmentOnboardingLocators.ADD_ASSIGNMENT_BUTTON,
            timeout=timeout,
        )

    def click_add_assignment_onboarding(self) -> None:
        """Нажать кнопку Add Assignment в онбординге."""
        self.click(AddAssignmentOnboardingLocators.ADD_ASSIGNMENT_BUTTON)

    def click_clients_menu_onboarding(self) -> None:
        """Нажать пункт меню Clients в онбординге."""
        self.click(ClientOnboardingLocators.CLIENTS_MENU_BUTTON)

    def run_clients_onboarding_steps(self) -> None:
        """Шаги онбординга раздела Clients (1–2)."""
        steps = [
            (ClientOnboardingLocators.STEP_1_MESSAGE_CLIENTS, ClientOnboardingTexts.STEP_1_MESSAGE_CLIENTS),
            (ClientOnboardingLocators.STEP_2_MESSAGE_CLIENTS, ClientOnboardingTexts.STEP_2_MESSAGE_CLIENTS),
        ]
        self.run_steps(steps, timeout=5)

    def click_client_link_onboarding(self) -> None:
        """Клик по ссылке клиента в онбординге."""
        self.click(ClientOnboardingLocators.CLIENT_LINK)

    def run_client_profile_onboarding_steps(self) -> None:
        """Шаги онбординга профиля клиента (1–3)."""
        steps = [
            (ClientOnboardingLocators.STEP_1_CLIENT_PROFILE, ClientOnboardingTexts.STEP_1_MESSAGE_CLIENT_PROFILE),
            (ClientOnboardingLocators.STEP_2_CLIENT_PROFILE, ClientOnboardingTexts.STEP_2_MESSAGE_CLIENT_PROFILE),
            (ClientOnboardingLocators.STEP_3_CLIENT_PROFILE, ClientOnboardingTexts.STEP_3_MESSAGE_CLIENT_PROFILE),
        ]
        self.run_steps(steps, timeout=5)
