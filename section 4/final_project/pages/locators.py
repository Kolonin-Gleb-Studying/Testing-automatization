# Чтобы не изменять селектор в нескольких местах их выносят во внешний файл.
# Этот файл содержит используемые селекторы

from selenium.webdriver.common.by import By

# Класс соответствующий всем объектам Page Object
class MainPageLocators():
    # Это кортеж, который содержит в себе информацию 
    # как искать и что искать. 
    # Его можно использовать в селекторах, а при изменении в верстке,
    # нужно будет изменить только как искать в этом файле
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #registration_link


class LoginPageLocators():
    # Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #registration_link
    pass
    
