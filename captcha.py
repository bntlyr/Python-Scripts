import string
import random

isRunning = True
captcha = ""
#captcha checker
def main():
    global isRunning
    global captcha 
    captcha = generate_captcha()
    print("To prove that you are not a robot.")
    print(f"Type what yo see here: {captcha}")
    user_input = input("What do you see?: ")
    check_captcha_user(user_input)
        
        
#generate capthca
def generate_captcha():
    #random strings of alphabets, numbers, and symbol
    characters = string.ascii_letters + string.digits + string.punctuation  
    return ''.join(random.choice(characters) for i in range(8))

#get user input
#check if user input is same with captcha
def check_captcha_user(user_input):
    global captcha
    if(captcha == user_input):
        print("You are not a robot.")
    else:
        print("You are a robot!")
    
main()