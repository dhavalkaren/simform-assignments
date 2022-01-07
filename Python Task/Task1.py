def string_to_int(string, numbers):
    """It will convert string to respective int numbers.

    Args:
        string ([str])
        numbers ([dict])

    Returns:
        [int]: [number]
    """
    temp = ""
    number = 0
    for character in string:
        temp += character
        x=numbers.get(temp)
        if x!=None:
            number = (number * 10) + x
            temp = ""
    return number


def int_to_string(number, numbers):
    """It will convert number to respective string.

    Args:
        number ([int])
        numbers ([dict])

    Returns:
        [str]: [number in words]
    """
    ans = ""
    new_dict=dict([(value, key) for key, value in numbers.items()])
    while number >= 1:
        temp = number % 10
        ans = new_dict.get(temp) + ans
        number //= 10
    return ans


def gcd_of_two_number(number1, number2):
    """It will Calculate the gcd of two numbers.

    Args:
        number1 ([int])
        number2 ([int])

    Returns:
        [int]: [Gcd of Two Number]
    """
    if number1 == 0:
        return number2
    if (number2 == 0) or (number1 == number2):
        return number1
    if number1 > number2:
        return gcd_of_two_number(number2, number1%number2)
    return gcd_of_two_number(number1, number2%number1)

def calculate_string_gcd(input1,input2):
    """It will call all function to compute a gcd from string input and return string as output.

    Args:
        input1 ([int])
        input2 ([int])

    Returns:
        [str]: [number in words]
    """
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    number1 = string_to_int(input1, numbers)
    number2 = string_to_int(input2, numbers)

    gcd = gcd_of_two_number(number1, number2)
    ans = int_to_string(gcd, numbers)
    return ans
    


if __name__ == "__main__":
    input1 = input("Input 1: ")
    input2 = input("Input 2: ")
    
    ans=calculate_string_gcd(input1,input2)
    print("Output: {}".format(ans))