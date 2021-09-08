class atm: 
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance(self):
        print("your balance is 1000")
    def withdrawal(self,amount):
        new_amount=1000-amount
        print("you have withdrawn"+str(amount)+"your remaining balance is"+str(new_amount))
def main():
    card_number = input("insert your card number ")
    pin_number = input("enter your pin number ")
    new_user = atm(card_number,pin_number)
    print("choose your actvity")
    print("1) balance inquiry. 2) withdrawl ")
    actvity = int(input("enter activty number"))
    if(actvity==1):
        new_user.check_balance()
    elif(actvity==2):
        amount=int(input("enter the amount"))
        new_user.withdrawal(amount)
    else:
        print("what man? time is money, stop wasting time, I got work to do, enter the right number, why you wast time?")
if __name__=="__main__":
    main()