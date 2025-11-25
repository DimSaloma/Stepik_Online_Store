from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_basket_button(browser):
    # Открываем страницу товара
    browser.get(link)
    
    # Для проверки языка раскомментируйте строку:
    # time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Убеждаемся, что кнопка есть на странице
    assert len(add_to_basket_button) > 0, "Add to basket button is not found on the page"
