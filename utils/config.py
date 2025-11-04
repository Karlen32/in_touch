class Urls:
    BASE_URL = "https://test24.intouch.care"
    LOGIN_URL = f"{BASE_URL}/login"
    RESET_PASSWORD_URL = f"{BASE_URL}/password-reset-requested"
    


class Doctor:
    BASE = Urls.BASE_URL
    HEAD_URL = f"{BASE}/assignments"
    CLIENTS_URL = f"{BASE}/clients"
    SETTINGS_URL = f"{BASE}/settings"
    FEEDBACK_URL = f"{BASE}/feedback"
    ADD_ASSIGNMENT_URL = f"{BASE}/add-assignment"
    ADD_CLIENT_URL = f"{BASE}/add-client"

    @staticmethod
    def assignment_by_id(assignment_id: int):
        return f"{Doctor.HEAD_URL}/{assignment_id}"

    @staticmethod
    def client_by_id(client_id: int):
        return f"{Doctor.CLIENTS_URL}/{client_id}"
    
    @staticmethod
    def diary_by_id(diary_id: int):
        return f"{Doctor.DIARY_URL}/{diary_id}"


class Client:
    BASE = Urls.BASE_URL
    HEAD_URL = f"{BASE}/my-assignments"
    DIARY_URL = f"{BASE}/my-diary"
    SETTINGS_URL = f"{BASE}/settings"
    FEEDBACK_URL = f"{BASE}/feedback"
    CREATE_DIARY_URL = f"{DIARY_URL}/create"

    @staticmethod
    def diary_by_id(diary_id: int):
        return f"{Client.DIARY_URL}/{diary_id}"
    
    @staticmethod
    def assignment_by_id(assignment_id: int):
        return f"{Client.HEAD_URL}/{assignment_id}"


class Admin:
    BASE = Urls.BASE_URL
    HEAD_URL = f"{BASE}/assignments"
    CLIENTS_URL = f"{BASE}/clients"
    SETTINGS_URL = f"{BASE}/settings"
    FEEDBACK_URL = f"{BASE}/feedback"
    ADD_ASSIGNMENT_URL = f"{BASE}/add-assignment"
    ADD_CLIENT_URL = f"{BASE}/add-client"
    METRICS_URL = f"{BASE}/metrics"
    STORYBOOK_URL = f"{BASE}/storybook"

    @staticmethod
    def assignment_by_id(assignment_id: int):
        return f"{Admin.HEAD_URL}/{assignment_id}"
    

    @staticmethod
    def diary_by_id(diary_id: int):
        return f"{Admin.DIARY_URL}/{diary_id}"
    
    
    