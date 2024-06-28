class Numerals:
    # Constructor here
    def __init__(self): 
        # ROM_DICT is for roman to numerals dictionary
        self.ROM_DICT  = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
            'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        } 
        
        # NUM_DICT is for numeral to roman dictionary
        self.NUM_DICT = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ] 


class RomanNumerals(Numerals): # Applying inheritance 
    def __init__(self):
        super().__init__()
    
    # From integer to roman conversion
    def to_roman(self, value): # Passing on int value, and Dictionary
        roman = ""
        for val, key in self.NUM_DICT: # Corrected tuple unpacking
            while value >= val:
                value -= val
                roman += key
        return roman
    
    # From roman to integer conversion
    def from_roman(self, roman): # Passing on string value and Dictionary
        roman = roman.upper()  # Ensures the input is in uppercase
        value = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in self.ROM_DICT:
                value += self.ROM_DICT[roman[i:i+2]]
                i += 2
            else:
                value += self.ROM_DICT[roman[i]]
                i += 1
        return value


class Roman_Numeral_Converter: # Class to be used in def main for encapsulation
    def __init__(self):
        self.roman_numerals = RomanNumerals()
        
    def convert_to_roman(self, num): # Validating the output if correct
        self.validate_integer(num)
        return self.roman_numerals.to_roman(num)
        
    def convert_from_roman(self, roman):
        self.validate_roman(roman)
        return self.roman_numerals.from_roman(roman)
        
    def validate_integer(self, num): 
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        if num <= 0 or num > 5000: # Checking if the input exceeds 5000
            raise ValueError("Input must be a whole number between 1 and 5000")

    def validate_roman(self, roman):
        valid_characters = set('IVXLCDM')
        for char in roman.upper(): # Converts to uppercase before validating to accept lowercases
            if char not in valid_characters:
                raise ValueError("Invalid Roman numeral character found")
        

def main():
    converter = Roman_Numeral_Converter() # New instance of the class
    # Loop to keep asking if input is wrong
    while True:
        try:
            # Main menu
            print()
            print("==========================================")
            print("Main Menu")
            print("==========================================")
            print("1. Convert an Integer to Roman Numeral")
            print("2. Convert a Roman Numeral to Integer")
            print("3. Exit")
            print("==========================================")
            options = int(input("Enter your choice: "))
            match options: # Using match for readability
                case 1:
                    num = int(input("Enter Integer: "))
                    print()
                    print(f"Output in Roman numerals is {converter.convert_to_roman(num)}")
                case 2:
                    roman = input("Enter Roman Numeral: ")
                    print()
                    print(f"Output in Integer is {converter.convert_from_roman(roman)}")
                case 3:
                    print()
                    break
                case _: # Handling invalid menu choices
                    print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError as e: # Will catch error if the input is wrong
            print(e)
            print()
    print("Program Exited Successfully.") 

if __name__ == "__main__": # Standard practice in Python
    main()
# Don't remove comments (for GitHub accessors)
# Creator "bntlyr" -Bently Rafa
# Can be used as another module just use import
