def inputNumber(message = "", errorMessage = "Please Enter A Valid Number", comparator = lambda x: True, floatingPoint = False):
    """" Lets user input an integer """
    while True:
        inputValue = input(message)
        try:
            if floatingPoint:
                inputValue = float(inputValue)
            else:
                inputValue = int(inputValue)
                
            if comparator(inputValue):
                return inputValue
            else:
                raise ValueError
            
            break
        except ValueError:
            print(errorMessage, "Input Value:", inputValue)
            

def inputComparator(message = "", errorMessage = "Please Enter Valid Value", comparator = lambda x: True, force_lower = False, strip = False):
    """ Lets user input a valid string that is validated by a comparator """
    while True:
        inputValue = input(message)
        if force_lower:
            inputValue = inputValue.lower()
        if strip:
            inputValue = inputValue.strip()
        try:
            if comparator(inputValue):
                return inputValue
            else:
                raise ValueError
            break
        except ValueError:
            print(errorMessage, "Input Value:", inputValue)
            
            
def notblank(value):
    """ Returns whether the argument is a blank string or a whitespace """
    if len(value) == 0:
        return False
    return not value.isspace()

def getAge(currentDate, birthDate):
    """ Returns the age in years """
    age = currentDate.year - birthDate.year - 1
    
    if currentDate.month > birthDate.month:
        age += 1
        
    if currentDate.month == birthDate.month and currentDate.day >= birthDate.day:
        age += 1
        
    return age


def isNumber(val, floatingPoint = False):
    """ Returns True when the value is a number returns false otherwise """
    try:
        if floatingPoint:
            float(val)
        else:
            int(val)
    except:
        return False
    else:
        return True
    
    
def isWhole(number):
    """ Returns True when the number is a whole number otherwise false"""
    return number % 1 == 0

def multipleValidation(*argv):
    """ Allows for multiple inorder assessment of boolean lambdas  """
    def validate(val):
        for validator in argv:
            if validator(val) == False:
                return False
        return True
    return validate


def hasNumberOrIsSpace(val):
    """ Returns true when the given character only contains letters and spaces """
    for letter in val:
        if letter.isdigit():
            return False
    if val.isspace():
        return False
    
    return True

import datetime
def isValidDate(val, dateformat):
    try:
        datetime.datetime.strptime(val, dateformat)
    except ValueError:
        return False
    else:
        return True
    
    
def isValidMonthDate(month, day):
    """         jan  feb mar apr may jun jul aug sep oct nov dec"""
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day <= monthDays[month - 1] and  day > 0


def printAsTable(table, padding = 3):
    # Display a new line if table is empty
    if len(table) == 0:
        print()
        return
    
    # Check if array is rectangular
    colLen = len(table[0])
    for row in table:
        if colLen != len(row):
            raise ValueError
    
    
    maxCol = [0 for val in table[0]]
    for indexRow, row in enumerate(table):
        for indexCol, col in enumerate(row):
            maxCol[indexCol] = max(maxCol[indexCol], len(str(col)))
        
    for indexRow, row in enumerate(table):
        for indexCol, col, in enumerate(row):
            colWidth =  maxCol[indexCol]
            print("".join(str(col).ljust(colWidth + padding)), end = "")
        print()
        