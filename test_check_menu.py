import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
#    options = webdriver.ChromeOptions()
#    options.add_argument("start-maximized")
#    wd = webdriver.Chrome(chrome_options=options)
    wd = webdriver.Firefox(firefox_binary="C:\\Program Files\\Mozilla Firefox\\firefox.exe")
#    wd = webdriver.Ie()
#    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_check_menu(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    menu_list = driver.find_elements_by_css_selector('li#app- a')
    hrefs = list_hrefs(menu_list)
    for href in hrefs:
        get_check_tag(driver, href)
        menu_list_inside = driver.find_elements_by_css_selector('li#app- li a')
        if len(menu_list_inside) > 0:
            hrefs_inside = list_hrefs(menu_list_inside)
            for href_inside in hrefs_inside:
                get_check_tag(driver, href_inside)


def get_check_tag(driver, href):
    driver.get(href)
    if are_elements_present(driver, "h1") is True:
        print("Заголовок H1 присутствует на странице " + href)


def list_hrefs(menu_list):
    hrefs = []
    for menu_item in menu_list:
        hrefs.append(menu_item.get_attribute("href"))
    return hrefs


def are_elements_present(driver, arg):
    return len(driver.find_elements_by_tag_name(arg)) > 0
