from selenium import webdriver
from selenium.webdriver.common.by import By


# người dẫn đường
driver = webdriver.Chrome()
URL= 'https://sinhvien.dau.edu.vn/sinh-vien-dang-nhap.html'
driver.get(URL)

# username
element_username = driver.find_element(By.ID, "Username")
element_username.click()
element_username.send_keys("21020586")

# password
element_password = driver.find_element(By.ID, "Password")
element_password.click()
element_password.send_keys("21020586")

# click button đăng nhập
element_login = driver.find_element(By.CSS_SELECTOR, "input[value='Đăng nhập']")
element_login.click()

print()