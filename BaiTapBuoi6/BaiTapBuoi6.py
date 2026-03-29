from abc import ABC, abstractmethod

# Lớp trừu tượng Account
class Account(ABC):
    def __init__(self, account_id, owner_name, balance=0):
        self.account_id = account_id
        self.owner_name = owner_name
        self.__balance = balance 

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Số dư không hợp lệ!")

    # Nạp tiền
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Nạp {amount} thành công.")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    # Rút tiền
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Hiển thị thông tin
    def display_info(self):
        print(f"Mã tài khoản: {self.account_id}")
        print(f"Chủ tài khoản: {self.owner_name}")
        print(f"Số dư: {self.__balance}")


# Tài khoản tiết kiệm
class SavingsAccount(Account):
    def __init__(self, account_id, owner_name, balance=0, interest_rate=0.05):
        super().__init__(account_id, owner_name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print(f"Rút {amount} thành công từ tài khoản tiết kiệm.")
        else:
            print("Rút tiền thất bại! Số dư không đủ hoặc số tiền không hợp lệ.")

    def display_info(self):
        print("=== TÀI KHOẢN TIẾT KIỆM ===")
        super().display_info()
        print(f"Lãi suất: {self.interest_rate}")


# Tài khoản thanh toán
class CheckingAccount(Account):
    def __init__(self, account_id, owner_name, balance=0, overdraft_limit=500):
        super().__init__(account_id, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance() + self.overdraft_limit:
            self.set_balance(self.get_balance() - amount)
            print(f"Rút {amount} thành công từ tài khoản thanh toán.")
        else:
            print("Rút tiền thất bại! Vượt quá hạn mức cho phép.")

    def display_info(self):
        print("=== TÀI KHOẢN THANH TOÁN ===")
        super().display_info()
        print(f"Hạn mức thấu chi: {self.overdraft_limit}")


# Tạo tài khoản tiết kiệm
tk1 = SavingsAccount("TK001", "Nguyễn Văn A", 1000, 0.06)

# Tạo tài khoản thanh toán
tk2 = CheckingAccount("TK002", "Trần Thị B", 500, 300)

# Nạp tiền
tk1.deposit(500)
tk2.deposit(200)

# Rút tiền
tk1.withdraw(300)
tk2.withdraw(900)

# Hiển thị thông tin
print()
tk1.display_info()
print()
tk2.display_info()