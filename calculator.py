def main():
    try: 
        while True:
            num1 = int(input("What is Num1? "))
            num2 = int(input("What is Num2? "))
            
            print("=================================")
            print("1.Add")
            print("2.Subtract")
            print("3.Divide")
            print("4.Multiply")
            print("5.Power")
            print("6.Exit")
            print("=================================")
            user_input = int(input("What operation doW you want? "))
            
            
            print("num1", num1)
            print(f"Num: {num1}")
            match user_input:
                case 1:
                    print(F"{num1} + {num2} = {add(num1, num2)}")
                case 2: 
                    print(F"{num1} - {num2} = {subtract(num1, num2)}")
                case 3: 
                    print(F"{num1} / {num2} = {divide(num1, num2)}")
                case 4: 
                    print(F"{num1} * {num2} = {multiply(num1, num2)}")
                case 5:
                    print(F"{num1} ^ {num2} = {power(num1, num2)}")
                case 6:
                    break #exit  
    except ValueError:
        print("Value must be Integer")

#add
def add(x, y):
    return x + y

#subtract
def subtract(x, y):
    return x - y

#divide
def divide(x, y):
    return x / y

#Multiply
def multiply(x, y):
    return x * y
    
#power
def power(x, y):
    return x ** y
    
main()