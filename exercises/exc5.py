def create_string_list(string):
    lst = []
    ini_num = 0
    while True:
        length = len(string)
        ini_string = ""
        
        while len(ini_string) < len(string):
            remaining = ini_num % length
            ini_string += string[remaining]
            ini_num += 1
        
        lst.append(ini_string)
        ini_num += 1
        if lst.count(string) == 2:
            break
    lst.pop(-1)    
    return lst

if __name__ == "__main__":
    string1 = input("Enter the first string: ")
    string2 = input("Enter another string: ")
    if len(string1) != len(string2):
        print("No")
    else:
        check_lst = create_string_list(string1)
        if string2 in check_lst:
            print("Yes")
        else:
            print("No")











