# Return array of indices of 2 element in num_Array that sum up to target
def twoSum(num_array, target):
    for index in range(len(num_array)):
        current_num = num_array[index]
        complement = target - current_num
        for sub_index in range(index+1,len(num_array)):
            sub_num = num_array[sub_index]
            if complement == sub_num:
                return [index,sub_index]  
    return "Error"
if __name__=="__main__":
    array = input("Enter a array of number: ").split(',')
    num_array = [int(x) for x in array]
    target = int(input("Enter a target that you want: "))

    print(twoSum(num_array, target))