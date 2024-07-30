from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CheckGrades:

    def __init__(self, username, password) -> None:
        self.url = "https://moj.esdnevnik.rs/login"
        self.username = username
        self.password = password
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.url)
    
    def log_in(self):
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')

        username_field.send_keys(self.username)
        password_field.send_keys(self.password)

        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        login_button.click()
    
    def select_school(self):
        schools_list = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//li[@class="has-dropdown" and .//div[@name="schools"]]'))
        )
        schools_list.click()

        school = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Техничка школа"]'))
        )
        school.click()
    
    def select_class(self):
        grades = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[span[text()="Оцене"]]'))
        )
        grades.click()

        math = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[.//div[@class="course-name" and contains(text(), "Математика")]]'))
        )
        
        math.click()

    
    def check_math_grades(self):
        self.log_in()
        self.select_school()
        self.select_class()


    


def main():

    dimi = CheckGrades('enter_your_email', 'enter_your_password')
    dimi.check_math_grades()
    time.sleep(1000000)
    dimi.driver.quit()


if __name__ == "__main__":
    main()



