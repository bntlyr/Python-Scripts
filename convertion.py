class Numerals:
    #constructor here
    def __init__(self): 
        #ROM_DICT is for roman to numerals dictionary
        self.ROM_DICT  = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        } 
        
        #NUM_DICT is for numeral to roman dictionary
        self.NUM_DICT = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ] 


class RomanNumerals(Numerals): #applying inheritance 
    def __init__(self):
        super().__init__()
    
    # from integer to roman convertion
    def to_roman(self, value): #passing on int value, and Dictionary
        roman = ""
        for key, val in self.ROM_DICT.items(): #key=value | 'I':1 
            while value % val != val: #less than but more pythonic
                value = value - val
                roman += key
        return roman
    
    # from roman to integer convertion
    def from_roman(self, roman): #passing on string value and Dictionary
        value = 0
        for key, val in self.NUM_DICT.items():
            while roman.startswith(key):
                roman = roman[len(key)]
                value += val
        return value

class Roman_Numeral_Converter: #class to be used in def main para sa encapsulation
    def __init__(self):
        self.RomanNumerals = RomanNumerals()
        
    def convert_To_roman(self, num): #validating the output if correct
        self.validate_integer(num)
        return self.integer_to_roman.convert(num)
        
    def convert_From_roman(self, roman):
        self.validate_roman(roman)
        return self.roman_to_integer.convert(roman)
        
    def validate_integer(self, num): 
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        if num <= 0 or num > 5000: #checking if yung input is mag exceed ng 5000
            raise ValueError("Input must be a whole number between 1 and 5000")

    def validate_roman(self, roman):
        valid_characters = set('IVXLCDM')
        for char in roman.upper(): #converts to upper bago mag validate para accepted lowercases
            if char not in valid_characters:
                raise ValueError("Invalid Roman numeral character found")
        
#global variables
isRunning = True
def main():
    converter = Roman_Numeral_Converter() #new instance of the class
    
    #loop to keep asking if input is wrong
    while isRunning:
        try:
            #main menu
            print("==========================================")
            print("Main Menu")
            print("==========================================")
            print("1. Convert an Integer to Roman Numeral")
            print("2. Convert a Roman Numeral to Integer")
            print("3. Exit")
            print("==========================================")
            options = int(input("Enter your choice: "))
            match options: #using match for readability
                case 1:
                    num = int(input("Enter Integer: "))
                    print(f"Output in Roman numerals is ( {converter.convert_To_roman(num)} ).")
                case 2:
                    roman = input("Enter Roman Numeral: ")
                    print(f"Output in Integer is ( {converter.convert_To_roman(roman)} ).")
                    converter.convert_From_roman()
                case 3:
                    isRunning = False  
        except ValueError: #will catch error if mali yung input
            print("Input must only be 1,2,3")
            print()
        
if __name__ == "__main__": #standard practice in python sabi ni youtube
    main()
#dont remove comments (for github accessors)
#creator "bntlyr" -Bently Rafa
#can be used as another module just use import