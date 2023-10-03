class Atm:
    # initialize
    def __init__ (self, balance, name, exp, cvv, bank):
        self.balance = balance
        self.name = name
        self.exp = exp
        self.cvv = cvv
        self.bank = bank
    # Atm method
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"You made a deposit of {amount} USD.")
    
    def transfer(self, amount, promptpay):
        self.balance = self.balance - amount
        print(f"You made a transfer {amount} USD to promptpay no. {promptpay}")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"You made a withdraw {amount} USD")

    def otp(self):
        number = [0,1,2,3,4,5,6,7,8,9]
        otp_nums = str(random.choice(number)) + str(random.choice(number)) + str(random.choice(number)) + str(random.choice(number))
        print("You have requested for OTP")
        print(f"Your OTP is {otp_nums}. Please use within 5 minutes")

atm1 = Atm(5000, "Tony", "03/28", "942", "BBL")

atm1.withdraw(5000)
