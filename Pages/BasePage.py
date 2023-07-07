class BaseP:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://ya.ru/"

    def go_to_site(self):
        return self.browser.get(self.base_url)

    def get_url(self):
        return self.browser.current_url

    def close_browser(self):
        self.browser.quit()
