from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

file_path = os.path.abspath("todo.html")
URL = "file://" + file_path


def setup_browser():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    return driver


def add_task(driver, task_text):
    input_box = driver.find_element(By.ID, "new-todo")
    input_box.send_keys(task_text)
    input_box.send_keys(Keys.ENTER)
    time.sleep(1)


def complete_task(driver):
    task_item = driver.find_element(By.TAG_NAME, "li")
    task_item.click()
    time.sleep(1)


def delete_task(driver):
    delete_btn = driver.find_element(By.CLASS_NAME, "delete-btn")
    delete_btn.click()
    time.sleep(1)


def close_browser(driver):
    driver.quit()


if __name__ == "__main__":
    print("🚀 Running To-Do App Selenium Test...")

    driver = setup_browser()

    try:
        add_task(driver, "Selenium test task")
        print("✅ Task added")

        complete_task(driver)
        print("✅ Task marked complete")

        delete_task(driver)
        print("✅ Task deleted")

    except Exception as e:
        print("❌ Test failed:", e)

    finally:
        close_browser(driver)
        print("🔚 Browser closed")
