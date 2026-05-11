import time
import smtplib
import pandas as pd
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================
# CẤU HÌNH
# =========================
URL = "https://www.phatnguoixe.com/"

# File Excel nằm cùng thư mục với file .py
FILE_EXCEL = Path(__file__).resolve().parent / "bienso.xlsx"

# Gmail SMTP
EMAIL_SENDER = "tle723772@gmail.com"
EMAIL_PASSWORD = "cgfb hmis xnjb dxtc"
EMAIL_RECEIVER = "dat_2351220007@dau.edu.vn"


# =========================
# HÀM GỬI EMAIL
# =========================
def gui_email(bien_so, chi_tiet):
    try:
        subject = "Cảnh báo phạt nguội"

        body = f"""Biển số: {bien_so}
Trạng thái: Có vi phạm

Chi tiết:
{chi_tiet}
"""

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain", "utf-8"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Đã gửi email cho biển số: {bien_so}")
        return True

    except Exception as e:
        print("Lỗi gửi email:", e)
        return False


# =========================
# CHỌN LOẠI PHƯƠNG TIỆN: Ô TÔ
# =========================
def chon_o_to(driver):
    danh_sach_xpath = [
        "//label[contains(., 'Ô tô')]",
        "//label[contains(., 'Ô Tô')]",
        "//*[contains(text(), 'Ô tô')]",
        "//*[contains(text(), 'Ô Tô')]"
    ]

    for xp in danh_sach_xpath:
        try:
            el = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, xp))
            )
            el.click()
            print("Đã chọn phương tiện: Ô tô")
            return True
        except:
            pass

    print("Không click được mục Ô tô, có thể website đang mặc định sẵn.")
    return False


# =========================
# NHẬP BIỂN SỐ
# =========================
def nhap_bien_so(driver, bien_so):
    danh_sach_selector = [
        (By.CSS_SELECTOR, "input[type='text']"),
        (By.XPATH, "//input[contains(@placeholder, 'biển số')]"),
        (By.XPATH, "//input[contains(@placeholder, 'Biển số')]"),
        (By.XPATH, "//input[contains(@placeholder, 'Nhập biển số')]"),
        (By.XPATH, "//input")
    ]

    for by, value in danh_sach_selector:
        try:
            o_nhap = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((by, value))
            )
            o_nhap.clear()
            o_nhap.send_keys(bien_so)
            print(f"Đã nhập biển số: {bien_so}")
            return True
        except:
            pass

    return False


# =========================
# CLICK NÚT KIỂM TRA
# =========================
def bam_nut_kiem_tra(driver):
    danh_sach_selector = [
        (By.XPATH, "//button[contains(., 'Kiểm tra phạt nguội')]"),
        (By.XPATH, "//button[contains(., 'Tra cứu')]"),
        (By.XPATH, "//button[@type='submit']"),
        (By.XPATH, "//input[@type='submit']")
    ]

    for by, value in danh_sach_selector:
        try:
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((by, value))
            )
            btn.click()
            print("Đã bấm nút kiểm tra")
            return True
        except:
            pass

    return False


# =========================
# PHÂN TÍCH KẾT QUẢ
# =========================
def phan_tich_ket_qua(driver, bien_so):
    time.sleep(5)

    body_text = driver.find_element(By.TAG_NAME, "body").text
    body_text_lower = body_text.lower()

    if "không tìm thấy vi phạm" in body_text_lower or "khong tim thay vi pham" in body_text_lower:
        print(f"{bien_so}: Không vi phạm")
        return False, "Không tìm thấy vi phạm"

    # Nếu có dữ liệu bảng / thông tin vi phạm thì coi như có vi phạm
    tu_khoa = ["thời gian", "địa điểm", "lỗi", "vi phạm", "biển số"]
    if any(k in body_text_lower for k in tu_khoa):
        print(f"{bien_so}: Có vi phạm")
        return True, body_text

    print(f"{bien_so}: Chưa xác định rõ, tạm coi là không vi phạm")
    return False, body_text


# =========================
# TRA CỨU 1 BIỂN SỐ
# =========================
def tra_cuu_phat_nguoi(driver, bien_so):
    driver.get(URL)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    time.sleep(2)

    # Bước 2: Chọn Ô tô
    chon_o_to(driver)
    time.sleep(1)

    # Bước 3: Nhập biển số
    if not nhap_bien_so(driver, bien_so):
        raise Exception("Không tìm thấy ô nhập biển số")

    time.sleep(1)

    # Bước 4: Bấm kiểm tra
    if not bam_nut_kiem_tra(driver):
        raise Exception("Không tìm thấy nút kiểm tra phạt nguội")

    # Bước 5: Lấy kết quả
    return phan_tich_ket_qua(driver, bien_so)


# =========================
# HÀM MAIN
# =========================
def main():
    if not FILE_EXCEL.exists():
        raise FileNotFoundError(f"Không tìm thấy file Excel: {FILE_EXCEL}")

    df = pd.read_excel(FILE_EXCEL, engine="openpyxl")

    if "BienSo" not in df.columns:
        raise Exception("File Excel phải có cột tên là: BienSo")

    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    try:
        for _, row in df.iterrows():
            bien_so = str(row["BienSo"]).strip()

            if bien_so == "" or bien_so.lower() == "nan":
                continue

            print("=" * 50)
            print(f"Đang kiểm tra biển số: {bien_so}")

            try:
                co_vi_pham, chi_tiet = tra_cuu_phat_nguoi(driver, bien_so)

                # Bước 6: Xử lý logic
                if co_vi_pham:
                    gui_email(bien_so, chi_tiet)
                else:
                    print("Không vi phạm")

            except Exception as e:
                print(f"Lỗi khi xử lý biển số {bien_so}: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()