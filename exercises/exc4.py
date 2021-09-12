def check_palindrome(val):
    reverse_value = val[::-1]
    if val == reverse_value:
        return "This is a palindrome."
    else:
        return "This is not a palindrome."

if __name__ == "__main__":
    user_input = input("Enter a word to check: ")

    print(check_palindrome(user_input))

