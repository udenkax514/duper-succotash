#school = "teachers" "students" "parents"
from math import e


class school: 
    def __init__(self,name,roomN,ethicity) :
        self.name = str(name)
        self.roomN = int(roomN)
        self.ethicity = str(ethicity) 
        self.name = input(f"name")
        self.roomN = input(f"roomN") 
        self.ethicity = input(f"ethicity")

while True:  # keeps looping forever until we break
    try:
        guess_number = int(input("Guess a number between 1-10: "))
        if guess_number == 4:
            print("You win!")
            break   # stops the loop if correct
        else:
            print("Try again")
    except ValueError:
        print("Invalid input. Please enter a number.") 
    
    
    def func():
        return 1+1    
    
    class Person: 
        def __init__(self,name, age , heigth): 
            self.name = str(name)
            self.age = int(age)
            self.heigth = float(heigth) 
            self.name = input(f"name")
            self.age = input(f"age") 
            self.heigth = input(f"heigth") 

