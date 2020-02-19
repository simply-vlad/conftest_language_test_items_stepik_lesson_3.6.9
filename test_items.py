import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_basket_should_visible(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("#add_to_basket_form")
    assert button, f"Button not found {button}"