
# 1. Define the function
def my_upper_case(input_string):
    return input_string.upper()

# 2. Get user input
user_input_text = input("What text do you need in uppercase: ")

# 3. Call the function with the user's input and store the result
uppercase_result = my_upper_case(user_input_text)

# 4. Print the result
print(uppercase_result)


class card:
    def _init_(self,suit,rank):
        self.suit = suit
        self.rank = rank


    def _str_(self): 
         return self.rank + "of" + self.suit
two_hearts = card("Heart", "Two")
two_hearts
print(two_hearts)
        


 
