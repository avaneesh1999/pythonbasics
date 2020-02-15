def count_substring(string, sub_string):
    index = 0
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if string[i:i + len(string)] == sub_string:
                index = index + 1
    return index


if __name__ == '__main__':
    string = input("enter the string").strip()
    sub_string = input("enter the sunstring").strip()

    count = count_substring(string, sub_string)
    print(count)

    print(
    'ab123'.isalnum())