class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount

    
    
    def deposit(self, amount):
        """พัฒนาเมธอดฝากเงิน"""
        if amount > 0:
            self._update_balance(amount)
            print(f"ฝากเงินสำเร็จ: {amount}")
        else:
            print("จำนวนเงินฝากต้องมากกว่า 0")

    def withdraw(self, amount):
        """พัฒนาเมธอดถอนเงินพร้อมเช็คยอดคงเหลือ"""
        if amount <= 0:
            print("จำนวนเงินถอนต้องมากกว่า 0")
        elif amount > self.get_balance():
            print("ยอดเงินในบัญชีไม่เพียงพอ")
        else:
            self._update_balance(-amount)
            print(f"ถอนเงินสำเร็จ: {amount}")
    