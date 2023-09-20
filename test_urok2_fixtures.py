import pytest


@pytest.fixture
def browser():
    print("Выполнить перед тестом")

    yield

    print("Выполнять после теста")

@pytest.fixture
def main_page(browser):
    pass

def test_first(browser, user, main_page):
    pass

def test_second(browser, user, main_page):
    pass
