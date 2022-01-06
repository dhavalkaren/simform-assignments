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
        if temp in numbers.keys():
            number = (number * 10) + numbers[temp]
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
    while number >= 1:
        temp = number % 10
        ans = str(get_key(numbers, temp)) + ans
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


def get_key(numbers, val):
    """It will return the key value of given number from
    numbers dictionary.

    Args:
        numbers ([dict])
        val ([int])

    Returns:
        [str]: [key value of given number]
    """
    for key, value in numbers.items():
        if val == value:
            return key


def main():
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

    input1 = input("Input 1: ")
    input2 = input("Input 2: ")

    number1 = string_to_int(input1, numbers)
    number2 = string_to_int(input2, numbers)

    gcd = gcd_of_two_number(number1, number2)
    ans = int_to_string(gcd, numbers)
    
    print("Output: {}".format(ans))


if __name__ == "__main__":
    main()