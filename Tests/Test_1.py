from Pages.search_yandex import SearchFunc, YSelectors


# Запуск первого теста
def test_first_link(browser):
    ya = SearchFunc(browser)
    ya.go_to_site()
    # проверяем наличие поисковой строки
    assert ya.check_exists_by_selector(YSelectors.SEARCH_FIELD)

    ya.input_word()  # вводим запрос
    # проверяем что появились подсказки по запросу
    assert ya.check_exists_by_class(YSelectors.SEARCH_SUGGEST)

    ya.click_enter(YSelectors.SEARCH_BUTTON)  # нажимаем на кнопку поиска
    # проверяем что появилась страница результатов поиска
    assert ya.check_exists_by_selector(YSelectors.SEARCH_RESULT)

    # проверяем что первая ссылка ведет на сайт "tensor.ru"
    assert ya.check_first_link() == 'tensor.ru'
    ya.close_browser()
