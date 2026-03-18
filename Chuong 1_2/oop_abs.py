# Bài toán: hệ thống thanh toán
# 1. chuyển tiền từ ngân hàng: stk sang stk
# 2. chuyển tiền từ thẻ tín dụng

# quy tắc:
# 1. kiểm tra stk hợp lệ
# 2. kiểm tra số dư đủ để chuyển
# 3. thực hiện chuyển tiền
# 4. tính phí(free, hoặc mấy %/1 giao dịch)

# giải quyết: tạo ra quy tắc để hệ thống con tuân theo

from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    # 1. Kiểm tra stk hợp lệ
    @abstractmethod
    def check_account_number(self, account_number_receiver):
        pass
    # 2. Kiểm tra số dư đủ để chuyển
    abstractmethod
    def check_balance(self):
        pass
    # 3. Thực hiện chuyển tiền
    @abstractmethod
    def transfer_balance(self, amount):
        pass
    # 4. Tính phí
    @abstractmethod
    def calculate_fee(self, fee=0):
        pass

# 1. chuyển tiền từ ngân hàng: stk sang stk
class PaymentVietinbank(PaymentInterface):
    # 1. kiểm tra stk hợp lệ
    def check_account_number(self, account_number_receiver):
        if account_number_receiver == "00000000":
            return False
        elif len(account_number_receiver) < 8:
            return False
        elif len(account_number_receiver) > 13:   
                return False     
        else:
            return True 
    # 2. Kiểm tra số dư đủ để chuyển
    def check_balance(self):
        if self.balance < 2000:
            return False
        else:
            return True
    # 3. Thực hiện chuyển tiền
    def transfer_balance(self, amount):
        print(f"Thực hiện chuyển tiền từ tài khoản ngân hàng này sang tài khoản ngân hàng khác với số tiền: {amount:,.2f} VND.")
        self.balance -= amount
        return self.balance
    # 4. Tính phí
    def calculate_fee(self, amount=0):
        """Chuyển tiền ngân hàng: không tính phí"""
        print("Không mất phí khi chuyển tiền ngân hàng.")
        return 0
    
    def complete_transfer(self):
        self.check_account_number()
        self.check_balance()
        self.transfer_balance()
        self.calculate_fee()
       
# 2. chuyển tiền từ thẻ tín dụng
class PaymentCredit(PaymentInterface):
    def __init__(self, account_number, balance):
        super().__init__()
        self.account_number = account_number
        self.balance = balance

    # 1. kiểm tra stk hợp lệ
    def check_account_number(self):
        if self.account_number == "00000000":
            return False
        elif len(self.account_number) < 8:
            return False
        elif len(self.account_number) > 13:   
                return False     
        else:
            return True 
    # 2. Kiểm tra số dư đủ để chuyển
    def check_balance(self):
        if self.balance < 40000:
            return False
        else:
            return True
    
    # 3. Thực hiện chuyển tiền
    def transfer_balance(self, amount):
        print(f"Thực hiện chuyển tiền từ tài khoản ngân hàng này sang tài khoản ngân hàng khác với số tiền: {amount:,.2f} VND.")
        self.balance -= amount
        return self.balance
    # 4. Tính phí
    def calculate_fee(self):
        print("Tính phí chuyển tiền từ thẻ tín dụng: 1% trên tổng số tiền chuyển.")
        number_fee = self.balance * 0.01
        return number_fee
