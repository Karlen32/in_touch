"""Page Object классы для сценариев врача (doctor)."""

from pages.doctor.clients_page import DoctorClientsPage
from pages.doctor.add_assignment_page import AddAssignmentPage
from pages.doctor.share_assignment_page import ShareAssignmentPage
from pages.doctor.onboarding_page import OnboardingPage

__all__ = [
    "DoctorClientsPage",
    "AddAssignmentPage",
    "ShareAssignmentPage",
    "OnboardingPage",
]
