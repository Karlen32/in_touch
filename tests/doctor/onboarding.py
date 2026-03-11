"""Тесты онбординга врача (Page Object)."""

from pages.doctor.onboarding_page import OnboardingPage


class TestOnboarding:
    """Тесты прохождения онбординга."""

    def test_main_onboarding(self, login_doctor):
        """Главный онбординг: приветствие и шаги 2–10."""
        page = OnboardingPage(login_doctor)
        page.wait_welcome_visible(timeout=5)
        page.click_lets_start()
        page.run_main_onboarding_steps_2_to_10()

    def test_full_onboarding_flow(self, login_without_onboarding):
        """Полный поток: онбординги Add Assignment → Clients → Client Profile."""
        page = OnboardingPage(login_without_onboarding)

        page.wait_add_assignment_button_visible(timeout=5)
        page.click_add_assignment_onboarding()
        page.run_add_assignment_onboarding_steps()

        page.click_clients_menu_onboarding()
        page.run_clients_onboarding_steps()

        page.click_client_link_onboarding()
        page.run_client_profile_onboarding_steps()
