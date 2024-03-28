from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest


#Стартовая информация
@pytest.fixture(scope="module")
def main_info():
    capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='ru.ozon.app.android',
    appActivity='.ui.start.AppHostActivity',
    language='en',
    locale='US'
)
    url = 'http://localhost:4723'
    driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield driver
    driver.quit()

#Поиск товара
def test_search(main_info):
    driver = main_info
    wait = WebDriverWait(driver, 10)
    find = lambda by, value: wait.until(EC.presence_of_element_located((by, value)))
    find(AppiumBy.ACCESSIBILITY_ID, value='Fashion').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/searchTv').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/etSearch').send_keys('gloria jeans')
    driver.tap([(1000, 2100)])
    assert find(AppiumBy.XPATH, '//*[@text="Популярные"]').is_displayed
    print('Открыт список товаров по запросу')

#Выбор товара
def test_find_item(main_info):
    driver = main_info
    wait = WebDriverWait(driver, 10)
    find = lambda by, value: wait.until(EC.presence_of_element_located((by, value)))
    find(AppiumBy.ID, 'ru.ozon.app.android:id/sortBtn').click()
    find(AppiumBy.XPATH, "//*[@text='Высокий рейтинг']").click()
    find(AppiumBy.XPATH, '(//*[@resource-id="ru.ozon.app.android:id/imageIv"])[1]').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/favIcon').click()
    assert find(AppiumBy.ID, 'ru.ozon.app.android:id/mainBtn').is_displayed
    print('Открыта страница товара')

#Операции с корзиной
def test_cart(main_info):
    driver = main_info
    wait = WebDriverWait(driver, 10)
    find = lambda by, value: wait.until(EC.presence_of_element_located((by, value)))
    find(AppiumBy.ID, 'ru.ozon.app.android:id/btnTitleTv').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/menu_cart').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/totalStickyButton').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/closeFlowButton').click()
    find(AppiumBy.ID, 'ru.ozon.app.android:id/removeButton').click()
    find(AppiumBy.ID, 'android:id/button1').click()
    assert find(AppiumBy.XPATH, '//*[@text="Корзина пуста"]')
    print('Товар удален из корзины')
    driver.tap([(550, 2280)])