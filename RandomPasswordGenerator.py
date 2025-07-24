import random
import string
import sys
import pyperclip

my_password = []
print("----- Random Password Generator -----")
pswd_length = int(input("Enter Password Length: "))

if pswd_length < 8 or pswd_length > 20:
    print("Password must be between 8 and 20 characters long")
    sys.exit()

else:
    Password_list = string.ascii_letters + string.digits + string.punctuation
    for a in range(pswd_length):
        my_password.append(random.choice(Password_list))

    string_pswd = "".join(my_password)
    print(f"Your Password is: {string_pswd}")

    choice = input(f"Do you wish to Copy {string_pswd} ?")
    if choice.lower() == "yes":
        pyperclip.copy(string_pswd)
        print("Your Password copied to clipboard")