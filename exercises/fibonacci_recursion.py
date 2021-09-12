
def fibo(num):
    # base case
    if (num == 1 or num == 0):
        return 1
    # recursion
    else: 
        return fibo(num-1) + fibo(num-2)

if __name__ == "__main__":
    while True:
        user_num = int(input("Enter number: "))
        print(fibo(user_num))