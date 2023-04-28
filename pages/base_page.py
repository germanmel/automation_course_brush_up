from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


"""Базовый класс страницы, который будем использовать везде"""
class BasePage:
    """Метод инициализирует аргументы при каждом вызове экземпляра класса"""
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    """Метод открытия страницы"""
    def open(self):
        self.driver.get(self.url)

    """Элемент виден на странице"""
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    """Элементы видны на странице"""
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """Элемент присутствует в dom дереве(может быть не виден, но он есть)"""
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    """Элементы присутствуют в dom дереве"""
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    """Элемент не виден на странице"""
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    """Элемент кликабелен"""
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """Скролл страницы к элементу"""
    def go_to_element(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locator)