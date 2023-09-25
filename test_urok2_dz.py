import pytest
from selene.support.shared import browser
from selene import be, have


class TestOne:
    def test_google_should_find_selene(self):
        browser.open("https://www.google.com/")
        browser.element('[name="q"]').should(be.blank).type('Hello, world!').press_enter()
        browser.element('[class="kb0PBd cvP2Ce"]').should(have.text('Hello, world!'))
        print('Страница соответствует критериям поиска')

    def test_google_should_not_find_result(self):
        browser.open("https://www.google.com/")
        browser.element('[name="q"]').should(be.blank).type('FJE^hds&&Q#^e888190<>').press_enter()
        browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
        print('По запросу ничего не найдено')