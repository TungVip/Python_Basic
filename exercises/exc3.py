array = input("Enter a array of number: ").split(',')
num_array = [int(x) for x in array]

target = int(input("Enter a target that you want: "))

all_num = []
for y in num_array:
    if y not in all_num:
        all_num.append(y)

chance_list = []

for i in all_num:
    if target - i in all_num:
        chance_list.append([i,target-i])

for a in chance_list:
    if a[0] != a[1]:
        b = [a[1], a[0]]
        chance_list.remove(b)
print(chance_list)

output = []

if chance_list[0][0] != chance_list[0][1]:
    for k in chance_list[0]:
        output.append(num_array.index(k))
else:
    value = chance_list[0][0]
    index1 = num_array.index(value)
    num_array.remove(value)
    index2 = num_array.index(value)+1
    output.append(index1)
    output.append(index2)
print(output)

