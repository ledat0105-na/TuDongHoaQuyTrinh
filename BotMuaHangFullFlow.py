import re
import time
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://automationexercise.com"

LOGIN_EMAIL = "tle723772@gmail.com"
LOGIN_PASSWORD = "dat1234"

SEARCH_KEYWORD = "shirt"

SMTP_EMAIL = "tle723772@gmail.com"

SMTP_APP_PASSWORD = "vwkq jxcy pwez scvw"

RECEIVER_EMAIL = "tle723772@gmail.com"

CARD_NAME = "LE NGUYEN TIEN DAT"
CARD_NUMBER = "4111111111111111"
CARD_CVC = "123"
CARD_EXP_MONTH = "12"
CARD_EXP_YEAR = "2030"

STEP_DELAY = 0.5
TYPE_DELAY = 0.01

def create_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    return driver

def wait(driver, timeout=30):
    return WebDriverWait(driver, timeout)

def pause(seconds=None):
    if seconds is None:
        seconds = STEP_DELAY
    time.sleep(seconds)

def remove_ads(driver):
    try:
        driver.execute_script("""
            document.querySelectorAll('iframe, ins, .adsbygoogle').forEach(e => e.remove());
        """)
    except Exception:
        pass

def click_element(driver, locator, timeout=30):
    print("Đang tìm nút cần bấm...")
    pause()

    element = wait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
    pause()

    try:
        wait(driver, 3).until(EC.element_to_be_clickable(locator))
        element.click()
    except Exception:
        driver.execute_script("arguments[0].click();", element)

    pause()

    if "#google_vignette" in driver.current_url:
        print("Phát hiện quảng cáo Google chặn click, đang xử lý và thử lại...")
        driver.get(driver.current_url.replace("#google_vignette", ""))
        pause(2)
        element = wait(driver, timeout).until(EC.presence_of_element_located(locator))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        pause(1)
        driver.execute_script("arguments[0].click();", element)
        pause(2)

    remove_ads(driver)
    return element

def type_text(driver, locator, text, timeout=30):
    print("Đang nhập dữ liệu...")
    pause()

    element = wait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

    element.clear()
    pause(0.5)

    for char in text:
        element.send_keys(char)
        time.sleep(TYPE_DELAY)

    pause()
    return element

def get_price_number(price_text):
    numbers = re.findall(r"\d+", price_text)

    if not numbers:
        return 999999999

    return int(numbers[0])

def page_has_text(driver, text):
    return text.lower() in driver.page_source.lower()

def send_email(subject, body):
    try:
        print("Đang gửi email thông báo kết quả...")

        app_password = SMTP_APP_PASSWORD.replace(" ", "")

        if SMTP_APP_PASSWORD == "DIEN_MA_APP_PASSWORD_GMAIL_VAO_DAY":
            print("Bạn chưa điền SMTP_APP_PASSWORD nên không gửi được mail.")
            return

        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain", "utf-8"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SMTP_EMAIL, app_password)
        server.sendmail(SMTP_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        print("Đã gửi email thành công.")

    except Exception as e:
        print("Gửi email thất bại:", e)

def login(driver):
    print("\n========== BƯỚC 1: MỞ WEBSITE ==========")
    driver.get(BASE_URL)
    pause(3)
    remove_ads(driver)

    print("\n========== BƯỚC 2: ĐĂNG NHẬP ==========")
    click_element(driver, (By.XPATH, "//a[contains(text(),'Signup / Login')]"))

    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='login-email']"), LOGIN_EMAIL)
    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='login-password']"), LOGIN_PASSWORD)

    click_element(driver, (By.CSS_SELECTOR, "button[data-qa='login-button']"))

    pause(3)
    remove_ads(driver)

    if page_has_text(driver, "Logged in as"):
        print("Đăng nhập thành công.")
    elif page_has_text(driver, "Your email or password is incorrect"):
        raise Exception("Sai email hoặc mật khẩu đăng nhập.")
    else:
        print("Không thấy dòng Logged in as, nhưng vẫn tiếp tục chạy flow.")

