import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://test24.intouch.care"

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(URL)
        print("Открылся браузер. Пройди онбординг или авторизацию вручную (у тебя 60 секунд)...")
        for remaining in range(60, 0, -1):
            print(f"Ожидание: {remaining} сек...", end="\r", flush=True)
            time.sleep(1)
        print()

        # Получаем localStorage из браузера
        local_storage_data = driver.execute_script(
            "return JSON.stringify(window.localStorage);"
        )

        # Сохраняем в файл
        with open("localstorage.json", "w", encoding="utf-8") as f:
            f.write(local_storage_data)

        print("✅ localStorage сохранён в localstorage.json")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()