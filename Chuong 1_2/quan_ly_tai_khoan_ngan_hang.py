# Xây dựng hệ thống quản lý tài khoản ngân hàng với các loại tài khoản khác nhau

def print_separator():
    print("=" * 50)


class Account:
    """Lớp cơ sở cho tất cả các loại tài khoản"""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền nạp phải > 0")
        self.balance += amount
        print(f"{self.owner}: đã nạp {amount:,} VND, số dư hiện tại {self.balance:,} VND")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")
        if amount > self.balance:
            raise ValueError("Số dư không đủ")
        self.balance -= amount
        print(f"{self.owner}: đã rút {amount:,} VND, số dư còn lại {self.balance:,} VND")

    def get_balance(self):
        return self.balance

    def __str__(self):
        account_type = self.__class__.__name__
        return f"{account_type} của {self.owner}, số dư {self.balance:,} VND"


class SavingsAccount(Account):
    """Tài khoản tiết kiệm có lãi suất"""
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.owner}: áp dụng lãi suất {self.interest_rate*100:.2f}%, lãi {interest:,.2f} VND, số dư {self.balance:,.2f} VND")


class CheckingAccount(Account):
    """Tài khoản thanh toán có phí mỗi giao dịch"""
    def __init__(self, owner, balance=0, fee=1000):
        super().__init__(owner, balance)
        self.fee = fee

    def withdraw(self, amount):
        total = amount + self.fee
        if total > self.balance:
            raise ValueError("Số dư không đủ sau khi tính phí giao dịch")
        super().withdraw(amount)
        self.balance -= self.fee  
        print(f"{self.owner}: phí giao dịch {self.fee:,} VND áp dụng, số dư còn lại {self.balance:,} VND")


# ví dụ sử dụng
if __name__ == "__main__":
    print_separator()
    print("HỆ THỐNG QUẢN LÝ TÀI KHOẢN NGÂN HÀNG")
    print_separator()

    sa = SavingsAccount("Anh", 500000, interest_rate=0.02)
    sa.deposit(100000)
    sa.apply_interest()
    sa.withdraw(200000)

    print_separator()

    ca = CheckingAccount("Bình", 1000000, fee=5000)
    ca.withdraw(200000)
    ca.deposit(500000)
    ca.withdraw(900000)

    print_separator()
    print("Thông tin tài khoản cuối cùng:")
    print(sa)
    print(ca)
