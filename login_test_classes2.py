from time import sleep


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.login = username, password
        username_input = browser.find_element_by_name("username")
        username_input.click()
        username_input.send_keys("toebeans_photographs")

        password_input = browser.find_element_by_name("password")
        password_input.click()
        password_input.send_keys("photos4life")

        login_button = browser.find_element_by_xpath("//button[@type = 'submit']")
        login_button.click()

    def goto_login(self):
        return self.login

    sleep(5)


class Homepage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.instagram.com")


from selenium import webdriver

browser = webdriver.Firefox
browser.implicitly_wait(5)

home_page = Homepage(browser)
login_page = LoginPage(browser)
#username = "toebeans_photographs"
#password = "photographs4life"
login_page_2 = login_page.goto_login()


