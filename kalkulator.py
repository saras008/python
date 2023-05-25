# class kalkulator:
#     def __init__(self,bil1,bil2):
#         self.bil1=bil1
#         self.bil2=bil2
    
#     def kali(self):
#         print(int(self.bil1) * int(self.bil2))
# perkalian=kalkulator(5,5)
# perkalian.kali(5,5)

def check_user_input(input):
    try:
        value=int(input)
        print("Your input is an integer number", value)
    except ValueError:
        try:
            value=float(input)
            print("You input is a float number",value)
        except ValueError:
            print("Your input isn't int or float, Please try again")

input1 =input("Please type your first number")
check_user_input(input1)
input2 =input("Please type your second number")
check_user_input(input2)
# def perkalian(input1,input2):
#     check_user_input(input1)
#     check_user_input(input2)
#     return input1 * input2

# perkalian(2,2)