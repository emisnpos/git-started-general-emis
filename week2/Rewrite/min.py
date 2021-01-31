
my_list = [88, 2, 3, 28, 99, 23, 55, 11, 67, 69, 1]
new_list = []

while my_list:
    min = my_list[0]  
    for x in my_list: 
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)    

print(new_list [0])