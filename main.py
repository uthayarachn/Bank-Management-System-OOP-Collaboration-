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
    
class SavingsAccount(Account): 
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """คำนวณและเพิ่มดอกเบี้ยเข้ายอดเงิน"""
        interest = self.get_balance() * self.interest_rate
        self._update_balance(interest)
        print(f"คำนวณดอกเบี้ยสำเร็จ: +{interest} บาท")

   
import datetime

def log_msg(text):
    print(f"[{datetime.datetime.now()}] {text}")

def validate_price(val):
    try:
        n = float(val)
        return n if n > 0 else None
    except:
        return None


if __name__ == "__main__":
    name = input("ชื่อบัญชี: ")
    acc = SavingsAccount(name, 1000)
    log_msg(f"สร้างบัญชี {name}")
    
    amount = validate_price(input("ยอดฝาก: "))
    if amount:
        acc.deposit(amount)
        log_msg(f"ฝากเงิน {amount}")
    else:
        print("ตัวเลขผิด!")