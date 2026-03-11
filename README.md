# in_touch

UI-тесты для приложения INtouch (Selenium + pytest). Проект организован по паттерну **Page Object**: тесты описывают сценарии, а взаимодействие с UI вынесено в классы страниц.

## Структура проекта

- **`pages/`** — Page Object классы:
  - `base_page.py` — базовый класс с общими методами (клик, ввод, ожидания, навигация).
  - `login_page.py` — страница логина.
  - `doctor/` — сценарии врача:
    - `clients_page.py` — раздел клиентов (добавление, редактирование, удаление).
    - `add_assignment_page.py` — форма создания/редактирования задания и список заданий (My Tasks).
    - `share_assignment_page.py` — шаринг заданий клиенту.
    - `onboarding_page.py` — онбординг (приветствие, Add Assignment, Clients, Client Profile).
- **`locators/`** — селекторы элементов (используются только в Page Object).
- **`tests/`** — тесты (используют Page Object и данные из `data/`).
- **`data/`** — тестовые тексты и константы.
- **`utils/`** — конфиг (URL), учётные данные.

## Запуск тестов

```bash
pytest tests/ -v
# или отдельный файл:
pytest tests/tests_login.py -v
pytest tests/doctor/test_invite_clients.py -v
```

Для части тестов нужен предзаполненный `localstorage.json` (фикстура `driver_with_storage`). Создать его можно скриптом `save_cookies.py` (или аналогом сохранения localStorage).

## Пример использования Page Object в тесте

```python
def test_login_valid(self, login_page: LoginPage):
    login_page.open_login()
    login_page.login_as_doctor()
    login_page.expect_success_login()
    assert "/assignments" in login_page.get_current_url()
```

```python
def test_invite_client(self, doctor_clients_page: DoctorClientsPage):
    doctor_clients_page.open_clients_page()
    doctor_clients_page.create_client(
        ClientsPagetexts.FIRST_NAME_TEXT,
        ClientsPagetexts.EMAIL_TEXT,
    )
    doctor_clients_page.expect_on_clients_page()
```

## Добавление новых тестов

1. Если новая страница или поток — добавить класс в `pages/` (наследование от `BasePage`), методы для действий и проверок, локаторы в `locators/` при необходимости.
2. В `conftest.py` при необходимости добавить фикстуру, возвращающую нужный Page Object (например, `add_assignment_page(driver_with_storage)`).
3. В тесте использовать только методы Page Object и данные из `data/`, без прямых вызовов `driver.find_element` и `WebDriverWait`.
