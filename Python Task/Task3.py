strings_list = list(map(str, input("Enter Strings: ").split()))
result = {}

for string in strings_list:
    sorted_str = "".join(sorted(string))
    x=result.get(sorted_str)
    if x!=None:
        result[sorted_str].append(string)
    else:
        result[sorted_str] = [string]
print(list(result.values()))
