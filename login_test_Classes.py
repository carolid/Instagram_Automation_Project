from time import sleep


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser = webdriver.Firefox()

    def login(self, username, password):
        username_input = browser.find_element_by_name("username")
        username_input.click()
        username_input.send_keys("toebeans_photographs")

        password_input = browser.find_element_by_name("password")
        password_input.click()
        password_input.send_keys("photos4life")

        login_button = browser.find_element_by_xpath("//button[@type = 'submit']")
        login_button.click()

        sleep(5)

class Homepage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.instagram.com")

