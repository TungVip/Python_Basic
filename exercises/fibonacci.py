
def create_fibo(num):
    fibo_lst = [1,1]
    while len(fibo_lst) < num:
        add_num = fibo_lst[-1] + fibo_lst[-2]
        fibo_lst.append(add_num)
    return fibo_lst      

if __name__ == "__main__":
    while True:
        user_num = int(input("Enter number: "))
        fibo_list = create_fibo(user_num)   
        print(fibo_list[user_num-1])
