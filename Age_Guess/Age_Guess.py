import pyfiglet as pyfig
from colorama import *
print(Fore.BLUE + pyfig.figlet_format("Age Guess "))
print(Fore.YELLOW + """              Created by CyberMan                      """)
print("""                    Welcome                              """)
def Age_Guess():
    print(Fore.RED + "Example : 09362011781")
    phone=input(Fore.GREEN +"Please enter your phone number >>> ")
    print(Fore.BLUE + "Example :1355 (just Enter year)")
    birth_Day=int(input(Fore.GREEN + "Please enter your Date of birth >>> "))
    Last_number=int(phone[9:11])
    Last_number*=2
    Last_number+=5
    Last_number*=50
    Last_number+=1151
    Age_Guess=Last_number-birth_Day
    finally_Age=str(Age_Guess)
    print(Fore. BLUE + "your Age Guess >",finally_Age[2:4])

Age_Guess()
