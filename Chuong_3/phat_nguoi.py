from selenium import webdriver
from selenium.webdriver.common.by import By
#nguoi dan duong
driver = webdriver.Chrome()
driver.get("https://phatnguoi.com/")
print()

#click vao danh sach options phuong tien
element_options = driver.find_element(By.ID, 'loaixe')
element_options.click()
print()
#click vao option xe may
element_options = driver.find_element(By.XPATH, '//*[@id="loaixe"]/option[2]')
element_options.click()
#nhap bien so
element_options = driver.find_element(By.ID, 'bsxinput')
element_options.click()
element_options.send_keys("ABC001")

#click vao button tra ngay
element_options = driver.find_element(By.ID, 'submit-btn')
element_options.click()
print()