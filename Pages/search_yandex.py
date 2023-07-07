from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Pages.BasePage import BaseP


class YSelectors:
    # локаторы объектов на странице
    SEARCH_FIELD = "#text"
    SEARCH_BUTTON = "body > main > div.body__content > form > div.search3__inner > button"
    SEARCH_RESULT = "#search-result > .serp-item a.link > b"
    SEARCH_SUGGEST = "mini-suggest__popup-content"
    SEARCH_MENU = "body > main > div.body__content > form > nav > ul > li.services-suggest__list-item-more > a"
    SEARCH_PICS = "body > div.popup2.services-more-popup.services-more-popup_pinnable_yes.services-more-popup_suggest_yes.popup2_theme_normal.popup2_autoclosable_yes.popup2_services-more_yes.popup2_view_classic.i-bem.popup2_js_inited.services-more-popup_js_inited.popup2_visible_yes > div > div > div.scrollbar__scrollable > div > div.services-more-popup__section.services-more-popup__section-all > div.services-more-popup__section-content > span:nth-child(9) > a"
    SEARCH_POPULAR_PICS = "PopularRequestList"
    SEARCH_POPULAR_PICS_1 = "PopularRequestList-Shadow"
    SEARCH_FIELD_PICS = "//input[@class='input__control mini-suggest__input']"
    SHOW_PICS = "//*[@role='listitem']/div/a"
    ORIG_PICS = "MMImage-Origin"
    NEXT_PICS = "CircleButton_type_next"
    PREV_PICS = "CircleButton_type_prev"


class SearchFunc(BaseP):

    def check_exists_by_selector(self, selector):  # проверка наличия объекта по селектору
        try:
            self.browser.find_element(By.CSS_SELECTOR, selector)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_class(self, selector):  # проверка наличия объекта по названию класса
        try:
            self.browser.find_element(By.CLASS_NAME, selector)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_xpath(self, selector):  # проверка наличия объекта по xpath
        try:
            self.browser.find_element(By.XPATH, selector)
        except NoSuchElementException:
            return False
        return True

    def check_first_link(self):  # возвращает первую ссылку на странице поиска
        links = self.browser.find_elements(By.CSS_SELECTOR, "#search-result > .serp-item a.link > b")
        items = [elem.text.strip() for elem in links]
        return items[0]

    def input_word(self):  # ввод в поисковую строку запроса
        search_string = self.browser.find_element(By.CSS_SELECTOR, "#text")
        search_string.send_keys("Тензор")
        return search_string

    def click_enter(self, selector):  # нажатие на выбранный по селектору объект
        search_string = self.browser.find_element(By.CSS_SELECTOR, selector).click()
        return search_string

    def click_pics(self, selector):  # нажатие на выбранную по классу картинку
        search_string = self.browser.find_element(By.CLASS_NAME, selector).click()
        return search_string

    def click_pics_xpath(self, selector):  # нажатие на выбранную по xpath картинку
        search_string = self.browser.find_element(By.XPATH, selector).click()
        return search_string

    def get_name_pics(self):  # получение названия картинки
        links = self.browser.find_element(By.CLASS_NAME, "PopularRequestList").text.split('\n')
        first_pics = links[0]
        return first_pics

    def get_search_category(self):  # получение названия категории
        inp = self.browser.find_element(By.XPATH, "//input[@class='input__control mini-suggest__input']")
        text = inp.get_attribute("value")
        return text

    def get_src(self):  # получение ссылки картинки
        attribute = self.browser.find_element(By.CLASS_NAME, "MMImage-Origin").get_attribute("src")
        return attribute

    def change_window(self):  # смена окна браузера
        self.browser.switch_to.window(self.browser.window_handles[-1])
