# # Login: au.test.example@mail.ru
# # Password: AIAutomationTEST1011


import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import allure

@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_open_spotify(driver_setup):
    driver = driver_setup
    driver.get('https://open.spotify.com/')
    print('Нужная страница открыта')

def test_login(driver_setup):
    driver = driver_setup
    wait = WebDriverWait(driver, 10)
    find = lambda by, value: wait.until(EC.presence_of_element_located((by, value)))
    print('Есть кнопка регистрации')
    assert find(By.CSS_SELECTOR, 'button[data-testid="signup-button"]')

    # Авторизация
    find(By.CSS_SELECTOR, '[data-testid=login-button]').click()
    print('Открыта форма авторизации')
    assert find(By.XPATH, '//*[@data-testid="login-container"]')
    find(By.ID, 'login-username').send_keys('au.test.example@mail.ru')
    find(By.XPATH, '//*[@type="password"]').send_keys('AIAutomationTEST1011')
    find(By.CLASS_NAME, 'Wrapper-sc-16y5c87-0').click()
    find(By.XPATH, '//*[@class="Type__TypeElement-sc-goli3j-0 cOJqPq sc-jSUZER sc-gKPRtg hJfyeq hgatVV"]').click()
    print('Авторизация прошла успешно')
    assert find(By.XPATH, '//*[@aria-label="AQA_Aleksandr"]')

def test_search_playlist(driver_setup):
    driver = driver_setup
    wait = WebDriverWait(driver, 10)
    find = lambda by, value: wait.until(EC.presence_of_element_located((by, value)))
    find(By.XPATH, '//a[@class="link-subtle UYeKN11KAw61rZoyjcgZ"]').click()
    print('Открыта вкладка поиска')
    assert find(By.XPATH, '//*[@class="CCi1L2OQvgdZvxkRHeKE"]')

    # Операции с поиском
    search_input = find(By.XPATH, '//input[@data-encore-id="text"]')
    search_input.send_keys('fallout 4 radio')
    find(By.XPATH, '//*[@class="_gB1lxCfXeR8_Wze5Cx9"]').click()
    print('Проверка наличия найденного плейлиста')
    assert find(By.XPATH, '//*[@title="Fallout 4 Radio Soundtrack"]')
    print('Плейлист открылся')
    assert find(By.XPATH, '//*[@data-testid="playlist-tracklist"]')
    play_btn = find(By.XPATH, '(//*[@class="Svg-sc-ytk21e-0 bneLcE"])[4]')
    play_btn.click()

    # Убираем запрос куков
    find(By.XPATH, '//*[@id="onetrust-close-btn-container"]').click()
    print('Попап с запросом cookies закрыт')

def test_user_profile_actions(driver_setup):
    driver = driver_setup
    wait = WebDriverWait(driver, 10)
    find = lambda by, value: wait.until(EC.presence_of_element_located((by, value)))

    # Прочие действия с профилем пользователя
    find(By.XPATH, '//button[@data-testid="user-widget-link"]').click()
    print('Открыто контекстное меню')
    assert find(By.XPATH, '//*[@id="context-menu"]')
    find(By.XPATH, '//a[@class="mWj8N7D_OlsbDgtQx5GW"]').click()
    print('Профиль открыт')
    assert find(By.XPATH, '//*[@class="gHImFiUWOg93pvTefeAD xYgjMpAjE5XT05aRIezb"]')
    find(By.XPATH, '//button[@class="ql0zZd7giPXSnPg75NR0"]').click()
    find(By.XPATH, '//button[@data-testid="user-widget-link"]').click()
    find(By.XPATH, '//a[@class="mWj8N7D_OlsbDgtQx5GW Vz3pFUXmll6fKB5Fc4nd"]').click()
    print('Открыта страница настроек')
    assert find(By.XPATH, '//*[@data-testid="settings-page"]')
    find(By.XPATH, '//button[@class="ql0zZd7giPXSnPg75NR0"]').click()
    assert find(By.XPATH, '//*[@class="contentSpacing"]')

    print('Тест завершен! Браузер скоро закроется')
    sleep(2)



