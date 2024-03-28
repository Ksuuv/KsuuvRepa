# Find Element by:

# CSS

# .class  (какой то класс)
# .class.class   (если у элемента несколько классов)
# #id     (какой то ID)  
# [attribute]  (например [Type])
# [attribute='hidden']   (например [Type='Hidden'])
# [Type*='idde']    (поиск всех аттрибутов у которых в названии есть 'idde')
# [Type^='hidde']        (если знаем как начинается строка)
# [Type$='idden']        (если знаем как заканчивается строка)
# [class~='requiredField'] (поиск по одному из значений аттрибута)
# form[method='post'] input  (если нужно найти один из вложенных тэгов под указаным тэгом)
# form[method='post'] > input (если нужно найти непосредственно следующий вложенный тэг в указанном)
#input#search   (поиск по ID с привязкой его тэга)

# XPATH
# каждый селектор начинается с '//' и в поиске аттрибуда строка начинается с '@'

# //li[@class='tab active']   (поиск тега li у которого есть class с аттрибутом 'tab active')
# //*[@class='tab active']     (поиск по любому тэгу с конкретным классом)
# //li[@class='tab'][2]       (если несколько одинаковых тэгов с одинаковыми классами, можно указать цифру порядк номер тэга)
# (//*[text()='Share'])[3]    (если не находит по индексу, можно взять все кроме индекса в скобки)
# //li[contains(@class='tab')][3]      (найти все теги li в которых содержиться указанный класс и указать конкретный номер тега)
# //*[text()='Simple Button']    (поиск по конкретному тексту)
# //*[contains(text(), 'Simple Button')]  (поиск по частичному совпадению текста)
# //label[@class='form-check-label' and contains(text(), 'One')]  (можно делать комбинированные запросы, например по классу и тексту)
# //label[@class='form-check-label']/folowing::input[@value='One'] (найти любой элемент ниже по дереву)
# //*[@id='div_id']/child::label   (найти дочерний элемент этого тэга, самый первый)
# //*[@id='div_id']/descendant::label  (найти все подобные элементы дочерние)
# //*[@class='form-label']/ancestor::div  (найти предков элемента по div)
# //*[@class='form-label']/ancestor::div[2]  (найти предка под номером 2)
# //*[@class='form-label']/parent::*  (найти ближайшего родителя вверх по дереву)
# //*[@class='form-label']/preceding::*[@data-scrollbar='True']    (поиск элемента который в любом месте выше по дереву)


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

def test_wiki():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    search = driver.find_element(By.XPATH, '//*[@class="gLFyf"]')
    search.click()
    search.send_keys('wikipedia')
    sleep(2)
    search.submit()
    sleep(2)
    find_link = driver.find_element(By.XPATH, "//*[text()='Википедия — свободная энциклопедия']")
    find_link.click()
    sleep(2)
    btn1 = driver.find_element(By.ID, 'n-content').click()
    sleep(2)
    btn2 = driver.find_element(By.LINK_TEXT, 'Содержание').click()
    sleep(2)
    btn3 = driver.find_element(By.LINK_TEXT, 'Техника').click()
    sleep(2)
    btn4 = driver.find_element(By.CLASS_NAME, 'mw-wiki-logo').click()
    sleep(5)
    search_wiki = driver.find_element(By.ID, 'searchInput')
    search_wiki.click()
    sleep(2)
    search_wiki.send_keys('Сакура')
    sleep(2)
    search_wiki.submit()
    sleep(2)
    assert driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table/tbody/tr[4]/td')
    sleep(5)
    