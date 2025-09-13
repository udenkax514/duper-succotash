
class Dog(): 
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age  
        self.breed = breed 
        my_dog = Dog("Buddy", 3, "Golden Retriever")
        type(my_dog)
    def bark(self):
        print("Woof! my name is {}".format(self.name))  

        class Account():
            def __init__(self,owner,balance=0,deposit=0,withdraw=0):
                self.owner = owner
                self.balance = balance
                self.deposit = deposit
                self.withdraw = withdraw 
                acct1 = Account("John",100)
                type(acct1) 
                print(acct1.owner) 
                print(acct1.balance) 
                print(acct1.deposit) 
                print(acct1.withdraw) 
                acct1.deposit(50) 
                return "Deposit successful" 

            def withdraw(self,amount):
                if amount > self.balance:
                    return "Insufficient funds"
                self.balance -= amount
                return "Withdrawal successful"  
            
x = 5
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.") 
finally:
    print('All Done!')
 
def get_integer():
    while True:
        try: 
            get_integer = int(input("Please enter an integer: "))
            return get_integer
        except ValueError:
            print("Invalid input. Please enter an integer.") 

            def my_fun(): 
                first = 1 
                second = 2 
                print(first)
                print(second) 
                my_fun()

 
 

