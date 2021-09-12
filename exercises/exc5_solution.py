# return True if is cycle string, False otherwise
def check_cycle_string(str1, str2):
    if (len(str1) != len(str2)):
        return False
    return str2 in (str1 + str1)

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter another string: ")
    if (check_cycle_string(string1, string2)):
        print("Yes")
    else:
        print("No")