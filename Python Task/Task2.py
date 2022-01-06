def generate_parenthesis(str, pos, n, open, close, ans):
    """It will create all combinations of well-formed parenthese.

    Args:
        str ([string])
        pos ([int])
        n ([int])
        open ([int])
        close ([int])
        ans ([list])

    Returns:
        [list]: [List of combinations of well-formed parenthese]
    """
    if close == n:
        temp = "".join(str)
        ans.append(temp)                   
        return ans                                               
    else:
        if open > close:
            str[pos] = ")"
            generate_parenthesis(str, pos + 1, n, open, close + 1, ans)
        if open < n:
            str[pos] = "("
            generate_parenthesis(str, pos + 1, n, open + 1, close, ans)
    return ans


number = int(input("Enter Number: "))
str = [""] * 2 * number
ans = []
print(generate_parenthesis(str, 0, number, 0, 0, ans))
