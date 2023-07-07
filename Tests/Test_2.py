import time
from Pages.search_yandex import SearchFunc, YSelectors


# Запуск второго теста
def test_first_pics(browser):
    ya = SearchFunc(browser)
    ya.go_to_site()
    ya.click_enter(YSelectors.SEARCH_FIELD)

    # проверка наличия кнопки "меню"
    assert ya.check_exists_by_selector(YSelectors.SEARCH_MENU)

    ya.click_enter(YSelectors.SEARCH_MENU)  # нажимаем на меню
    ya.click_enter(YSelectors.SEARCH_PICS)  # из всплывающего окна выбираем иконку "картинки"
    ya.change_window()  # переключаемся на окрывшееся окно браузера
    # проверяем что текущий адрес страницы равен "https://yandex.ru/images"
    assert ya.get_url() == 'https://yandex.ru/images/'

    ya.click_pics(YSelectors.SEARCH_POPULAR_PICS)  # выбираем первую категорию популярных картинок
    ya.click_pics(YSelectors.SEARCH_POPULAR_PICS_1)  # выбираем поисковую строку
    # проверяем что название категории указано в поисковой строке
    assert ya.get_name_pics() == ya.get_search_category()

    time.sleep(2)
    ya.click_pics_xpath(YSelectors.SHOW_PICS)  # выбираем первую картинку
    time.sleep(2)
    orig_pics = ya.get_src()  # получаем ссылку первой картинки
    # проверяем что картинка открылась
    assert ya.check_exists_by_class(YSelectors.ORIG_PICS)

    time.sleep(2)
    ya.click_pics(YSelectors.NEXT_PICS)  # открываем вторую картинку
    next_pics = ya.get_src()  # получаем ее ссылку
    # проверяем что первая и вторая картинки не идентичны
    assert orig_pics != next_pics

    time.sleep(2)
    ya.click_pics(YSelectors.PREV_PICS)  # возвращаемся на первую картинку
    # проверяем что вернулись на первую картинку
    assert ya.get_src() == orig_pics

    ya.close_browser()