def clear_cart_if_has_old_products(driver):
    print("\n========== KIỂM TRA GIỎ HÀNG CŨ ==========")

    try:
        click_element(driver, (By.XPATH, "//a[contains(text(),'Cart')]"), timeout=10)
        pause(2)

        delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".cart_quantity_delete")

        if len(delete_buttons) == 0:
            print("Giỏ hàng đang trống hoặc không có sản phẩm cũ.")
            return

        print(f"Đang xóa {len(delete_buttons)} sản phẩm cũ trong giỏ hàng...")

        for btn in delete_buttons:
            try:
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
                pause(1)
                btn.click()
                pause(2)
            except Exception:
                try:
                    driver.execute_script("arguments[0].click();", btn)
                    pause(2)
                except Exception:
                    pass

        print("Đã xử lý giỏ hàng cũ.")

    except Exception:
        print("Bỏ qua bước xóa giỏ hàng cũ.")

def search_product(driver):
    print("\n========== BƯỚC 3: VÀO TRANG PRODUCTS ==========")
    click_element(driver, (By.XPATH, "//a[contains(@href, '/products')]"))
    remove_ads(driver)

    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "search_product"))
    )

    print(f"\n========== BƯỚC 4: TÌM KIẾM SẢN PHẨM '{SEARCH_KEYWORD}' ==========")
    type_text(driver, (By.ID, "search_product"), SEARCH_KEYWORD)

    click_element(driver, (By.ID, "submit_search"))

    wait(driver).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Searched Products') or contains(text(),'SEARCHED PRODUCTS')]")
        )
    )

    pause(3)
    remove_ads(driver)
    print("Đã tìm kiếm xong.")

def choose_lowest_price_product(driver):
    print("\n========== BƯỚC 5: CHỌN SẢN PHẨM GIÁ THẤP NHẤT ==========")

    pause(2)

    products = driver.find_elements(By.CSS_SELECTOR, ".product-image-wrapper")
    product_list = []

    print("Danh sách sản phẩm tìm được:")

    for product in products:
        try:
            name = product.find_element(By.CSS_SELECTOR, ".productinfo p").text.strip()
            price_text = product.find_element(By.CSS_SELECTOR, ".productinfo h2").text.strip()
            add_button = product.find_element(By.CSS_SELECTOR, ".productinfo a.add-to-cart")

            name_lower = name.lower()

            if (
                "shirt" in name_lower
                or "t-shirt" in name_lower
                or "tshirt" in name_lower
            ):
                price_number = get_price_number(price_text)

                product_list.append({
                    "name": name,
                    "price_text": price_text,
                    "price_number": price_number,
                    "button": add_button
                })

                print(f"- {name} | {price_text}")

        except Exception:
            continue

    if len(product_list) == 0:
        raise Exception("Không tìm thấy sản phẩm nào có từ khóa shirt ở trang đầu.")

    selected = min(product_list, key=lambda x: x["price_number"])

    print("\nSản phẩm được chọn:")
    print("Tên:", selected["name"])
    print("Giá:", selected["price_text"])

    pause(3)
    return selected

def add_to_cart(driver, product):
    print("\n========== BƯỚC 6: THÊM SẢN PHẨM VÀO GIỎ HÀNG ==========")

    button = product["button"]

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", button)
    pause(2)

    try:
        button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", button)

    pause(2)

    wait(driver).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Added!') or contains(text(),'Your product has been added to cart')]")
        )
    )

    print("Đã thêm sản phẩm vào giỏ hàng.")

    print("\n========== BƯỚC 7: VÀO GIỎ HÀNG ==========")
    click_element(driver, (By.XPATH, "//u[contains(text(),'View Cart')] | //a[contains(text(),'View Cart')]"))

    pause(2)
    remove_ads(driver)

