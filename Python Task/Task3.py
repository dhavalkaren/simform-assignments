def main():
    strings_list = list(map(str, input("Enter Strings: ").split()))
    result = {}

    for string in strings_list:
        sorted_str = "".join(sorted(string))
        if sorted_str in result:
            result[sorted_str].append(string)
        else:
            result[sorted_str] = [string]

    print(list(result.values()))


if __name__ == "__main__":
    main()