def verify_cart_quantity(driver):
    print("\n========== BƯỚC 8: VERIFY SỐ LƯỢNG = 1 ==========")

    wait(driver).until(
        EC.visibility_of_element_located((By.ID, "cart_info"))
    )

    pause(2)

    quantity_elements = driver.find_elements(By.CSS_SELECTOR, ".cart_quantity button")

    if len(quantity_elements) == 0:
        raise Exception("Không tìm thấy số lượng sản phẩm trong giỏ hàng.")

    quantity = quantity_elements[0].text.strip()

    print("Số lượng trong giỏ hàng:", quantity)

    if quantity != "1":
        raise Exception(f"Số lượng không đúng. Mong muốn = 1, thực tế = {quantity}")

    print("Verify thành công: số lượng = 1.")
    pause(2)

def checkout(driver):
    print("\n========== BƯỚC 9: PROCEED TO CHECKOUT ==========")

    click_element(driver, (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]"))

    wait(driver).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Address Details') or contains(text(),'Review Your Order')]")
        )
    )

    print("Đã vào trang checkout.")
    pause(2)

    print("\n========== BƯỚC 10: NHẬP COMMENT ==========")

    try:
        type_text(
            driver,
            (By.NAME, "message"),
            "Don hang test tu dong bang Python Selenium."
        )
        print("Đã nhập comment.")
    except Exception:
        print("Không tìm thấy ô comment, bỏ qua.")

    print("\n========== BƯỚC 11: PLACE ORDER ==========")
    click_element(driver, (By.XPATH, "//a[contains(text(),'Place Order')]"))

def payment(driver):
    print("\n========== BƯỚC 12: NHẬP THÔNG TIN THANH TOÁN GIẢ ==========")

    wait(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='name-on-card']"))
    )

    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='name-on-card']"), CARD_NAME)
    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='card-number']"), CARD_NUMBER)
    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='cvc']"), CARD_CVC)
    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='expiry-month']"), CARD_EXP_MONTH)
    type_text(driver, (By.CSS_SELECTOR, "input[data-qa='expiry-year']"), CARD_EXP_YEAR)

    print("\n========== BƯỚC 13: XÁC NHẬN THANH TOÁN ==========")

    click_element(driver, (By.CSS_SELECTOR, "button[data-qa='pay-button']"))

    wait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-qa='order-placed']"))
    )

    print("Đặt hàng thành công.")
    pause(3)

def main():
    driver = create_driver()

    status = "THẤT BẠI"
    product_name = ""
    product_price = ""
    error_message = ""

    try:
        login(driver)

        clear_cart_if_has_old_products(driver)

        search_product(driver)

        selected_product = choose_lowest_price_product(driver)

        product_name = selected_product["name"]
        product_price = selected_product["price_text"]

        add_to_cart(driver, selected_product)

        verify_cart_quantity(driver)

        checkout(driver)

        payment(driver)

        status = "THÀNH CÔNG"
        error_message = "Không có lỗi."

    except Exception as e:
        status = "THẤT BẠI"
        error_message = traceback.format_exc()
        print("\n========== CÓ LỖI XẢY RA ==========")
        print(error_message)

    finally:
        if status == "THÀNH CÔNG":
            subject = f"Kết quả BOT mua hàng AutomationExercise: {status}"
            body = f"""KẾT QUẢ BOT MUA HÀNG FULL FLOW

Website: {BASE_URL}
Tài khoản đăng nhập: {LOGIN_EMAIL}
Từ khóa tìm kiếm: {SEARCH_KEYWORD}

Trạng thái: {status}
Sản phẩm đã chọn: {product_name}
Giá sản phẩm: {product_price}
Số lượng verify: 1
"""
            send_email(subject, body)
        else:
            print("\nKhông gửi email vì quá trình chạy THẤT BẠI.")

        print("\n========== HOÀN TẤT CHƯƠNG TRÌNH ==========")
        input("Nhấn Enter để thoát...")

        driver.quit()

if __name__ == "__main__":
    main()